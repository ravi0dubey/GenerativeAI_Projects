from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import os
from dotenv import load_dotenv

load_dotenv()

# Step 1 : Your Source Documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search"),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# Step 2 : Initialize the Embedding Model
embedding_model = OpenAIEmbeddings(api_key=os.getenv("OPEN_API_KEY"))

# Step 3 : Create Chroma vector store in memory
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name= "ravi_retriever_collection"
)

# Step 4 : Convert vectorstore into a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k":2})

# Step 5: Define your query
query = "Give me details about Embeddings?"

# Step 6: Get the relevant response
results = retriever.invoke(query)

# Step 7: Print retrieved content
for i, doc in enumerate(results):
    print(f"Document {i+1}:")
    print(doc.page_content)
    print("\n")