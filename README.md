# LLM Starter

Instructions to get students up and running with OpenRouter in the Data Science Clinic.

## Overview

We use the [LiteLLM](https://github.com/BerriAI/litellm) package to access models through [OpenRouter](https://openrouter.ai). OpenRouter allows users to choose from many different LLM models from various providers (OpenAI, Anthropic, Google, Meta, and more) through a single unified API.

## Setup

### 1. Create an OpenRouter Account and API Key

1. Go to [openrouter.ai](https://openrouter.ai) and create an account
2. Create a new API key for your account

### 2. Add Your API Key to `.env`

Add your OpenRouter API key to your `.env` file:

```
OPENROUTER_API_KEY=your-api-key-here
```

**Important:** Do NOT commit your `.env` file! It contains your private API key.

### 3. Add LiteLLM Dependency

Add `litellm` to your `pyproject.toml` dependencies:

```toml
dependencies = [
    "litellm",
]
```

## Code Examples

### Chat Completion

```python
import os
from litellm import completion

# Set environment variables
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENROUTER_API_BASE"] = os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")

response = completion(
    model="openrouter/openai/gpt-oss-120b",  # Change this to any model from OpenRouter
    messages=[{"role": "user", "content": "What is up?"}],
)

print(response.choices[0].message.content)
```

### Embeddings

```python
import os
from litellm import embedding

# Set environment variables
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENROUTER_API_BASE"] = os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")

response = embedding(
    model="openrouter/openai/text-embedding-3-small",
    input=["item one", "item two"],
)

print(response)
```

## Free Models

There are many different free models available on OpenRouter. Check [https://openrouter.ai/models/?q=free](https://openrouter.ai/models/?q=free) for a complete list.

Simply replace `"openrouter/openai/gpt-oss-120b"` with the model ID of your choice from the OpenRouter models page. Use the `openrouter/` prefix for all OpenRouter models (e.g., `openrouter/openai/gpt-3.5-turbo`).

## Paid Models

If your clinic project requires access to a paid model, contact Clinic administration to explain your use case. If the use case is appropriate and funds are available, they will create an API key with limited credits for you.
