from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv


model_openapi= ChatOpenAI(model = "gpt-4o-mini",temperature=0, api_key=os.getenv("OPEN_API_KEY") )
while True:
    user_input = input('You : ')
    if user_input == 'exit':
        break
    result = model_openapi.invoke(user_input)
    print(f"AI : {result.content}")
