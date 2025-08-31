## Chains

Chains are the pipeline of Langchain

If we have a task to take input of English text which is around 1000 words and translate as well as summarize the same into Hindi text in 100 words then we have to manually create a pipeline where we have to set output of one block as input of another block and maintain it manually.

We can simplify the pipeline using Chains.


## We have 4 types of Chains
1. Simple Chains
2. Sequential Chains
3. Parallel Chains
4. Conditional Chains


### 1 Simple Chains()

It simply executes step written in below command 

chain = Prompt | model_openapi | string_parser 

On running code we get below output
![alt text](image.png)

Chain graph looks like below, it has prompt input -> which fills prompt template ->   which is used by llm model-> output of llm model is extracted by string output parser and we get the output

![alt text](image-1.png)

### 2 Sequential Chains()

It Executes tasks one after another, passing output from one step as input to the next.
Example: Creating a detailed report  → Extracting 5 pointer summary from the detailed report.

chain = prompt1 | model_openapi | string_parser | prompt2 | model_openapi | string_parser

For above command of sequential chain, below steps works.

Prompt1 is passed to the model which generates detailed output about the topic. 
Detailed output is passed to string output parser which extracts text from the detailed report.
Detailed report is send to prompt2 which is sent to model to generate 5 pointer summary from the detailed report. From summary report , parser will extract the text.


![alt text](image-2.png)


### 3 Parallel Chains()

It executes multiple tasks simultaneously, each independent of the other.
Example: Translating English text to Hindi and translating the same English text to French at the same time.

### 4 Conditional Chains()

Executes tasks based on conditions or logic defined in the process.
Example: If input text is in English, translate to Hindi; if input text is in Hindi, directly summarize it.
