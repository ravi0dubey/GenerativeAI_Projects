
from langchain_openai import ChatOpenAI
import streamlit as st
import os
from dotenv import load_dotenv

# model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model_openapi= ChatOpenAI(model = "gpt-4o-mini",temperature=0, api_key=os.getenv("OPEN_API_KEY") )


st.header('Research Tool')
user_prompt= st.text_input('Enter your prompt')

if st.button('Summarize'):
    result= model_openapi.invoke(user_prompt)
    st.write(result.content)


