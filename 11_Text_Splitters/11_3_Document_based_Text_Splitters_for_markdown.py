import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

load_dotenv()


# It is used to split documents which does not contain regular text. 
# A python program cannot be splitted using conventional split technique to maintain the sanctity of the code
# To split we will still use RecursiveCharacterTextSplitter

# Step 1 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 2 : Load the readme document
loader = TextLoader('sample_readme_for_splitting.md')

docs = loader.load()

# Step 3 : Extract the actual text content from the first document
text = docs[0].page_content
print("Loaded text:\n", text)

# Step 4 : Create Splitter object
splitter = RecursiveCharacterTextSplitter.from_language(
    language= Language.MARKDOWN,
    chunk_size = 300,
    chunk_overlap = 0,
)

# Step 5 : Print the result
result = splitter.split_text(text)

# Step 6: Print the result
print("\n--- Split Chunks ---")
for i, chunk in enumerate(result, 1):
    print(f"Chunk {i}:\n{chunk}\n")