
from langchain_openai import ChatOpenAI
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model_openapi= ChatOpenAI(model = "gpt-4o-mini",temperature=0, api_key=os.getenv("OPEN_API_KEY") )

st.header('Research Tool_ Dynamic')
paper_input = st.selectbox("Select Research paper Name",["Attention is All you Need","BERT: Pre-Training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few Shot Learners", "Diffusion Models Beat GANS on Image Synthesis"])
style_input = st.selectbox("Select Explanation Style",["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length_input = st.selectbox("Select Explanation Length",["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

# loading template.json file which was created by 2.1.4_prompts_dynamic_generator.py
template = load_prompt("template.json")

if st.button('Summarize'):
    chain = template | model_openapi
    result = chain.invoke({
        'paper_input' : paper_input,
        'style_input': style_input,
        'length_input':length_input
    })
    st.write(result.content)


