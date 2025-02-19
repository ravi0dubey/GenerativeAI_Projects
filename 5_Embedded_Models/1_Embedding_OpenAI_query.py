from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
print ("Result1 with model OpenAi-text-embedding-3-large")
openai_embedding_models = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
"""
Below line will convert the query into vector of dimensions 32 as specified in the model
"""
result_openai_embedquery_vector = openai_embedding_models.embed_query("Donal Trump is president of USA")
print(str(result_openai_embedquery_vector))
