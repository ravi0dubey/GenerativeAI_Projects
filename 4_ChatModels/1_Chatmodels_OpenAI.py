from langchain_openai import ChatOpenAI
import os

# chat_model_openapi= ChatOpenAI(model = "chatgpt-4o-latest",temperature=0, api_key=os.getenv("OPEN_API_KEY") )
chat_model_openapi= ChatOpenAI(model = "gpt-4o-2024-11-20",temperature=0, api_key=os.getenv("OPEN_API_KEY") )

result_opeanapi = chat_model_openapi.invoke("Who is President of USA")
print(result_opeanapi.content)
