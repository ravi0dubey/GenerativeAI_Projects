from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Step 1 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 2 : Create Prompt2 which will generate tweet about the Topic
promptX = PromptTemplate(
    template='Generate tweet about topic  \n {topic}',
    input_variables=['topic'],
    )

# Step 3 : Create Prompt2 which will write post about the Topic
promptL = PromptTemplate(
    template='Generate LinkedIn post about the topic \n {topic}',
    input_variables=['topic'],
    )


# Step 5 Create String Output Parser
string_parser = StrOutputParser()

# Step 5 Create a Runnable Parallel

parallel_chain = RunnableParallel(
    { 'tweet': RunnableSequence(promptX,model_openapi,string_parser),
      'LinkedIn' : RunnableSequence(promptL,model_openapi,string_parser)
    }
)

# Step 6  Run Chain
result = parallel_chain.invoke({'topic' : 'AI'})

print(f"X post : {result['tweet']}")
print(f"Linkedin Post: {result['LinkedIn']}")