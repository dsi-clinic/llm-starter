# LLM Starter

Instructions to get students up and running with OpenRouter in the Data Science Clinic.

## Quick Start

### 1. Create an OpenRouter Account and API Key

1. Go to [openrouter.ai](https://openrouter.ai) and create an account
2. Create a new API key for your account

### 2. Set Up Your Environment

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your-api-key-here
   ```

   **Important:** Do NOT commit your `.env` file! It contains your private API key.

### 3. Start an Interactive Docker Container

```bash
make run-interactive
```

This will build and start a Docker container with all dependencies installed.

### 4. Run the Example

Once inside the Docker container, run the example script:

```bash
uv run python examples/openrouter_example.py
```

## Free Models

There are many different free models available on OpenRouter. Check [https://openrouter.ai/models/?q=free](https://openrouter.ai/models/?q=free) for a complete list.

You can change the model in your code by modifying the `model` parameter. For example, in `examples/openrouter_example.py`:

```python
completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",  # Change this to any model from OpenRouter
    messages=[{"role": "user", "content": "What is up?"}],
)
```

Simply replace `"openai/gpt-oss-120b"` with the model ID of your choice from the OpenRouter models page.

## Paid Models

If your clinic project requires access to a paid model, contact Clinic administration and they will create an API key with limited credits for you.
