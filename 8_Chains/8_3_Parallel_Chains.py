from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Step 1 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )


# Step 2 : Create 1st Prompt to generate Detailed report about the topic
prompt1 = PromptTemplate(
    template='Generate a summary report on {topic}',
    input_variables=['topic']
    )

# Step 3 : Create 2nd Prompt which will extract Notes from the detailed topic
prompt2 = PromptTemplate(template='Generate 5 notes from the following text {text}',input_variables=['text'])


# Step 4 : Create 3rd Prompt which will generate quiz from the detailed topic
prompt3 = PromptTemplate(template='Generate 5 short question answers quiz from the detailed text {text}',input_variables=['text'])

# Step 5 : Create 4th Prompt which will merge notes and  quiz into one document
prompt4 = PromptTemplate(template='Merge the provided notes and quiz into a single documents 5 short question answers ' \
                'from the detailed text {notes} and quiz {quiz}',
                 input_variables=['notes','quiz'])

# Step 6 Create Parser
string_parser = StrOutputParser()

# Step 7 Create Chains using below steps

#  Step 7.1 Create Parallel chain using RunnableParallel which does two task parallely
#     a. Task1 : Prompt1 is passed to the model which generates detailed output about the topic. 
#     and Detailed output is passed to string output parser which extracts 5 notes from the detailed report using prompt2
#     b. Task2 : Prompt2 is passed to the model which generates detailed output about the topic. 
#     and Detailed output is passed to string output parser which generates quiz from the detailed report using prompt3.

#  Step 7.2  Create Merge_chain which uses prompt4 to merge output of task1 and task2 into one

#  Step 7.3  Create a final chain which runs parallel_chain and merge_chain in sequence.

parallel_chain = RunnableParallel(
    {'notes': prompt1 | model_openapi | string_parser | prompt2 | model_openapi | string_parser ,
     'quiz' : prompt1 | model_openapi | string_parser | prompt3 | model_openapi | string_parser
     }
)

merge_chain = prompt4 | model_openapi | string_parser 

final_chain = parallel_chain | merge_chain


# Step 8 Invoke the chain and pass a topic 
result1 = parallel_chain.invoke({'topic' : 'soccer worldcup 2010'})
print(result1)


# Step 9 Print graph of the Parallel chain
final_chain.get_graph().print_ascii()