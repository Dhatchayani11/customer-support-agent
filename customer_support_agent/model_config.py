
import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm
from litellm.llms.groq.chat.transformation import GroqChatConfig

ENV_FILE = Path(__file__).resolve().parent / ".env"
load_dotenv(ENV_FILE)

MODEL_NAME = os.getenv(
    "AGENT_MODEL",
    "groq/openai/gpt-oss-120b"
)

# Compatibility workaround:
# Remove GPT-OSS reasoning metadata before Groq
# receives previous assistant messages.

_original_transform_messages = GroqChatConfig._transform_messages


def _transform_messages_without_reasoning(
    self, messages, model, is_async=False
):
    sanitized_messages = []

    for message in messages:
        if isinstance(message, dict):
            message = dict(message)
            message.pop("reasoning_content", None)

        elif hasattr(message, "model_dump"):
            message = message.model_dump(exclude_none=True)
            message.pop("reasoning_content", None)

        sanitized_messages.append(message)

    return _original_transform_messages(
        self, sanitized_messages, model, is_async
    )


GroqChatConfig._transform_messages = (
    _transform_messages_without_reasoning
)

if MODEL_NAME.startswith("groq/") and not os.getenv("GROQ_API_KEY"):
    raise ValueError(
        "GROQ_API_KEY is missing from customer_support_agent/.env"
    )

AGENT_MODEL = LiteLlm(model=MODEL_NAME)
