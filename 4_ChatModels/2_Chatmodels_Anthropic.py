from langchain_anthropic import ChatAnthropic
import os
print ("Result1 with model claude-3-5-sonnet-20241022")
model_anthropic = ChatAnthropic(model="claude-3-5-sonnet-20241022", max_tokens=1000, temperature=0,api_key=os.getenv("ANTHROPIC_API_KEY"))
result_anthropic = model_anthropic.invoke("Who is President of USA")
print(result_anthropic)

print("****")
print ("Result1 with only content with model claude-3-5-sonnet-20241022")
print(result_anthropic.content)

print("****")
print ("Result1 with model claude-3-5-haiku-20241022")
model_anthropic = ChatAnthropic(model="claude-3-5-haiku-20241022", max_tokens=1000, temperature=0,api_key=os.getenv("ANTHROPIC_API_KEY"))
result_anthropic = model_anthropic.invoke("Who is President of USA")
print(result_anthropic.content)
