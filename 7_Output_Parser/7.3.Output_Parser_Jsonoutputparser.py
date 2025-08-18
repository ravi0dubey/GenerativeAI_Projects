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
prompt = template.format()

# Step 3 Invoke the llm model and pass prompt in it
result = llm_model.invoke(prompt)

# Step 4 Parse the outout in json format and print it
final_result = json_parser.parse(result.content)
print(final_result)
print(f"name : {final_result['name']}")
print(f"age : {final_result['age']}")
print(f"city : {final_result['city']}")