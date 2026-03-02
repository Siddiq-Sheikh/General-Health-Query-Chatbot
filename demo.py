"""
Demo Script — Runs example health queries without live API calls.
Shows safety filtering behavior on various input types.
Run: python demo.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.safety import SafetyFilter


def run_demo():
    sf = SafetyFilter()

    demo_queries = [
        # General health questions
        ("What causes a sore throat?", "general"),
        ("Is paracetamol safe for children?", "general"),
        ("How much water should I drink per day?", "general"),
        ("What are the symptoms of the common cold?", "general"),

        # Sensitive topics
        ("What are early signs of depression?", "sensitive"),
        ("How does diabetes affect the body?", "sensitive"),

        # Out-of-scope
        ("What disease do I have based on my symptoms?", "out_of_scope"),
        ("Diagnose me please", "out_of_scope"),

        # Emergencies
        ("I have severe chest pain and can't breathe", "emergency"),
        ("I think I overdosed on medication", "emergency"),
    ]

    print("=" * 65)
    print("   Health Chatbot — Safety Filter Demo")
    print("=" * 65)
    print(f"{'Query':<50} {'Safety Result'}")
    print("-" * 65)

    for query, expected in demo_queries:
        result = sf.check_input(query)

        if result["is_emergency"]:
            tag = "🚨 EMERGENCY → redirect to emergency services"
        elif result["is_out_of_scope"]:
            tag = "🚫 OUT-OF-SCOPE → politely decline"
        elif result["is_sensitive"]:
            tag = "⚠️  SENSITIVE → answer + disclaimer"
        else:
            tag = "✅ SAFE → answer normally"

        print(f"  {query[:48]:<48} {tag}")

    print("\n" + "=" * 65)
    print("Example of an emergency response:")
    print("-" * 65)
    emergency_result = sf.check_input("I have severe chest pain")
    print(emergency_result["early_response"])

    print("\n" + "=" * 65)
    print("To run the full chatbot with live AI responses:")
    print("  1. Copy .env.example to .env")
    print("  2. Add your OpenRouter API key")
    print("  3. Run: python main.py")
    print("=" * 65)


if __name__ == "__main__":
    run_demo()
