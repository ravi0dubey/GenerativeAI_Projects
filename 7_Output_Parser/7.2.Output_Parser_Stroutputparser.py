from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm_model= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )


# Step 1 : Create 1st Prompt about  Detailed report about the topic
template1 = PromptTemplate(template='Write a detailed report on {topic}',input_variables=['topic'])

# Step 2 : Create 2nd Prompt about Summary of the detailed report
template2 = PromptTemplate(template='Write 5 lines summary of the text {text}',input_variables=['text'])

# ## Step 3: Without String Output Parser code would look like this
# ### Step 3.1: Generate Detailed report
# prompt1 = template1.invoke({'topic' : 'Yoga'})
# result1 = llm_model.invoke(prompt1)
# ### Step 3.2: Generate 5 Line summary report from the detailed report
# result2 = template2.invoke({'text':result1.content})
# result2 = llm_model.invoke(result2)

# Step 3 Create Parser
string_parser = StrOutputParser()

# Step 4 Create a Chain which does following
# Template1 which is a prompt1 is passed to the model which generates detailed output. 
# Detailed output is passed to string output parser  which extracts text from the detailed report.
# Detailed report is send to template2 to generate 2nd prompt which is sent to model to generate summary report.
# from summary report , parser will extract the text.

chain = template1 | llm_model | string_parser | template2 | llm_model | string_parser

# Step 5 Invoke the chain and pass a topic 
result = chain.invoke({'topic' : 'Yoga'})
print(result)