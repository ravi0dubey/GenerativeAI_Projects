# Embedding Models 
 Embedding models convert the text into vectors.

******We have two types of Embedding Models******
1. **Closed-Source Models**
2. **Open-Source Models** -> It can be run locally or using HugginFace Interface API

## Closed-Source Embedding Models 

### 1. OpenAI_Embedding Single query Model

#### Parameters of OpenAI for Single query

```openai_embedding_models = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)```
1. Model = text-embedding-3-large
2. dimensions= What should be the dimension of vector

```result_openai_embedquery_vector = openai_embedding_models.embed_query("Donal Trump is president of USA")```

Above code will convert the user query into vector of dimensions 32 as specified in the model
#### Code output
![image](https://github.com/user-attachments/assets/3d843624-920b-46dc-89dc-6f2898810de7)

### 2. OpenAI_Embedding Docs Model

#### Parameters of OpenAI for Documents

```openai_embedding_models = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)```
1. Model = text-embedding-3-large
2. dimensions= What should be the dimension of vector

```result_openai_embedquery_vector = openai_embedding_models.embed_query("Donal Trump is president of USA")```

Above code will convert the user query into vector of dimensions 32 as specified in the model
#### Code output
![image](https://github.com/user-attachments/assets/3d843624-920b-46dc-89dc-6f2898810de7)
