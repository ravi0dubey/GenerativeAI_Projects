from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
model_openapi= ChatOpenAI(model = "gpt-4o-mini",temperature=0, api_key=os.getenv("OPEN_API_KEY") )

# SystemMessage is the direction given to the AI 
# HumanMessage is the input prompt/text entered by users
# AIMessage is the response provided by the AI


messages = [
    SystemMessage(content='You are a helpful Assistant, give me just 1 line answer'),
    HumanMessage(content='Who is Messi')
]

result = model_openapi.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)



