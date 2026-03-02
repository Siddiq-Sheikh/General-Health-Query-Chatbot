"""
Chat Logger Module
Logs conversations to a file for review and debugging.
"""

import os
import logging
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create a timestamped log file per session
log_filename = os.path.join(LOG_DIR, f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_filename, encoding="utf-8"),
    ]
)

logger = logging.getLogger("health_chatbot")


class ChatLogger:
    """Simple wrapper for logging chat events."""

    def log_user(self, message: str):
        logger.info(f"USER: {message}")

    def log_assistant(self, message: str, safety_flag: bool = False):
        flag = " [SAFETY TRIGGERED]" if safety_flag else ""
        logger.info(f"ASSISTANT{flag}: {message}")

    def log_system(self, message: str):
        logger.info(f"SYSTEM: {message}")
