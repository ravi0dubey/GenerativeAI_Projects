## Runnables

Runnables are a flexible, composable, and standardized way to build chains, replacing the older Chain class.

It is divided into two parts
1. **Task specific Runnables** -> These are LanChain Core Components which are used to perform specific task like LLM calls, prompting etc.
Examples
a. ChatOpenAI -> Runs an LLM Model.
b. PromptTemplate -> Formats prompts dynamically.
c. Retriever -> Retrieves relevant documents.

2. **Runnable primitives** -> 

## We have 4 types of Runnables
1. RunnableSequence
2. RunnableParallel


### 1 RunnableSequence()

It is a sequential chain of runnable which simply executes step in a sequence, passing the output of one step as input to the next. Generally used when we need to compose multiple runnables together in a structured flow.

![alt text](image-4.png)

chain = RunnableSequence(prompt1,model_openapi,string_parser,prompt2,model_openapi,string_parser)

On running code we get below output

![alt text](image-3.png)




### 2 RunnableParallel
It is a runnable Primitive that allows multiple runnables to execute in parallel. Each runnable receives the same input and process it independently and in parallel sequence, producing a dictionary of outputs.

parallel_chain = RunnableParallel({
 'tweet': RunnableSequence(promptX,model_openapi,string_parser), 
'LinkedIn' : RunnableSequence(promptL,model_openapi,string_parser)})

On running code we get below output
![alt text](image-5.png)