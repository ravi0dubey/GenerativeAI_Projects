import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

# Step 1 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 2 : Load the text document
loader = PyPDFLoader('sample_pdf.pdf')
docs = loader.load()

# Step 3 : Extract the actual text content from the first document
print("\n--- Page1 ---")
page1 = docs[0].page_content
print("Loaded text:\n", page1)

print("\n--- Page2 ---")
page2 = docs[1].page_content
print("Loaded text:\n", page2)

# Step 4 : Create Splitter object
splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator= ' '
)

# Step 5 : Split page1 document
result = splitter.split_documents(docs)

# Step 6: Print the chunks result of page1
print("\n--- Split Chunks ---")
for i, chunk in enumerate(result, 1):
    print(f"Chunk {i}:\n{chunk}\n")