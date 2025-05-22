from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain 
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.2)

memory = ConversationBufferMemory(return_messages=True)

system = SystemMessagePromptTemplate.from_template("""
You are a personal assistant that manages the user's agenda.

Here is your current memory of scheduled events:
{memory.buffer}

The user just said:
"{input}"

If this message refers to something that is already scheduled, summarize the related information.
If it's a new task, appointment, or event, assume it should be added to the agenda. Confirm it has been noted.

Always reply politely and clearly.
""")

human = HumanMessagePromptTemplate.from_template("{input}")
chat = ChatPromptTemplate.from_messages([system, human])

chain = LLMChain(llm=llm, prompt=chat, memory=memory)

while True:
    user_input = input("you: ")
    if user_input.lower() in ["nothing", "exit", "bye"]:
          print("See you next time!")
          break

response = chain.invoke({"input": user_input})
print("\n Assistent:", response['text'])