from typing import Sequence, Union

from promptmanager.script.base.agents.agent import AgentOutputParser
from promptmanager.script.base.schema import AgentAction, AgentFinish, OutputParserException


class SelfAskOutputParser(AgentOutputParser):
    """Parses self-ask style LLM calls.

    Expects output to be in one of two formats.

    If the output signals that an action should be taken,
    should be in the below format. This will result in an AgentAction
    being returned.

    ```
    Thoughts go here...
    Follow up: what is the temperature in SF?
    ```

    If the output signals that a final answer should be given,
    should be in the below format. This will result in an AgentFinish
    being returned.

    ```
    Thoughts go here...
    So the final answer is: The temperature is 100 degrees
    ```

    """

    followups: Sequence[str] = ("Follow up:", "Followup:")
    finish_string: str = "So the final answer is: "

    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
        last_line = text.split("\n")[-1]
        if not any([follow in last_line for follow in self.followups]):
            if self.finish_string not in last_line:
                raise OutputParserException(f"Could not parse output: {text}")
            return AgentFinish({"output": last_line[len(self.finish_string) :]}, text)

        after_colon = text.split(":")[-1].strip()
        return AgentAction("Intermediate Answer", after_colon, text)

    @property
    def _type(self) -> str:
        return "self_ask"
