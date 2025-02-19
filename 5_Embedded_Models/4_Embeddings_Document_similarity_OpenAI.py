"""
This project uses OpenAI Embedding Model for document similarity search
"""
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


Documents = [
    "Ravi Dubey is a Data Scientist working on Some Big project based out of Toronto. His Hobbies are wathcing Movies and Playing Tennis",
    "Astha is an HR professional who works in Big Firm in Toronto. Her Hobbies are Singing and relaxing",
    "Illisha Dubey is a student who studies in Grade 4. Her Hobbies are Dancing and Drawing",
    "Lika Dubey is a student who studies in Grade 1. Her Hobbies are Dancing and playing"
]

openai_embedding_models = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300,api_key=os.getenv("OPEN_API_KEY"))
"""
Below line will convert each sentence of the Documents into vector of dimensions 300
"""
doc_openai_embeddocs_vector = openai_embedding_models.embed_documents(Documents)

query1 = 'What does Illisha likes?'
query1_embeddings = openai_embedding_models.embed_query(query1)
query1_score = cosine_similarity([query1_embeddings],doc_openai_embeddocs_vector)[0]
index, similarity_score = sorted(list(enumerate(query1_score)),key=lambda x:x[1])[-1]
print(f"Question : {query1}  : Answer : {Documents[index]}")

query2 = 'Where does Astha works'
query2_embeddings = openai_embedding_models.embed_query(query2)
query2_score = cosine_similarity([query2_embeddings],doc_openai_embeddocs_vector)[0]
index, similarity_score = sorted(list(enumerate(query2_score)),key=lambda x:x[1])[-1]
print(f"Question : {query2}  : Answer : {Documents[index]}")



query3 = 'In which Grade does Lika study?'
query3_embeddings = openai_embedding_models.embed_query(query3)
query3_score = cosine_similarity([query3_embeddings],doc_openai_embeddocs_vector)[0]
index, similarity_score = sorted(list(enumerate(query3_score)),key=lambda x:x[1])[-1]
print(f"Question : {query3}  : Answer : {Documents[index]}")



