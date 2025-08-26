# Copilot Instructions for proect01

## Project Overview
- **Purpose:** This project is a Python package for working with OpenAI-compatible agents, using the `openai-agents` library and environment-based configuration.
- **Key Files:**
  - `main.py`: Entry point, demonstrates agent instantiation and configuration loading.
  - `.env`: Stores API keys and base URLs for agent communication.
  - `pyproject.toml`: Project metadata and dependencies.

## Architecture & Patterns
- **Agent Abstraction:** Uses `AsyncOpenAI` and `OpenAIChatCompletionsModel` (imported from `agents`, assumed to be an external or future module).
- **Configuration:** All secrets and endpoints are loaded via `python-decouple` from `.env`.
- **Python Version:** Requires Python 3.13 (see `.python-version`).
- **Dependencies:**
  - `openai-agents` (>=0.2.9)
  - `python-decouple` (>=3.8)

## Developer Workflows
- **Install dependencies:**
  ```sh
  pip install -r requirements.txt  # or use pyproject.toml with pip or poetry
  ```
- **Environment setup:**
  - Copy `.env.example` to `.env` and fill in secrets (if `.env.example` exists; otherwise, see `.env`).
- **Run the project:**
  ```sh
  python main.py
  ```
- **Testing:**
  - No tests or test framework detected. Add tests in a `tests/` directory and use `pytest` or similar.

## Conventions & Integration
- **Secrets:** Never hardcode API keys; always use `.env` and `decouple.config`.
- **Extensibility:** To add new agent types, import and instantiate them in `main.py`.
- **External APIs:** Communicates with OpenAI-compatible endpoints, configurable via `.env`.

## Examples
```python
from decouple import config
from agents import AsyncOpenAI

key = config('GEMINI_API_KEY')
base_url = config('base_url')
client = AsyncOpenAI(api_key=key, base_url=base_url)
```

## Gaps & TODOs
- The `agents` module is not present in the repo; ensure it is installed or added.
- No tests or CI/CD detected.
- Update this file as the project structure evolves.
