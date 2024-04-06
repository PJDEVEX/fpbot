from flask import Flask, render_template, jsonify, request
from src.helper import download_embedding_model
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone  
import os
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from dotenv import load_dotenv
from src.prompt import *

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

embeddings = download_embedding_model()

# Initialize Pinecone
#Initializing the Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name=PINECONE_INDEX_NAME

index = pc.Index(PINECONE_INDEX_NAME)

# Load the extracted data
docsearch=PineconeVectorStore.from_existing_index(index, embeddings)

# 
PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}

# Define the llm
llm=CTransformers(model="./model/llama-2-7b-chat.ggmlv3.q2_K.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.5},)

# QA chain
qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_type="mmr",search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)

# Define the route
@app.route('/')
def index():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)