
import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

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
classifier_chain = prompt1 | model_openapi | pydantic_parser


# loader = TextLoader('WhatsApp_Chat.txt', encoding ='utf-8')
loader = TextLoader('chat1.txt', encoding ='utf-8')
docs = loader.load()


# Step 13  Run conditional chain 
result1 = classifier_chain.invoke({'feedback' : docs[0].page_content})
print(result1)




