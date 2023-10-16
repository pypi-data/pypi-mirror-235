"""Tool for the SceneXplain API."""
from typing import Optional

from promptmanager.script.base.callbacks.manager import CallbackManagerForToolRun
from promptmanager.script.base.pydantic_v1 import BaseModel, Field
from promptmanager.script.base.tools.base import BaseTool
from promptmanager.script.base.utilities.scenexplain import SceneXplainAPIWrapper


class SceneXplainInput(BaseModel):
    """Input for SceneXplain."""

    query: str = Field(..., description="The link to the image to explain")


class SceneXplainTool(BaseTool):
    """Tool that explains images."""

    name: str = "image_explainer"
    description: str = (
        "An Image Captioning Tool: Use this tool to generate a detailed caption "
        "for an image. The input can be an image file of any format, and "
        "the output will be a text description that covers every detail of the image."
    )
    api_wrapper: SceneXplainAPIWrapper = Field(default_factory=SceneXplainAPIWrapper)

    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        return self.api_wrapper.run(query)
