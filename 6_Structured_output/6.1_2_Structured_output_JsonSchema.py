from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, Optional, Literal
import os

load_dotenv()

# Step1 : Declare Model
model_openapi= ChatOpenAI(model = "gpt-4o-mini",temperature=0, api_key=os.getenv("OPEN_API_KEY") )

# Step2 : Create Json Schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {"type": "string"},
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {"type": "string"},
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

# Step3 : Invoke Model laden with Json Schema for annotated reviews
strcutured_model = model_openapi.with_structured_output(json_schema)
result= strcutured_model.invoke(""" 
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
Reviewed by : Ravi Dubey                                 
""")



print(f"Brief Summary of Review:{result['summary']}")
print(f"Review Sentiment Type :{result['sentiment']}")
print(f"Pros Review :{result['pros']}")
print(f"Cons Review :{result['cons']}")
print(f"Reviewer Name :{result['name']}")