🏥 Health Query Chatbot

A safe and responsible AI-powered health information chatbot built using the OpenRouter API, enhanced with prompt engineering, safety filtering, and structured project architecture.

The chatbot provides general health education while actively preventing unsafe medical advice, diagnoses, or emergency misinformation.

✨ Key Features

🤖 LLM-powered conversational health assistant

🛡️ Multi-layer safety filtering system

🧠 Prompt-engineered medical guardrails

📜 Automatic conversation logging

🧪 Unit-tested safety module

⚡ Support for multiple free OpenRouter models

🔒 Environment-based API configuration

📂 Project Structure
health_chatbot/
│
├── main.py                  # Application entry point
├── demo.py                  # Offline demo (no API required)
├── requirements.txt
├── .env.example             # Environment configuration template
├── .gitignore
│
├── config/
│   └── settings.py          # Model configuration & API settings
│
├── src/
│   ├── prompts.py           # System prompts & safety instructions
│   ├── safety.py            # Input/output safety validation
│   ├── api_client.py        # OpenRouter API interface
│   ├── chatbot.py           # Core chatbot controller
│   └── logger.py            # Session logging system
│
├── tests/
│   └── test_safety.py       # Safety filter unit tests
│
└── logs/                    # Auto-generated chat session logs
🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/health-query-chatbot.git
cd health-query-chatbot
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Configure Environment Variables

Create a .env file:

cp .env.example .env

Add your OpenRouter API Key:

OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxx
MODEL=mistralai/mistral-7b-instruct:free

Get a free API key here:
👉 https://openrouter.ai/keys

4️⃣ Run the Chatbot
python main.py
5️⃣ Run Demo Mode (No API Needed)

Useful for testing safety filters locally.

python demo.py
6️⃣ Run Tests

Using pytest:

python -m pytest tests/ -v

Or directly:

python tests/test_safety.py
🤖 Supported Free Models (OpenRouter)
Model	Identifier
Mistral 7B (Default)	mistralai/mistral-7b-instruct:free
LLaMA 3 8B	meta-llama/llama-3-8b-instruct:free
Gemma 7B	google/gemma-7b-it:free

You can switch models anytime inside the .env file.

🛡️ Safety Architecture

The chatbot follows a defensive AI design approach to reduce harmful outputs.

Safety Layer	Purpose
Emergency Detection	Identifies crisis-related queries and redirects users
Medical Advice Blocking	Prevents diagnosis or prescription generation
Sensitive Topic Handling	Adds contextual safety disclaimers
Prompt Guardrails	Ensures safe and non-diagnostic responses
Output Validation	Filters unsafe model responses
Conversation Logging	Maintains session transparency
💬 Example Queries

Users can ask educational health questions such as:

What causes a sore throat?

How does the immune system work?

What are common flu symptoms?

Is paracetamol generally used for fever?

How much sleep do adults typically need?

🧪 Engineering Concepts Demonstrated

Prompt Engineering

AI Safety & Guardrails

API Abstraction Design

Modular Python Architecture

Environment Configuration

Unit Testing

Logging Systems

⚠️ Medical Disclaimer

This chatbot provides general health information only and is intended for educational use.

It does not provide medical diagnosis, treatment, or professional healthcare advice.
Always consult a licensed healthcare professional for medical concerns.

📜 License

This project is developed for educational and research purposes.

✅ This version is portfolio-ready, recruiter-friendly, and suitable for showcasing AI engineering skills on GitHub.

If you want, I can also upgrade it to top 5% GitHub README style with:

badges

architecture diagram

demo screenshots

contribution section

AI system flow diagram.