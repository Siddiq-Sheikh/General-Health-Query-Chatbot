"""
Tests for the Safety Filter Module
Run: python -m pytest tests/ -v
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.safety import SafetyFilter


class TestSafetyFilter:
    def setup_method(self):
        self.sf = SafetyFilter()

    # --- Emergency Detection ---
    def test_detects_chest_pain(self):
        result = self.sf.check_input("I have severe chest pain right now")
        assert result["is_emergency"] is True
        assert result["early_response"] is not None

    def test_detects_overdose(self):
        result = self.sf.check_input("I think I took an overdose")
        assert result["is_emergency"] is True

    def test_normal_query_not_emergency(self):
        result = self.sf.check_input("What causes a sore throat?")
        assert result["is_emergency"] is False

    # --- Sensitive Topic Detection ---
    def test_detects_mental_health(self):
        result = self.sf.check_input("Tell me about depression symptoms")
        assert result["is_sensitive"] is True

    def test_detects_cancer(self):
        result = self.sf.check_input("What are early signs of cancer?")
        assert result["is_sensitive"] is True

    def test_normal_query_not_sensitive(self):
        result = self.sf.check_input("How do I treat a minor cut?")
        assert result["is_sensitive"] is False

    # --- Out-of-Scope Detection ---
    def test_detects_diagnosis_request(self):
        result = self.sf.check_input("What disease do I have?")
        assert result["is_out_of_scope"] is True
        assert result["early_response"] is not None

    # --- Disclaimer Tests ---
    def test_disclaimer_added_for_sensitive(self):
        response = "Here is some information about anxiety."
        result = self.sf.add_disclaimer(response, is_sensitive=True)
        assert "Disclaimer" in result

    def test_disclaimer_added_for_medication_mention(self):
        response = "You can take this medication twice a day."
        result = self.sf.add_disclaimer(response)
        assert "Disclaimer" in result

    def test_no_disclaimer_for_plain_response(self):
        response = "Drinking water is important for staying hydrated."
        result = self.sf.add_disclaimer(response)
        assert result == response


if __name__ == "__main__":
    # Simple manual test runner
    sf = SafetyFilter()
    test_queries = [
        "What causes a sore throat?",
        "Is paracetamol safe for children?",
        "I have chest pain right now",
        "Do I have cancer?",
        "How does the immune system work?",
    ]

    print("Safety Filter Test Results")
    print("=" * 50)
    for query in test_queries:
        result = sf.check_input(query)
        flags = []
        if result["is_emergency"]: flags.append("🚨 EMERGENCY")
        if result["is_sensitive"]: flags.append("⚠️  SENSITIVE")
        if result["is_out_of_scope"]: flags.append("🚫 OUT-OF-SCOPE")
        if not flags: flags.append("✅ OK")
        print(f"Query: {query[:45]:<45} | {', '.join(flags)}")
