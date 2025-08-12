# Chat Models

******We have two types of Chat Models******
1. **Closed-Source Models** -> It has to be run using API.
2. **Open-Source Models** -> It can be run locally or using HugginFace Interface API

![image](https://github.com/user-attachments/assets/9e4985ec-0053-4bc5-ab90-d31f51ac49f3)

**Advanatages of Using Open-Source Models compared to Closed-source Models**
```
i.  Open-source language models are freely available AI models that can be downloaded, modified, fine-tuned,
    and deployed without restrictions from a central provider. 
ii. Unlike closed-source models such as OpenAI's GPT-4, Anthropic's Claude, or Google's Gemini,
   open-source models allow full control and customization.
```
**Disadvanatages of Using Open-Source Models compared to Closed-source Models**
```
i.  To run larger open-source models, locally, It requires expensive GPUs.
ii. Requires Installation of dependencies like PyTorch, CUDA, Transformers.
iii. Most open source models does not have Reinforcement Learning, making them weaker in instruction following
iv. It does not support images, audio or video
```


## Closed-Source Models 

### 1. OpenAI_Chat Models 
#### Parameters of OpenAI

```chat_model_openapi= ChatOpenAI(model = "gpt-4",temperature=0, max_completion_tokens=10, api_key=os.getenv("OPEN_API_KEY") )```

##### 1.Temperature parameter
![image](https://github.com/user-attachments/assets/e8ead1c5-4c49-4b84-a92e-58c178741a09)

In case of lower temperature, output will remain same every time we invoke the model. While if we increase the temperature the output will keep on changing every time we invoke the model.

##### 2.max_completion_tokens
It is the count of token we get in output results. If we see result4, our answer is not even complete.

#### Code output
It seems GPT4 Chat models are trained till Oct 2024, hence it is unable to give latest output

![image](https://github.com/user-attachments/assets/bf639bb8-6c41-46e7-8d95-1203dd6acf45)

### 2. Anthropic Claude Chat Models

#### Code output
It seems Anthropic Claude models are trained till Oct 2024, hence it is unable to give latest output
![image](https://github.com/user-attachments/assets/02323657-6b36-4b20-8451-08dbd15cd67c)

### 3. Google Gemini Chat Models

#### Code output
It seems Gemini models are trained till Oct 2024, hence it is unable to give latest output

![image](https://github.com/user-attachments/assets/e2fc60f6-39c9-44a9-b049-4394745ecb8a)

## Open Source Models 

Repository of Open Source Models are in **HuggingFace**.
We can run Open Source Models either using HugginFace Interface API or downloading it locally.

### 2. TinyLlama/TinyLlama-1.1B-Chat-v1.0 Chat Model run locally

#### Code output
Running first time it takes time as its download the model from Hugginface into local system before processing our query
![image](https://github.com/user-attachments/assets/9c1ea1e7-550f-4b61-b2b4-96857ede8528)

In below snapshot we can see it downloded the model into local sytem, it also gives the source of answer and the answer
![image](https://github.com/user-attachments/assets/2e7d58aa-826a-4655-b0a4-f6893be30b79)

When i run it again, model execution is fast. If i ask additional question and run it again, still the execution is fast
![image](https://github.com/user-attachments/assets/005de44e-9ab8-4205-8677-361788d9f332)



