import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

load_dotenv()



# Step 1 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 2 : Load the text document
loader = TextLoader('sample_text.txt')
docs = loader.load()

# Step 3 : Extract the actual text content from the first document
text = docs[0].page_content
print("Loaded text:\n", text)

# Step 4 : Create Splitter object
splitter = SemanticChunker(
    OpenAIEmbeddings(api_key=os.getenv("OPEN_API_KEY")) , breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)
# Step 5 : Print the result

result = splitter.create_documents(text)

# Step 6: Print the result
print("\n--- Split Chunks ---")
for i, chunk in enumerate(result, 1):
    print(f"Chunk {i}:\n{chunk}\n")