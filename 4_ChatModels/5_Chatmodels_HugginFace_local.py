from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
import os


load_dotenv()
print ("Result1 with model HuggingFace")
llm = HuggingFacePipeline.from_model_id(
    model_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
    temperature = 0.5, max_new_tokens= 100
    )
)

chat_model_local_hugginface = ChatHuggingFace(llm=llm)
result_huggingface = chat_model_local_hugginface.invoke("Who is President of USA")
print(result_huggingface.content)
result_huggingface = chat_model_local_hugginface.invoke("Who is Prime Minister of Canada")
print(result_huggingface.content)