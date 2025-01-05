# we need to execute this for the first time 

# we wanna add some more information then we can add it here by using this code

from src.helper import load_pdf_data, text_split, download_hugging_face_embeddings
import pinecone
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Pinecone
from pinecone.grpc import PineconeGRPC as Pinecone 
from pinecone import ServerlessSpec


load_dotenv()
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

extractred_data = load_pdf_data(data="Data/")
text_chunk = text_split(extractred_data)
embeddings = download_hugging_face_embeddings()

## We have to intialise the pinceone with the python code
pc = Pinecone(api_key=PINECONE_API_KEY)
# Create a serverless index
index_name = "medibot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws', 
            region='us-east-1'
        ) 
    ) 

# adding the chunks/data
docsearch = Pinecone.from_documents(
    documents=text_chunk,
    index_name=index_name,
    embedding=embeddings,
)

