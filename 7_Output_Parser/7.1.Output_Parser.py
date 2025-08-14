from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm_model = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm_model)

# 1st Prompt -> Detailed report about the topic

template1 = PromptTemplate(template='Write a detailed report on {topic}',input_variables=['topic'])

# 2nd Prompt -> Summary of the detailed report
template2 = PromptTemplate(template='Write 5 lines summary of the text {text}',input_variables=['text'])

prompt1 = template1.invoke({'topic' : 'Yoga'})
result1 = llm_model.invoke(prompt1)

result2 = template2.invoke({'text':result1.content})
result2 = llm_model.invoke(result2)

print(result2.content)