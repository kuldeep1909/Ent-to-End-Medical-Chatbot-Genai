from flask import Flask, render_template, request, jsonify
from src.helper import download_hugging_face_embeddings
from langchain_groq import ChatGroq
from langchain.vectorstores import Pinecone
import pinecone

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import  ChatPromptTemplate
from dotenv import load_dotenv

from src.prompt import *
import os

app = Flask(__name__)

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ['GROQ_API_KEY'] = GROQ_API_KEY

embeddings = download_hugging_face_embeddings()

#####################################################################
index_name = "medibot"

docsearch = Pinecone.from_existing_index(
    index_name=index_name,
    embedding=embeddings,
)

retriever = docsearch.as_retriever(search_type = "similarity", search_kwargs = {"k": 3})

llm = ChatGroq(
    temperature = 0,
    max_tokens = 500,
    groq_api_key = GROQ_API_KEY,
    model_name = "llama-3.3-70b-specdec"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain) 




## create two route one is deafult for user userinterface for user
@app.route('/')
def index():
    return render_template('index.html')

## second route for the chat operation for user input
@app.route('/get', methods=['GET', 'POST'])
def chat():
    msg = request.form['msg']
    input = msg
    print(input)
    response = rag_chain.invoke({"input" : msg})
    print("Response : ", response["answer"])
    return str(response["answer"])



if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=8080, debug=True)