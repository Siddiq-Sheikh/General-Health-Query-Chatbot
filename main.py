"""
Health Query Chatbot - Main Entry Point
Run: python main.py
"""

from src.chatbot import HealthChatbot


def main():
    print("=" * 60)
    print("   🏥  General Health Query Chatbot")
    print("   Powered by OpenRouter API")
    print("=" * 60)
    print("Type your health question and press Enter.")
    print("Type 'quit' or 'exit' to stop.\n")

    bot = HealthChatbot()

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit", "q"]:
                print("\nAssistant: Take care and stay healthy! Goodbye! 👋")
                break

            response = bot.chat(user_input)
            print(f"\nAssistant: {response}\n")
            print("-" * 60)

        except KeyboardInterrupt:
            print("\n\nAssistant: Goodbye! Stay healthy! 👋")
            break
        except Exception as e:
            print(f"\n[Error] Something went wrong: {e}\n")


if __name__ == "__main__":
    main()
