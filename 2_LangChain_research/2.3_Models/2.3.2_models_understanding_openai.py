from openai import OpenAI
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
client = OpenAI(api_key=os.getenv("OPEN_API_KEY")) 
completions= client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role" : "system", "content": "You are a helpful assistant."},
        {"role" : "user", "content": "Write a haiku about recursion in programming"},   
    ]
)   

print(completions.choices[0].message)