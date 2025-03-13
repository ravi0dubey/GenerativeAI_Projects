from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated
import os

load_dotenv()

# Step1 : Declare Model
model_openapi= ChatOpenAI(model = "gpt-4o-mini",temperature=0, api_key=os.getenv("OPEN_API_KEY") )

# Step2 : Create Typedict Class
class Review(TypedDict):
    summary: str
    sentiment: str
    brief_summary: Annotated[str,"A Brief summary of the review"]
    type_sentiment: Annotated[str,"Return sentiment of the review either, negative, positive or neutral"]



# Step3 : Invoke Model laden with  TypeDict class
strcutured_model = model_openapi.with_structured_output(Review)
result= strcutured_model.invoke("""Paying over 12k and getting a product with scratches how it will feel? The same feeling I had...it had scratches all over the product ....just ban this kind of sellers..and people please buy from a showroom so that you can check and buy...I bought this even after all the negative comments.
the frame and lens is fine just because the seller had no responsibility of the customers money iam returning this....worst experience I have ever had.
""")


print(f"Summary of Review:{result['summary']}")
print(f"Sentiment of Review :{result['sentiment']}")
print(f"Brief Summary of Review:{result['brief_summary']}")
print(f"Review Sentiment Type :{result['type_sentiment']}")