from io import IOBase
from typing import Any, List, Optional, Union

from promptmanager.script.base.agents.agent import AgentExecutor
from promptmanager.script.base.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent
from promptmanager.script.base.schema.language_model import BaseLanguageModel


def create_csv_agent(
    llm: BaseLanguageModel,
    path: Union[str, IOBase, List[Union[str, IOBase]]],
    pandas_kwargs: Optional[dict] = None,
    **kwargs: Any,
) -> AgentExecutor:
    """Create csv agent by loading to a dataframe and using pandas agent."""
    try:
        import pandas as pd
    except ImportError:
        raise ImportError(
            "pandas package not found, please install with `pip install pandas`"
        )

    _kwargs = pandas_kwargs or {}
    if isinstance(path, (str, IOBase)):
        df = pd.read_csv(path, **_kwargs)
    elif isinstance(path, list):
        df = []
        for item in path:
            if not isinstance(item, (str, IOBase)):
                raise ValueError(f"Expected str or file-like object, got {type(path)}")
            df.append(pd.read_csv(item, **_kwargs))
    else:
        raise ValueError(f"Expected str, list, or file-like object, got {type(path)}")
    return create_pandas_dataframe_agent(llm, df, **kwargs)
