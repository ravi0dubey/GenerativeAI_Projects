## Custom Tool

### Build the tools by giving it
#### a. personalized function name in below case multiply_numbers_ravi
#### b. decorator to define a tool so that it can be called from llm
#### c. type hinting to be explicit what data type it takes as input and return as output
#### d. doc string to make llm understand what the function does


This is what LLM sees when it reaches to the tool multiply_numbers_ravi

```json
{
   "description":"Multiplies two numbers.",
   "properties":{
      "a":{
         "title":"A",
         "type":"integer"
      },
      "b":{
         "title":"B",
         "type":"integer"
      }
   },
   "required":[
      "a",
      "b"
   ],
   "title":"multiply_numbers_ravi",
   "type":"object"
}
```
