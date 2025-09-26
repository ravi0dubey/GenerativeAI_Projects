
from langchain_community.document_loaders import TextLoader

loader = TextLoader('WhatsApp_Chat.txt', encoding ='utf-8')
docs = loader.load()
print(docs[0])
print("Printing Page content")
print(docs[0].page_content)
print("Printing Meta Data content")
print(docs[0].metadata)


