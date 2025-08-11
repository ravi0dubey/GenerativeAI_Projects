from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv
load_dotenv()

print ("Result1 with model claude-3-5-sonnet-20241022")
model_anthropic = ChatAnthropic(model="claude-3-5-sonnet-20241022", max_tokens=1000, temperature=0)
result_anthropic = model_anthropic.invoke("who is indian test cricket captain")
print(result_anthropic)

print("****")
print ("Result1 with only content with model claude-3-5-sonnet-20241022")
print(result_anthropic.content)

print("****")
print ("Result1 with model claude-3-5-haiku-20241022")
model_anthropic = ChatAnthropic(model="claude-3-5-haiku-20241022", max_tokens=1000, temperature=0)
result_anthropic = model_anthropic.invoke("who is indian test cricket captain")
print(result_anthropic.content)

print("****")
print ("Result1 with model claude-opus-4-1-20250805")
model_anthropic = ChatAnthropic(model="claude-opus-4-1-20250805", max_tokens=1000, temperature=0)
result_anthropic = model_anthropic.invoke("who is indian test cricket captain")
print(result_anthropic.content)