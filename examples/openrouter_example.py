"""Example of using OpenRouter API with LiteLLM."""

import os
import warnings

from litellm import completion

# Suppress Pydantic serialization warnings from LiteLLM
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

# Set environment variables
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENROUTER_API_BASE"] = os.getenv(
    "OPENROUTER_API_BASE", "https://openrouter.ai/api/v1"
)

response = completion(
    model="openrouter/openai/gpt-oss-120b",
    messages=[{"role": "user", "content": "What is up?"}],
)

print(response)
