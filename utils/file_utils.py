import os
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def save_uploaded_file(file, base_path, content_type):
    folder = Path(base_path) / content_type
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / file.name
    with open(file_path, "wb") as f:
        f.write(file.read())
    return file_path

def convert_to_txt(pdf_path):
    txt_folder = pdf_path.parent.parent / f"{pdf_path.parent.name}_txt"
    txt_folder.mkdir(parents=True, exist_ok=True)

    loader = PyMuPDFLoader(str(pdf_path))
    documents = loader.load()
    full_text = "\n".join([doc.page_content for doc in documents])

    txt_path = txt_folder / (pdf_path.stem + ".txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(full_text)

    return txt_path

def embed_txt_to_chroma(txt_path, chroma_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([text])
    embedding = OpenAIEmbeddings(disallowed_special=())
    vectorstore = Chroma.from_documents(chunks, embedding, persist_directory=chroma_path)
    vectorstore.persist()
