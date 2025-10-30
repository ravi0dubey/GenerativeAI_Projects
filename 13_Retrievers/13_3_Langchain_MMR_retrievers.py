from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import os
from dotenv import load_dotenv

load_dotenv()

# Step 1 : Your Source Documents
documents = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representation of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

# Step 2 : Initialize the Embedding Model
embedding_model = OpenAIEmbeddings(api_key=os.getenv("OPEN_API_KEY"))

# Step 3 : Create FAISS vector store in memory
vectorstore = FAISS.from_documents(
    documents=documents,
    embedding=embedding_model,
)

# Step 4 : Convert vectorstore into a retriever
retriever = vectorstore.as_retriever(
    search_type = "mmr", # <- This enables MMR 
    search_kwargs={"k":3, "lambda_mult": 1}) # k= top results, lambda_mult = relevance-diversity balance

# Step 5: Define your query
query = "Give me details about Embeddings?"

# Step 6: Get the relevant response
results = retriever.invoke(query)

# Step 7: Print retrieved content
for i, doc in enumerate(results):
    print(f"Document {i+1}:")
    print(doc.page_content)
    print("\n")