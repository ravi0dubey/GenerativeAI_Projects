from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Step 1 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 2 : Create Prompt1 about Topic
prompt1 = PromptTemplate(
    template='Write a joke about a topic \n {topic}',
    input_variables=['topic'],
    )

# Step 3 : Create Prompt2 which will explain the job about the Topic
prompt2 = PromptTemplate(
    template='Explain the joke \n {text}',
    input_variables=['text'],
    )

# Step 4 Create String Output Parser
string_parser = StrOutputParser()

# Step 6 Create a Runnable Parallel

joke_gen_chain = RunnableSequence(prompt1,model_openapi,string_parser)

parallel_chain = RunnableParallel(
    { 'Joke': RunnablePassthrough(),
      'Explanation' : RunnableSequence(prompt2,model_openapi,string_parser)
    }
)

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

# Step 6  Run Chain
result = final_chain.invoke({'topic' : 'AI'})

print(f"Joke : {result['Joke']}")
print(f"Explanation: {result['Explanation']}")