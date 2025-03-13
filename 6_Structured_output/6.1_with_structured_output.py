from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
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

class Review_upgrade(TypedDict):
    key_themes : Annotated[list[str],"Write down all the key themes discussed in the review in a list"]
    brief_summary: Annotated[str,"A Brief summary of the review"]
    type_sentiment: Annotated[str,"Return sentiment of the review either, negative, positive or neutral"]
    pros : Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons : Annotated[Optional[list[str]],"Write down all the cons inside a list"]


# Step3.1 : Invoke Model laden with  TypeDict class
strcutured_model1 = model_openapi.with_structured_output(Review)
result1= strcutured_model1.invoke("""Paying over 12k and getting a product with scratches how it will feel? The same feeling I had...it had scratches all over the product ....just ban this kind of sellers..and people please buy from a showroom so that you can check and buy...I bought this even after all the negative comments.
the frame and lens is fine just because the seller had no responsibility of the customers money iam returning this....worst experience I have ever had.
""")

# Step3.2 : Invoke Model laden with  TypeDict class
strcutured_model2 = model_openapi.with_structured_output(Review_upgrade)
result2= strcutured_model2.invoke(""" 
First I would like to rate this phone in the following basics after 1 month of use
1) Battery life- 6000mah is a pretty huge and good performance battery.... Butvu have to take care of it if u want the same backup for the coming years... Don't on the battery saver when it's 55% or above... It can damage ur battery backup...
2) Display- It has a huge screen(6.5 inche Fhd+)with 90hz refresh rate(u can change it in the display setting)
Color are great
3) Camera- It comes with quard camera(50mp main, 8mp ultra wide, 2mp depth sensor and 2mp macro lens.). Quality of pics are awesome👍.... 50 Mp camera is the best to take any pics.
Front camera is 8mp and give best pics(use snapchat filters for best results😆).
3) Performance or processor- It comes with mediatek helio g88 12 nm chipset. It gives u a high performance for gaming and multimedia surfing. BGMI graphic can be set up to HD in High fps😊.
4) -design- it's great buy the Bifrost option.
5) speakers- have dual speakers.. Best sound

Pros- camera is great
Performance is okay
Design is cool
Display is good
Battery is huge
Comes with a 22.5w charger and supports 18 w quick charging

Cons- heating problem 🔥🔥🔥🔥
Sometimes hang for 5min

At last I will say in this range it's a pretty good offer...... And if u van get any offer u can go for real me narzo 50
For example I will put some pics taken from the phone

""")

print(f"Summary of Review:{result1['summary']}")
print(f"Sentiment of Review :{result1['sentiment']}")
print(f"Brief Summary of Review:{result1['brief_summary']}")
print(f"Review Sentiment Type :{result1['type_sentiment']}")


print(" *** output 2 ***")

print(f"Brief Summary of Review:{result2}")
print(f"Brief Summary of Review:{result2['brief_summary']}")
print(f"Review Sentiment Type :{result2['type_sentiment']}")
print(f"Pros Review :{result2['pros']}")
print(f"Cons Review :{result2['cons']}")