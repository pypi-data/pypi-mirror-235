"""**Chat Models** are a variation on language models.

While Chat Models use language models under the hood, the interface they expose
is a bit different. Rather than expose a "text in, text out" API, they expose
an interface where "chat messages" are the inputs and outputs.

**Class hierarchy:**

.. code-block::

    BaseLanguageModel --> BaseChatModel --> <name>  # Examples: ChatOpenAI, ChatGooglePalm

**Main helpers:**

.. code-block::

    AIMessage, BaseMessage, HumanMessage
"""  # noqa: E501

from promptmanager.script.base.chat_models.anthropic import ChatAnthropic
from promptmanager.script.base.chat_models.anyscale import ChatAnyscale
from promptmanager.script.base.chat_models.azure_openai import AzureChatOpenAI
from promptmanager.script.base.chat_models.baidu_qianfan_endpoint import QianfanChatEndpoint
from promptmanager.script.base.chat_models.bedrock import BedrockChat
from promptmanager.script.base.chat_models.cohere import ChatCohere
from promptmanager.script.base.chat_models.ernie import ErnieBotChat
from promptmanager.script.base.chat_models.fake import FakeListChatModel
from promptmanager.script.base.chat_models.fireworks import ChatFireworks
from promptmanager.script.base.chat_models.google_palm import ChatGooglePalm
from promptmanager.script.base.chat_models.human import HumanInputChatModel
from promptmanager.script.base.chat_models.javelin_ai_gateway import ChatJavelinAIGateway
from promptmanager.script.base.chat_models.jinachat import JinaChat
from promptmanager.script.base.chat_models.konko import ChatKonko
from promptmanager.script.base.chat_models.litellm import ChatLiteLLM
from promptmanager.script.base.chat_models.minimax import MiniMaxChat
from promptmanager.script.base.chat_models.mlflow_ai_gateway import ChatMLflowAIGateway
from promptmanager.script.base.chat_models.ollama import ChatOllama
from promptmanager.script.base.chat_models.openai import ChatOpenAI
from promptmanager.script.base.chat_models.promptlayer_openai import PromptLayerChatOpenAI
from promptmanager.script.base.chat_models.vertexai import ChatVertexAI

__all__ = [
    "ChatOpenAI",
    "BedrockChat",
    "AzureChatOpenAI",
    "FakeListChatModel",
    "PromptLayerChatOpenAI",
    "ChatAnthropic",
    "ChatCohere",
    "ChatGooglePalm",
    "ChatMLflowAIGateway",
    "ChatOllama",
    "ChatVertexAI",
    "JinaChat",
    "HumanInputChatModel",
    "MiniMaxChat",
    "ChatAnyscale",
    "ChatLiteLLM",
    "ErnieBotChat",
    "ChatJavelinAIGateway",
    "ChatKonko",
    "QianfanChatEndpoint",
    "ChatFireworks",
]
