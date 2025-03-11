from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# step 1 : create a chat template

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent expert'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')])

# step 2 : load Chat history
chat_history = []
with open('2.1.6.1.chat_history.txt') as f:
    chat_history.extend(f.readlines())
    
print(chat_history)

# # step 3 : create a prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query':'What is the status of the refund'})
print(prompt)