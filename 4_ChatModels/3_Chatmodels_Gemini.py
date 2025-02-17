from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
print ("Result1 with model gemini-1.5-pro")
chat_model_gemini = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
result_gemini = chat_model_gemini.invoke("Who is President of USA")
print(result_gemini.content)
