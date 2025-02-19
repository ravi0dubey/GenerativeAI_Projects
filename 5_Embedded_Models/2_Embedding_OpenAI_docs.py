"""
OpenAI Embedding Models to convert Documents into Vector
"""
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

Documents = [
    "Ottawa is capital of Canada",
    "WashingtonDC is capitcal of USA",
    "New Delhi is the capital of USA"
]
print ("Result1 with model OpenAi-text-embedding-3-large")
openai_embedding_models = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32,api_key=os.getenv("OPEN_API_KEY"))
"""
Below line will convert the Documents into vector of dimensions 32 as specified in the model
"""
result_openai_embeddocs_vector = openai_embedding_models.embed_documents(Documents)
print(str(result_openai_embeddocs_vector))
