# AI Personal Assistant with Memory

This project is a conversational **AI-powered personal assistant** built with Python. It helps users organize their schedules by intelligently managing events, tasks, and appointments using natural language.

## 🧠 What It Does

- Engages in a natural language conversation with the user.
- Maintains **contextual memory** of previous interactions.
- Detects whether the input refers to an already scheduled event or a new one.
- Confirms newly added events and provides summaries of existing ones.

## 🚀 Technologies Used

- [LangChain](https://www.langchain.com/) — for building LLM-based conversational chains.
- [OpenAI GPT](https://platform.openai.com/) — for natural language understanding and generation.
- `dotenv` — for environment variable management.
- Python 3.8+

## 📦 Requirements

Install dependencies with:

pip install -r requirements.txt
Sample requirements.txt:


langchain
openai
python-dotenv

⚙️ Setup
Create a .env file and add your OpenAI API key:


OPENAI_API_KEY=your_api_key_here
Make sure .env is listed in .gitignore to avoid pushing sensitive information.

▶️ Usage
Run the assistant with:

python main.py
Then interact via the terminal:

you: Meeting with Laura tomorrow at 10am
Assistant: Noted. I've added your meeting with Laura for tomorrow at 10am. ✔️

you: What time was the meeting with Laura?
Assistant: You have a meeting with Laura scheduled for tomorrow at 10am. 🗓️
To exit the assistant, type exit, bye, or nothing.

📁 Project Structure
personal-assistant/
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md