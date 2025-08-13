from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# below code will not work 
# chat_template = ChatPromptTemplate([
#   SystemMessage(content='You are a helpful {domain} expert'),
#   HumanMessage(content= 'Explain in simple terms, what is {topic}')
# ])

# so we have to give it as tuple instead of above format.

chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in simple terms, what is {topic}')])


model_openapi= ChatOpenAI(model = "gpt-4o-mini",temperature=0, api_key=os.getenv("OPEN_API_KEY") )

prompt = chat_template.invoke({'domain':'football','topic':'offside'})
print(prompt)