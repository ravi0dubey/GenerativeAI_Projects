from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever
import os
from dotenv import load_dotenv

load_dotenv()

# Step 1 : Your Source Documents
documents = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
]

# Step 2 : Initialize the Embedding Model
embedding_model = OpenAIEmbeddings(api_key=os.getenv("OPEN_API_KEY"))

# Step 3 : Create FAISS vector store in memory
vectorstore = FAISS.from_documents(
    documents=documents,
    embedding=embedding_model,
)

# Step 4 : Convert vectorstore into a similarity retriever
similarity_retriever = vectorstore.as_retriever(
    search_type = "similarity", 
    search_kwargs={"k":5}) 

# Step 5: Create a multiquery retrievers
multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    llm=ChatOpenAI(model="gpt-3.5-turbo",api_key=os.getenv("OPEN_API_KEY"))
)

# Step 6: Define your query
query = "How to improve energy levels and maintain balance?"

# Step 7: Get the relevant response for your query using similarity results
similarity_results = similarity_retriever.invoke(query)


# Step 8: Print retrieved content
for i, doc in enumerate(similarity_results):
    print(f"Document {i+1}:")
    print(doc.page_content)
    print("\n")

# Step 9: Get the relevant response
multiquery_results= multiquery_retriever.invoke(query)

# Step 10: Print retrieved content
for i, doc in enumerate(multiquery_results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)