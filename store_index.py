import os
from src.helper import load_pdf, text_split, download_embedding_model
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")  

# print(PINECONE_API_KEY)
# print(PINECONE_INDEX_NAME)

# Load the extracted data
extracted_data = load_pdf("./data")

# Split the extracted text into chunks
text_chunks = text_split(extracted_data)

# Download the embedding model
embeddings = download_embedding_model()


#Initializing the Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name=PINECONE_INDEX_NAME

index = pc.Index(PINECONE_INDEX_NAME)
#Creating Embeddings for Each of The Text Chunks & storing
docsearch=PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)