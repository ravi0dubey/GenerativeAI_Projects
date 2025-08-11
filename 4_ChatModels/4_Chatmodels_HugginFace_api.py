from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os


load_dotenv()
print ("Result1 with model HuggingFace")
llm = HuggingFaceEndpoint(repo_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",task="text-generation")

chat_model_hugginface = ChatHuggingFace(llm=llm)
result_huggingface = chat_model_hugginface.invoke("Who is Captain of Indian test cricket team")
print(result_huggingface.content)