from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda,RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
import os

load_dotenv()

# Step 1 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 2 Create String Output Parser
string_parser = StrOutputParser()

# Step 3 : Create a class from the BaseModel for the Sentiment analysis
class Sentiment(BaseModel):
    Sentiment : Literal['Positive','Negative'] = Field(description='Sentiment of the feedback')
    
# Step 4 Create Pydantic Output Parser
pydantic_parser = PydanticOutputParser(pydantic_object=Sentiment)

# Step 5 : Create 1st Prompt to classify the feedback sentiment into Positive or Negative
prompt1 = PromptTemplate(
    template='Classify the Sentiment of following feedback {feedback} into positive or Negative sentiment' \
    'about product from the users  \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables= {'format_instruction' : pydantic_parser.get_format_instructions() }
    )

# Step 6 : Create Classifier Chain to classify feedback sentiment as Positive or Negative
classifier_chain  = RunnableSequence(prompt1,model_openapi,pydantic_parser)

# Step 7 : Create 2nd prompt to generate response for Positive feedback
prompt2 = PromptTemplate(
    template='Write an appropriate response to this Positive feedback \n {feedback}',
    input_variables=['feedback'],
    )

# Step 8 : Create 3rd prompt to generate response for Negative feedback
prompt3 = PromptTemplate(
    template='Write an appropriate response to this Negative feedback \n {feedback}',
    input_variables=['feedback'],
    )

# Step 9  Create chain for Positive sentiment
positive_sentiment  = RunnableSequence(prompt2,model_openapi,string_parser)

# Step 10  Create chain for Negative sentiment
negative_sentiment  = RunnableSequence(prompt3,model_openapi,string_parser)

# Step 11  Create Branch chain to perform task for Positive or Negative sentiment accordingly
branch_chain = RunnableBranch(
    (lambda x:x.Sentiment == 'Positive', positive_sentiment),
    (lambda x:x.Sentiment == 'Negative', negative_sentiment),
    RunnableLambda(lambda x: " Could not find the sentiment from the given Feedback")
)

final_chain = RunnableSequence(classifier_chain,branch_chain)

# Step 6  Run Chain
result = final_chain.invoke({'feedback' : 'Product is kinda so so'})

print(result)
# print(f"Joke : {result['Joke']}")
# print(f"Count of words: {result['word_count']}")