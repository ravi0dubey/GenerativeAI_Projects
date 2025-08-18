from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm_model= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 1 Create Parser
json_parser = JsonOutputParser()

# Step 2 : Create  Prompt to get details about fictional person
template = PromptTemplate(
    template='Give me the name,age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables= {'format_instruction' :json_parser.get_format_instructions() }
    )


# Step 3 Create a Chain which does following
# Template which is a prompt is passed to the model which generates output. 
# from output, parser will extract the json variable and print it.

chain = template | llm_model | json_parser 
final_result = chain.invoke({})

print(final_result)
print(f"name : {final_result['name']}")
print(f"age : {final_result['age']}")
print(f"city : {final_result['city']}")