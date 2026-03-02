"""
Health Chatbot Core Logic
Orchestrates prompts, safety filters, and API calls.
"""

from src.prompts import SYSTEM_PROMPT
from src.safety import SafetyFilter
from src.api_client import OpenRouterClient
from src.logger import ChatLogger


class HealthChatbot:
    """Main chatbot class that manages conversation state and safety."""

    def __init__(self):
        self.client = OpenRouterClient()
        self.safety = SafetyFilter()
        self.logger = ChatLogger()

        # Conversation history (supports multi-turn dialogue)
        self.history: list[dict] = []

        # System message prepended to every API call
        self.system_message = {"role": "system", "content": SYSTEM_PROMPT}

    def chat(self, user_input: str) -> str:
        """
        Process a user message and return the chatbot's response.

        Args:
            user_input: The user's health question

        Returns:
            The assistant's response string
        """
        self.logger.log_user(user_input)

        # --- Safety check on user input ---
        safety_result = self.safety.check_input(user_input)

        if safety_result["early_response"]:
            response = safety_result["early_response"]
            self.logger.log_assistant(response, safety_flag=True)
            return response

        # --- Build message history for API ---
        self.history.append({"role": "user", "content": user_input})

        messages = [self.system_message] + self.history

        # --- Call the LLM ---
        raw_response = self.client.complete(messages)

        # --- Add safety disclaimer if needed ---
        final_response = self.safety.add_disclaimer(
            raw_response,
            is_sensitive=safety_result["is_sensitive"]
        )

        # --- Update history with assistant reply ---
        self.history.append({"role": "assistant", "content": final_response})

        # Keep history from growing too large (last 10 exchanges = 20 messages)
        if len(self.history) > 20:
            self.history = self.history[-20:]

        self.logger.log_assistant(final_response)
        return final_response

    def reset(self):
        """Clear conversation history."""
        self.history = []
        self.logger.log_system("Conversation reset.")
