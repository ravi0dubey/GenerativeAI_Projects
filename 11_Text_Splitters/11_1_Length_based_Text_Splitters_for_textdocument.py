import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI

from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

# Step 1 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 2 : Load the text document
loader = TextLoader('sample_chat.txt', encoding ='utf-8')
docs = loader.load()

# Step 3 : Extract the actual text content from the first document
text = docs[0].page_content
print("Loaded text:\n", text)

# Step 4 : Create Splitter object
splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator= ' '
)

# Step 5 : Print the result
result = splitter.split_text(text)

# Step 6: Print the result
print("\n--- Split Chunks ---")
for i, chunk in enumerate(result, 1):
    print(f"Chunk {i}:\n{chunk}\n")