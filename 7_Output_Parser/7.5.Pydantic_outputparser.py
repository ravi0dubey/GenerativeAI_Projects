from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

llm_model= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 1 : Create a class from the BaseModel
class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description=' Age of the person')
    city: str = Field(description= 'City where the person belongs to')

# Step 2 Create Structured Output Parser
pydantic_parser = PydanticOutputParser(pydantic_object=Person)

# Step 3 : Create  Prompt to get details about fictional person
template = PromptTemplate(
    template='Generate the Name, age and city of a city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables= {'format_instruction' : pydantic_parser.get_format_instructions() }
    )

# Step 4 Create a Chain which does following
# Template which is a prompt is passed to the model which generates output. 
# from output, parser will extract the json variable and print it.
place = 'Italian'
chain = template | llm_model | pydantic_parser 
final_result = chain.invoke({'place': place})



print(f"Name of {place} person: {final_result.name}")
print(f"age of  {place}: {final_result.age}")
print(f"city of  {place}: {final_result.city}")