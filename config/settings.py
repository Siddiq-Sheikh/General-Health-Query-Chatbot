"""
Configuration Settings
Loads environment variables and defines app-wide constants.
"""

import os
from dotenv import load_dotenv

load_dotenv()  # Reads from .env file in project root

# --- API Configuration ---
OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "your-openrouter-api-key-here")
API_BASE_URL: str = "https://openrouter.ai/api/v1"

# --- Model Selection ---
# Free models on OpenRouter (as of 2025):
#   "mistralai/mistral-7b-instruct:free"
#   "meta-llama/llama-3-8b-instruct:free"
#   "google/gemma-7b-it:free"
MODEL: str = os.getenv("MODEL", "mistralai/mistral-7b-instruct:free")

# --- Generation Parameters ---
MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "512"))
TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))
