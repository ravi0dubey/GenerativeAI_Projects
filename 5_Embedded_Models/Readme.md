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

```
Documents = [
    "Ottawa is capital of Canada",
    "WashingtonDC is capitcal of USA",
    "New Delhi is the capital of USA"
]
openai_embedding_models = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32,api_key=os.getenv("OPEN_API_KEY"))
result_openai_embeddocs_vector = openai_embedding_models.embed_documents(Documents)
```

Above code will convert the Documents text into vector of dimensions 32 as specified in the model

#### Code output
![image](https://github.com/user-attachments/assets/1c5ae04d-4d3d-4e33-92a2-650271587973)



## Open Source Embedding Models
Repository of Open Source Embedding Models are in HuggingFace. We can run Open Source Models either using HugginFace Interface API or downloading it locally
### 1. all-MiniLM-L6-v2
#### Parameters of  all-MiniLM-L6-v2 for Single query
```
Documents = [
    "Ottawa is capital of Canada",
    "WashingtonDC is capitcal of USA",
    "New Delhi is the capital of USA"
]
hugginface_embedding_models = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
result_hugginface_embeddocs_vector = hugginface_embedding_models.embed_documents(Documents)
```
Above code will convert the Documents text into vector of dimensions 384 as per model default specification

#### Code output
Running first time it takes time as its download the model from Hugginface into local system before processing our query
![image](https://github.com/user-attachments/assets/9de11104-c841-4fb5-98e7-e9936de38120)

In below snapshot we can see it downloded the model into local sytem, and then it converted the documents into vectors
![image](https://github.com/user-attachments/assets/aba1ddb0-a5d0-4133-8cd0-43a9406091c0)


## Project 1: Using OpeniAI Embedding Models perform Similarity Search on Documents

We will feed documents to our **OpenAI Embedding models** of dimension 300 and then ask question from the documents
Embedding model will conver the documents into vectors of dimension **300** and store it internally.
When the question is asked it uses query embedding models to convert the query into vector and perform **cosine similarity** search
to find the text in the document similar to the query asked.

#### Code output
![image](https://github.com/user-attachments/assets/90e35f0c-890a-4beb-9027-7397938a7e65)

