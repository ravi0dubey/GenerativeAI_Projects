from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

chat_history = []


model_openapi= ChatOpenAI(model = "gpt-4o-mini",temperature=0, api_key=os.getenv("OPEN_API_KEY") )
while True:
    user_input = input('You : ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model_openapi.invoke(chat_history)
    chat_history.append(result.content)
    print(f"AI : {result.content}")

print("Printing complete chat history after exit")
print(chat_history)