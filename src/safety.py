"""
Safety Filter Module
Checks user inputs and model outputs for safety concerns.
"""

import re
from src.prompts import EMERGENCY_KEYWORDS, EMERGENCY_RESPONSE, SAFETY_DISCLAIMER


class SafetyFilter:
    """Handles safety checks for both user inputs and model responses."""

    # Topics that need extra care — chatbot should educate but strongly defer to doctors
    SENSITIVE_TOPICS = [
        "cancer", "hiv", "aids", "diabetes", "pregnancy", "abortion",
        "mental health", "depression", "anxiety", "addiction", "drug abuse",
        "eating disorder", "self-harm"
    ]

    # Queries that are clearly out of scope
    OUT_OF_SCOPE_PATTERNS = [
        r"\bprescribe\b", r"\bdiagnose me\b", r"\bam i (sick|dying|ill)\b",
        r"\bwhat (disease|illness|condition) do i have\b"
    ]

    def check_input(self, user_input: str) -> dict:
        """
        Analyze user input for safety concerns.

        Returns:
            dict with keys:
                - 'is_emergency' (bool)
                - 'is_sensitive' (bool)
                - 'is_out_of_scope' (bool)
                - 'early_response' (str | None) — if set, return this directly without calling API
        """
        lower_input = user_input.lower()

        # Check for emergency keywords
        if any(kw in lower_input for kw in EMERGENCY_KEYWORDS):
            return {
                "is_emergency": True,
                "is_sensitive": False,
                "is_out_of_scope": False,
                "early_response": EMERGENCY_RESPONSE
            }

        # Check for out-of-scope patterns
        for pattern in self.OUT_OF_SCOPE_PATTERNS:
            if re.search(pattern, lower_input):
                return {
                    "is_emergency": False,
                    "is_sensitive": False,
                    "is_out_of_scope": True,
                    "early_response": (
                        "I'm not able to diagnose conditions or prescribe treatments. "
                        "I can share general health information, but for personal medical concerns, "
                        "please consult a licensed healthcare professional who can properly evaluate you."
                    )
                }

        # Check for sensitive topics
        is_sensitive = any(topic in lower_input for topic in self.SENSITIVE_TOPICS)

        return {
            "is_emergency": False,
            "is_sensitive": is_sensitive,
            "is_out_of_scope": False,
            "early_response": None
        }

    def add_disclaimer(self, response: str, always: bool = False, is_sensitive: bool = False) -> str:
        """Append a medical disclaimer to the response when appropriate."""
        if always or is_sensitive:
            return response + SAFETY_DISCLAIMER
        # Add disclaimer if response mentions medications, treatments, or symptoms
        trigger_words = ["medication", "medicine", "treatment", "symptom", "dose", "drug", "pill"]
        if any(word in response.lower() for word in trigger_words):
            return response + SAFETY_DISCLAIMER
        return response
