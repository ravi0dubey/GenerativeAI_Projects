from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Step 1 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 2 : Create Prompt about Topic
prompt = PromptTemplate(
    template='Write a joke about a topic \n {topic}',
    input_variables=['topic'],
    )

# Step 3 Create String Output Parser
string_parser = StrOutputParser()

# Step 4 Create a Runnable sequence
chain = RunnableSequence(prompt,model_openapi,string_parser)

# Step 13  Run Chain
result1 = chain.invoke({'topic' : 'pizza'})
print(result1)