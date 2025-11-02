from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
import os
from dotenv import load_dotenv

load_dotenv()

# Step 1 : Your Source Documents
documents = [
    Document(page_content=(
        """The Grand Canyon is one of the most visited natural wonders in the world.
        Photosynthesis is the process by which green plants convert sunlight into energy.
        Millions of tourists travel to see it every year. The rocks date back millions of years."""
    ), metadata={"source": "Doc1"}),

    Document(page_content=(
        """In medieval Europe, castles were built primarily for defense.
        The chlorophyll in plant cells captures sunlight during photosynthesis.
        Knights wore armor made of metal. Siege weapons were often used to breach castle walls."""
    ), metadata={"source": "Doc2"}),

    Document(page_content=(
        """Basketball was invented by Dr. James Naismith in the late 19th century.
        It was originally played with a soccer ball and peach baskets. NBA is now a global league."""
    ), metadata={"source": "Doc3"}),

    Document(page_content=(
        """The history of cinema began in the late 1800s. Silent films were the earliest form.
        Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.
        Modern filmmaking involves complex CGI and sound design."""
    ), metadata={"source": "Doc4"})
]

# Step 2 : Initialize the Embedding Model
embedding_model = OpenAIEmbeddings(api_key=os.getenv("OPEN_API_KEY"))

# Step 3 : Create FAISS vector store in memory
vectorstore = FAISS.from_documents(
    documents=documents,
    embedding=embedding_model,
)

# Step 4 : Convert vectorstore into a base retriever
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# Step 5: Setup the compressor using an LLM
llm=ChatOpenAI(model="gpt-3.5-turbo",api_key=os.getenv("OPEN_API_KEY"))
compressor = LLMChainExtractor.from_llm(llm)

# Step 6: Create the contextual compression retriever
compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

# Step 7: Define your query
query = "What is photosynthesis?"

# Step 8: Get the relevant response for your query using similarity results
similarity_results = compression_retriever.invoke(query)


# Step 9: Print retrieved content
for i, doc in enumerate(similarity_results):
    print(f"Document {i+1}:")
    print(doc.page_content)
    print("\n")

