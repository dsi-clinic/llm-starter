"""Example of using OpenRouter API for embeddings with LiteLLM."""

import os

from litellm import embedding

# Set environment variables
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENROUTER_API_BASE"] = os.getenv(
    "OPENROUTER_API_BASE", "https://openrouter.ai/api/v1"
)

response = embedding(
    model="openrouter/openai/text-embedding-3-small",
    input=["item one", "item two"],
)

print(response)
