from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda
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

# Step 3 : Create a function to count the number of text in the Topic
def word_counter(text):
    return len(text.split())

# Step 4 Create String Output Parser
string_parser = StrOutputParser()

# Step 5 Create a Runnable Lambda
joke_gen_chain = RunnableSequence(prompt1,model_openapi,string_parser)

parallel_chain = RunnableParallel(
    { 'Joke': RunnablePassthrough(),
      'word_count' : RunnableLambda(word_counter)
    }
)

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

# Step 6  Run Chain
result = final_chain.invoke({'topic' : 'AI'})

print(f"Joke : {result['Joke']}")
print(f"Count of words: {result['word_count']}")