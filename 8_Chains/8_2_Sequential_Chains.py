from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Step 1 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )


# Step 2 : Create 1st Prompt to generate Detailed report about the topic
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
    )

# Step 3 : Create 2nd Prompt which will extract 5 pointer text from the following text
prompt2 = PromptTemplate(template='Generate 5 pointer summary from the following text {text}',input_variables=['text'])


# Step 3 Create Parser
string_parser = StrOutputParser()

# Step 4 Create a Chain which does following
# Prompt1 is passed to the model which generates detailed output about the topic. 
# Detailed output is passed to string output parser which extracts text from the detailed report.
# Detailed report is send to prompt2 which is sent to model to generate 5 pointer summary from the detailed report.
# From summary report , parser will extract the text.

chain = prompt1 | model_openapi | string_parser | prompt2 | model_openapi | string_parser

# Step 5 Invoke the chain and pass a topic 
result = chain.invoke({'topic' : 'soccer'})
print(result)