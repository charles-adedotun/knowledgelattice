import tempfile
import time 
import os
from utils import compute_sha1_from_file
from langchain.schema import Document
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from stats import add_usage
from typing import List

def remove_null_characters(data: str) -> str:
    return data.replace('\u0000', '')

def process_file(vector_store, file, loader_class, file_suffix, stats_db=None):
    documents = []
    file_name = file.name
    file_size = file.size
    if st.secrets.self_hosted == "false":
        if file_size > 1000000:
            st.error("File size is too large. Please upload a file smaller than 1MB or self host.")
            return

    dateshort = time.strftime("%Y%m%d")
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_suffix) as tmp_file:
        tmp_file.write(file.getvalue())
        tmp_file.flush()

        loader = loader_class(tmp_file.name)
        documents = loader.load()
        file_sha1 = compute_sha1_from_file(tmp_file.name)

    os.remove(tmp_file.name)
    
    chunk_size = st.session_state['chunk_size']
    chunk_overlap = st.session_state['chunk_overlap']

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    # Replace null characters from the document content
    documents = [Document(page_content=remove_null_characters(doc.page_content), metadata=doc.metadata) for doc in documents]

    documents = text_splitter.split_documents(documents)

    # Add the document sha1 as metadata to each document
    docs_with_metadata = [Document(page_content=doc.page_content, metadata={"file_sha1": file_sha1,"file_size":file_size ,"file_name": file_name, "chunk_size": chunk_size, "chunk_overlap": chunk_overlap, "date": dateshort}) for doc in documents]
    
    vector_store.add_documents(docs_with_metadata)
    if stats_db:
        add_usage(stats_db, "embedding", "file", metadata={"file_name": file_name,"file_type": file_suffix, "chunk_size": chunk_size, "chunk_overlap": chunk_overlap})
