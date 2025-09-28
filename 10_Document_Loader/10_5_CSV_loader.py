import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, DirectoryLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

# Step 1 : Create a model
model_openapi= ChatOpenAI(model = "gpt-4",temperature=0,  api_key=os.getenv("OPEN_API_KEY") )

# Step 2 Create String Output Parser
string_parser = StrOutputParser()


# Step 3 : Create 1st Prompt to ask the question about shares
prompt1 = PromptTemplate(
    template=
    """You are a tax analyst. Here is the list of share transactions: {shares}
Task:
1. Group transactions by stock symbol.
2. Calculate the **total capital gain (sum of Profit column)** for each stock.
3. Explain briefly (2–3 lines) why the capital gain/loss may have occurred (e.g., market conditions, sector performance).
4. At the end, also provide the **overall total capital gain across all stocks**.

Format:
- Stock: <Symbol> — Profit: <value>
  Explanation: <short reasoning>
- TOTAL CAPITAL GAIN: <value>
""",
    input_variables=['shares']
    )
# Step 3 : Create 2nd Prompt which will extract 5 pointer text from the following text
prompt2 = PromptTemplate(template="""Refine the following analysis into a clear bullet-point report:{analysis}""",input_variables=['analysis'])

# Step 4 : Create  Chain to ask question 
chain = prompt1 | model_openapi | string_parser | RunnableLambda(lambda x: {"analysis": x})| prompt2 | model_openapi | string_parser


loader = TextLoader('Zerodha_TAX Statement.csv')
docs = loader.load()
# print(docs[0].page_content)


# Step 5  Run  chain 
result1 = chain.invoke({'shares' : docs[0].page_content})
print(result1)