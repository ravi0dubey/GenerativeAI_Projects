import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Step 1 : Create a prompt

Prompt= PromptTemplate(
    template = 'Generate 5 interestic facts about the {topic}',
    input_variables=['topic']
)

# Step 2 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 3 Create Parser
string_parser = StrOutputParser()

# Step 4 Create a Chain which does following
# Template1 which is a prompt1 is passed to the model which generates detailed output. 
# Detailed output is passed to string output parser  which extracts text from the detailed report.
# Detailed report is send to template2 to generate 2nd prompt which is sent to model to generate summary report.
# from summary report , parser will extract the text.

chain = Prompt | model_openapi | string_parser 

# Step 5 Invoke the chain and pass a topic 
result = chain.invoke({'topic' : 'Yoga'})
print(result)
