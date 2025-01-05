# here we add all the utility related function

from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import sentence_transformers
from langchain.embeddings import HuggingFaceEmbeddings


## extract the data from the pdf

def load_pdf_data(data):
    loader = DirectoryLoader(data, glob="*.pdf",
                             loader_cls=PyPDFLoader)
    
    documents = loader.load()
    return documents


# perfrom the text splitting 

def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    text_chunk = text_splitter.split_documents(extracted_data)
    return text_chunk


## download the embedding model from the huggingface

def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

