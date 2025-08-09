
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, FewShotPromptTemplate
from langchain_openai import ChatOpenAI
from openai import OpenAI
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path)
llm_openai = ChatOpenAI(model = "gpt-3.5-turbo",api_key=os.getenv("OPEN_API_KEY"))


# 1. Dynamic Prompt
Dynamic_prompt = PromptTemplate.from_template('Summarize {topic} in {tone} tone')

formatted_dynamic_prompt =Dynamic_prompt.format(topic ='Tennis', tone = 'fun')
result_openapi= llm_openai.invoke(formatted_dynamic_prompt)
print(result_openapi)

formatted_dynamic_prompt = Dynamic_prompt.format(topic ='Tennis', tone = 'technical')
result_openapi= llm_openai.invoke(formatted_dynamic_prompt)
print(result_openapi)

formatted_dynamic_prompt = Dynamic_prompt.format(topic ='Cricket', tone = 'serious')
result_openapi= llm_openai.invoke(formatted_dynamic_prompt)
print(result_openapi)


# 2. Role-Based Prompt
role_based_prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a experienced {profession}"),
    ("user","Tell me about {topic}"),])
formatted_role_based_prompt= role_based_prompt.format_messages(profession="Doctor", topic="Viral Fever")
result_openapi= llm_openai.invoke(formatted_role_based_prompt)
print(result_openapi)


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
result_openapi= llm_openai.invoke(prompt)
print(result_openapi)