import anthropic
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1000,
    temperature=0,
    system="You are a world-class poet. Respond only with short poem",
    messages=[
        {"role" : "user", 
         "content":  [
             {
                 "type" : "text",
                 "text" : "why is the ocean salty?"
             }
         ]
        }
                      
    ]
)   

print(message.content)