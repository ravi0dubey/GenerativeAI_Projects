from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")

model_openapi= ChatOpenAI(model = "gpt-4o-mini",temperature=0, api_key=os.getenv("OPEN_API_KEY") )
result_opeanapi = model_openapi.invoke("Divide result by 1.5")
print(result_opeanapi.content)

model_anthropic = ChatAnthropic(model="claude-3-5-sonnet-20241022", max_tokens=1000, temperature=0,api_key=os.getenv("ANTHROPIC_API_KEY"))
result_anthropic = model_anthropic.invoke("Divide result by 1.5")
print(result_anthropic)