
import os
from langchain_community.document_loaders import AmazonTextractPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

# To install scanned pdf images etc we use AmazonTextractPDFLoader
# multipage document needs to be in S3 instead of  loading it from folder
# pip install amazon-textract-caller -> do it before running the cdode for AmazonTextractPDFLoader to install amazon-textract-caller-0.2.4 amazon-textract-response-parser-1.0.3
# pip install amazon-textract-textractor


load_dotenv()

# # Step 1 : Create a model
# model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# # Step 2 Create String Output Parser
# string_parser = StrOutputParser()

# # Step 3 : Create a class from the BaseModel for the Sentiment analysis
# class Sentiment(BaseModel):
#     Sentiment : Literal['Positive','Negative'] = Field(description='Sentiment of the feedback')
    
# # Step 4 Create Pydantic Output Parser
# pydantic_parser = PydanticOutputParser(pydantic_object=Sentiment)

# # Step 5 : Create 1st Prompt to classify the feedback sentiment into Positive or Negative
# prompt1 = PromptTemplate(
#     template='Classify the Sentiment of following feedback {feedback} into positive or Negative sentiment' \
#     'about product from the users  \n {format_instruction}',
#     input_variables=['feedback'],
#     partial_variables= {'format_instruction' : pydantic_parser.get_format_instructions() }
#     )

# # Step 6 : Create Classifier Chain to classify feedback sentiment as Positive or Negative
# classifier_chain = prompt1 | model_openapi | pydantic_parser


loader = AmazonTextractPDFLoader('8_Blood Report_24th_July_2025_Detailed.pdf')
docs = loader.load()
print(docs[0].page_content)





