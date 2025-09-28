import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, DirectoryLoader
from dotenv import load_dotenv

load_dotenv()

def load_documents(file_type: str):
    """Load documents of a specific type: 'pdf', 'txt', or 'csv'"""
    if file_type == "pdf":
        loader = DirectoryLoader(
            path="./",
            glob="**/*.pdf",
            loader_cls=PyPDFLoader
        )
    elif file_type == "txt":
        loader = DirectoryLoader(
            path="./",
            glob="**/*.txt",
            loader_cls=TextLoader
        )
    elif file_type == "csv":
        loader = DirectoryLoader(
            path="./",
            glob="**/*.csv",
            loader_cls=CSVLoader
        )
    else:
        raise ValueError("Unsupported file type. Choose from: 'pdf', 'txt', 'csv'")

    docs = loader.load()
    print(f"Loaded {len(docs)} {file_type.upper()} documents")
    return docs


def print_sample(docs, file_type: str, page_num: int = 0):
    """Print sample content. For PDFs, show a specific page."""
    if not docs:
        print(f"No {file_type.upper()} files found.")
        return

    if file_type == "pdf":
        if page_num < len(docs):
            print(f"Content from PDF page {page_num}:\n")
            print(docs[page_num].page_content[:500])  
        else:
            print(f"Page {page_num} out of range. PDF has {len(docs)} pages.")
    else:
        print(f"Content from {file_type.upper()} document:\n")
        print(docs[0].page_content[:500])  



pdf_docs = load_documents("pdf")
print_sample(pdf_docs, "pdf", page_num=2)  

txt_docs = load_documents("txt")
print_sample(txt_docs, "txt")

csv_docs = load_documents("csv")
print_sample(csv_docs, "csv")
