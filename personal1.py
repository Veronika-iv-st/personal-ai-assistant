from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# 🔐 Cargar clave API
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.2)

# ✅ IMPORTANTE: memory_key="history" para que se use correctamente en el prompt
memory = ConversationBufferMemory(memory_key="history", return_messages=True)

# 🧠 Prompt del asistente
system = SystemMessagePromptTemplate.from_template("""
You are a qualified personal assistant who manages the user's agenda.

Your task is:
- If the user asks about something already scheduled, respond with a summary.
- If the user mentions a new event, task, or appointment, assume it should be added and confirm it.

Here is your current memory of scheduled items:
{history}

Always respond politely, clearly, and without inventing information.
""")

human = HumanMessagePromptTemplate.from_template("{input}")
chat = ChatPromptTemplate.from_messages([system, human])

# 🔗 Crear cadena con memoria
chain = LLMChain(llm=llm, prompt=chat, memory=memory)

# 💬 Bucle del asistente
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "bye", "nothing"]:
        print("Assistant: Goodbye! Have a great day!")
        break

    # ✅ NO hay que pasar la memoria manualmente: la cadena ya la integra con `memory_key="history"`
    response = chain.invoke({"input": user_input})

    print("\nAssistant:", response["text"])
