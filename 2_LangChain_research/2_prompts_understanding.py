
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate,FewShotPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

# 1. Dynamic Prompt
Dynamic_prompt = PromptTemplate.from_template('Summarize {topic} in {tone} tone')
print(Dynamic_prompt.format(topic ='Tennis', tone = 'fun'))

# 2. Role-Based Prompt
role_based_prompt = ChatPromptTemplate.from_template([
    ("system", "You are a experienced {profession}"),
    ("user","Tell me about {topic}"),])
print(role_based_prompt.format_messages(profession="Doctor", topic="Viral Fever"))

# 3. Few shot Prompt
examples = [
    {"input": "What is machine learning?", "output": "Machine learning is a branch of AI that enables systems to learn from data without explicit programming."},
    {"input": "Explain neural networks.", "output": "Neural networks are computational models inspired by the human brain, consisting of layers of interconnected nodes."}
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}\n"
)

example_str = "".join([example_prompt.format(**example) for example in examples])

main_prompt = PromptTemplate(
    input_variables=["question"],
    template=f"""
    Here are some examples:\n{example_str}\nNow answer the following question:\nInput: {{question}}\nOutput:
    """
)

question = "Describe linear regression."
prompt = main_prompt.format(question=question)
print(prompt)



llm = OpenAI(api_key="your_openai_api_key")
response = llm(prompt)
print(response)