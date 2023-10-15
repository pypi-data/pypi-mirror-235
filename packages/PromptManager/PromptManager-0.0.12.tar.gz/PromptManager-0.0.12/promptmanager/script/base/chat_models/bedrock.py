from typing import Any, Dict, Iterator, List, Optional

from promptmanager.script.base.callbacks.manager import (
    CallbackManagerForLLMRun,
)
from promptmanager.script.base.chat_models.anthropic import convert_messages_to_prompt_anthropic
from promptmanager.script.base.chat_models.base import BaseChatModel
from promptmanager.script.base.llms.bedrock import BedrockBase
from promptmanager.script.base.pydantic_v1 import Extra
from promptmanager.script.base.schema.messages import AIMessage, AIMessageChunk, BaseMessage
from promptmanager.script.base.schema.output import ChatGeneration, ChatGenerationChunk, ChatResult


class ChatPromptAdapter:
    """Adapter class to prepare the inputs from Promptmanager to prompt format
    that Chat model expects.
    """

    @classmethod
    def convert_messages_to_prompt(
        cls, provider: str, messages: List[BaseMessage]
    ) -> str:
        if provider == "anthropic":
            prompt = convert_messages_to_prompt_anthropic(messages=messages)
        else:
            raise NotImplementedError(
                f"Provider {provider} model does not support chat."
            )
        return prompt


class BedrockChat(BaseChatModel, BedrockBase):
    @property
    def _llm_type(self) -> str:
        """Return type of chat model."""
        return "amazon_bedrock_chat"

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    def _stream(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[ChatGenerationChunk]:
        provider = self._get_provider()
        prompt = ChatPromptAdapter.convert_messages_to_prompt(
            provider=provider, messages=messages
        )

        for chunk in self._prepare_input_and_invoke_stream(
            prompt=prompt, stop=stop, run_manager=run_manager, **kwargs
        ):
            delta = chunk.text
            yield ChatGenerationChunk(message=AIMessageChunk(content=delta))

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        completion = ""

        if self.streaming:
            for chunk in self._stream(messages, stop, run_manager, **kwargs):
                completion += chunk.text
        else:
            provider = self._get_provider()
            prompt = ChatPromptAdapter.convert_messages_to_prompt(
                provider=provider, messages=messages
            )

            params: Dict[str, Any] = {**kwargs}
            if stop:
                params["stop_sequences"] = stop

            completion = self._prepare_input_and_invoke(
                prompt=prompt, stop=stop, run_manager=run_manager, **params
            )

        message = AIMessage(content=completion)
        return ChatResult(generations=[ChatGeneration(message=message)])
