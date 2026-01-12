# LLM Starter

Instructions to get students up and running with OpenRouter in the Data Science Clinic.

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

### 3. Add OpenAI Dependency

Add `openai` to your `pyproject.toml` dependencies:

```toml
dependencies = [
    "openai",
]
```

## Code Example

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",  # Change this to any model from OpenRouter
    messages=[{"role": "user", "content": "What is up?"}],
)

print(completion.choices[0].message.content)
```

## Free Models

There are many different free models available on OpenRouter. Check [https://openrouter.ai/models/?q=free](https://openrouter.ai/models/?q=free) for a complete list.

Simply replace `"openai/gpt-oss-120b"` with the model ID of your choice from the OpenRouter models page.

## Paid Models

If your clinic project requires access to a paid model, contact Clinic administration and they will create an API key with limited credits for you.
