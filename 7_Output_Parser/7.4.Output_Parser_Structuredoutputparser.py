from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
import os

load_dotenv()

llm_model= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 1 : Create Schema for the output you want to receive
schema = [
    ResponseSchema(name = "fact_1", description='Fact 1 about the topic'),
    ResponseSchema(name = "fact_2", description='Fact 2 about the topic'),
    ResponseSchema(name = "fact_3", description='Fact 3 about the topic'),
    ResponseSchema(name = "fact_4", description='Fact 4 about the topic'),
]
# Step 2 Create Structured Output Parser
stroutputparser_parser = StructuredOutputParser.from_response_schemas(schema)

# Step 3 : Create  Prompt to get details about fictional person
template = PromptTemplate(
    template='Give me 4 Benefits about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables= {'format_instruction' :stroutputparser_parser.get_format_instructions() }
    )

# Step 4 Create a Chain which does following
# Template which is a prompt is passed to the model which generates output. 
# from output, parser will extract the json variable and print it.
topic = 'Yoga'
chain = template | llm_model | stroutputparser_parser 
final_result = chain.invoke({topic})

print(f"Fact1 about {topic}: {final_result['fact_1']}")
print(f"Fact2 about {topic}: {final_result['fact_2']}")
print(f"Fact3 about {topic}: {final_result['fact_3']}")
print(f"Fact4 about {topic}: {final_result['fact_4']}")
