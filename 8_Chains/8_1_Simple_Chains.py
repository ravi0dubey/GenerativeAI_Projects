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
parser = StrOutputParser()

# Step 4 Create a Chain which does following
# Prompt is passed to the model which generates output. 
# Detailed output is passed to string output parser  which extracts text from the report.

chain = Prompt | model_openapi | parser 

# Step 5 Invoke the chain and pass a topic 
result = chain.invoke({'topic' : 'Yoga'})
print(result)


# Step 5 Invoke the chain and pass a topic 
chain.get_graph().print_ascii()

