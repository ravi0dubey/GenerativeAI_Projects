# Langchain Tools

## 1. Built-In Tools
## 2. Custom Tool 
These are custom build tools, built by us

### Build the tools by giving it

a. Personalized function name — in this case `multiply_numbers_ravi`  
b. Decorator to define a tool so it can be called from the LLM  
c. Type hinting to clearly specify input and output data types  
d. Docstring to help the LLM understand what the function does  

```python
@tool  
def multiply_numbers_ravi(a: int, b: int) -> int: 
    """Multiplies two numbers.""" 
    return a * b  
```

 LLM sees below schema when it reaches to the tool multiply_numbers_ravi.

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

## 3. Structured Tools

It is a special type of tool where the input to the tool follows a structured schema, typically defined using a Pydantic model.
