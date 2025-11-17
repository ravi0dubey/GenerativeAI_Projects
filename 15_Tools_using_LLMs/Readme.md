## Custom Tool

### Build the tools by giving it
a. Personalized function name in below case multiply_numbers_ravi
b. Decorator to define a tool so that it can be called from llm
c. Type hinting to be explicit what data type it takes as input and return as output
d. Docstring to make llm understand what the function does

a. Personalized function name — in this case `multiply_numbers_ravi`  
b. Decorator to define a tool so it can be called from the LLM  
c. Type hinting to clearly specify input and output data types  
d. Docstring to help the LLM understand what the function does  

- Personalized function name — in this case `multiply_numbers_ravi`
- Decorator to define a tool so it can be called from the LLM
- Type hinting to specify input and output types
- Docstring to explain to the LLM what the function does

a. Personalized function name — in this case `multiply_numbers_ravi`<br>
b. Decorator to define a tool so it can be called from the LLM<br>
c. Type hinting to specify input and output types<br>
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
