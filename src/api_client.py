"""
OpenRouter API Client
Handles all communication with the OpenRouter API.
"""

import requests
from config.settings import OPENROUTER_API_KEY, MODEL, API_BASE_URL, MAX_TOKENS, TEMPERATURE


class OpenRouterClient:
    """Wrapper for the OpenRouter API."""

    def __init__(self):
        if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == "your-openrouter-api-key-here":
            raise ValueError(
                "OpenRouter API key not set. Please add your key to the .env file.\n"
                "Get a free key at: https://openrouter.ai/keys"
            )
        self.headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://health-chatbot.local",  # Required by OpenRouter
            "X-Title": "Health Query Chatbot"
        }

    def complete(self, messages: list[dict]) -> str:
        """
        Send a list of messages to the API and return the assistant's reply.

        Args:
            messages: List of {'role': ..., 'content': ...} dicts

        Returns:
            Assistant's reply as a string
        """
        payload = {
            "model": MODEL,
            "messages": messages,
            "max_tokens": MAX_TOKENS,
            "temperature": TEMPERATURE,
        }

        try:
            response = requests.post(
                f"{API_BASE_URL}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]

        except requests.exceptions.Timeout:
            raise RuntimeError("Request timed out. Please check your internet connection.")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise RuntimeError("Invalid API key. Please check your OPENROUTER_API_KEY in .env")
            elif e.response.status_code == 429:
                raise RuntimeError("Rate limit exceeded. Please wait a moment before trying again.")
            else:
                raise RuntimeError(f"API error {e.response.status_code}: {e.response.text}")
        except (KeyError, IndexError):
            raise RuntimeError("Unexpected API response format.")
