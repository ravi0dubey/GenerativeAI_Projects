from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")

llm_openai = OpenAI(model = "gpt-3.5-turbo-instruct",api_key=os.getenv("OPEN_API_KEY"))
result_opeanapi= llm_openai.invoke("Who is Prime Minister of Canada")
print(result_opeanapi)

