"""
HuggingFace Embedding Models to convert each sentence of the Documents into 384 Dimensional Vector
"""
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

Documents = [
    "Ottawa is capital of Canada",
    "WashingtonDC is capital of USA",
    "New Delhi is the capital of India"
]
print ("Result1 with model Hugginface-all-MiniLM-L6-v2")
hugginface_embedding_models = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

"""
Below line will convert the each sentence of the Documents into vector of dimensions 384 
"""
result_hugginface_embeddocs_vector = hugginface_embedding_models.embed_documents(Documents)
print(str(result_hugginface_embeddocs_vector))
