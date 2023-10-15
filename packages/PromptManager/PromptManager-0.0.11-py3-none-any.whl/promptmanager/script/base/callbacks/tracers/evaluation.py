"""A tracer that runs evaluators over completed runs."""
from __future__ import annotations

import logging
import threading
import weakref
from concurrent.futures import Future, ThreadPoolExecutor, wait
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union, cast
from uuid import UUID

import langsmith
from langsmith.evaluation.evaluator import EvaluationResult

from promptmanager.script.base.callbacks import manager
from promptmanager.script.base.callbacks.tracers import promptmanager as promptmanager_tracer
from promptmanager.script.base.callbacks.tracers.base import BaseTracer
from promptmanager.script.base.callbacks.tracers.promptmanager import _get_executor
from promptmanager.script.base.callbacks.tracers.schemas import Run

logger = logging.getLogger(__name__)

_TRACERS: weakref.WeakSet[EvaluatorCallbackHandler] = weakref.WeakSet()


def wait_for_all_evaluators() -> None:
    """Wait for all tracers to finish."""
    global _TRACERS
    for tracer in list(_TRACERS):
        if tracer is not None:
            tracer.wait_for_futures()


class EvaluatorCallbackHandler(BaseTracer):
    """A tracer that runs a run evaluator whenever a run is persisted.

    Parameters
    ----------
    evaluators : Sequence[RunEvaluator]
        The run evaluators to apply to all top level runs.
    client : LangSmith Client, optional
        The LangSmith client instance to use for evaluating the runs.
        If not specified, a new instance will be created.
    example_id : Union[UUID, str], optional
        The example ID to be associated with the runs.
    project_name : str, optional
        The LangSmith project name to be organize eval chain runs under.

    Attributes
    ----------
    example_id : Union[UUID, None]
        The example ID associated with the runs.
    client : Client
        The LangSmith client instance used for evaluating the runs.
    evaluators : Sequence[RunEvaluator]
        The sequence of run evaluators to be executed.
    executor : ThreadPoolExecutor
        The thread pool executor used for running the evaluators.
    futures : Set[Future]
        The set of futures representing the running evaluators.
    skip_unfinished : bool
        Whether to skip runs that are not finished or raised
        an error.
    project_name : Optional[str]
        The LangSmith project name to be organize eval chain runs under.
    """

    name = "evaluator_callback_handler"

    def __init__(
        self,
        evaluators: Sequence[langsmith.RunEvaluator],
        client: Optional[langsmith.Client] = None,
        example_id: Optional[Union[UUID, str]] = None,
        skip_unfinished: bool = True,
        project_name: Optional[str] = "evaluators",
        max_concurrency: Optional[int] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.example_id = (
            UUID(example_id) if isinstance(example_id, str) else example_id
        )
        self.client = client or promptmanager_tracer.get_client()
        self.evaluators = evaluators
        if max_concurrency is None:
            self.executor: Optional[ThreadPoolExecutor] = _get_executor()
        elif max_concurrency > 0:
            self.executor = ThreadPoolExecutor(max_workers=max_concurrency)
            weakref.finalize(
                self,
                lambda: cast(ThreadPoolExecutor, self.executor).shutdown(wait=True),
            )
        else:
            self.executor = None
        self.futures: weakref.WeakSet[Future] = weakref.WeakSet()
        self.skip_unfinished = skip_unfinished
        self.project_name = project_name
        self.logged_eval_results: Dict[Tuple[str, str], List[EvaluationResult]] = {}
        self.lock = threading.Lock()
        global _TRACERS
        _TRACERS.add(self)

    def _evaluate_in_project(self, run: Run, evaluator: langsmith.RunEvaluator) -> None:
        """Evaluate the run in the project.

        Parameters
        ----------
        run : Run
            The run to be evaluated.
        evaluator : RunEvaluator
            The evaluator to use for evaluating the run.

        """
        try:
            if self.project_name is None:
                eval_result = self.client.evaluate_run(run, evaluator)
            with manager.tracing_v2_enabled(
                project_name=self.project_name, tags=["eval"], client=self.client
            ):
                eval_result = self.client.evaluate_run(run, evaluator)
        except Exception as e:
            logger.error(
                f"Error evaluating run {run.id} with "
                f"{evaluator.__class__.__name__}: {repr(e)}",
                exc_info=True,
            )
            raise e
        example_id = str(run.reference_example_id)
        with self.lock:
            self.logged_eval_results.setdefault((str(run.id), example_id), []).append(
                eval_result
            )

    def _persist_run(self, run: Run) -> None:
        """Run the evaluator on the run.

        Parameters
        ----------
        run : Run
            The run to be evaluated.

        """
        if self.skip_unfinished and not run.outputs:
            logger.debug(f"Skipping unfinished run {run.id}")
            return
        run_ = run.copy()
        run_.reference_example_id = self.example_id
        for evaluator in self.evaluators:
            if self.executor is None:
                self._evaluate_in_project(run_, evaluator)
            else:
                self.futures.add(
                    self.executor.submit(self._evaluate_in_project, run_, evaluator)
                )

    def wait_for_futures(self) -> None:
        """Wait for all futures to complete."""
        wait(self.futures)
