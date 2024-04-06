import os
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME")



def load_pdf(data):
    """
    Load PDF file(s) from a directory
    """
    loader = DirectoryLoader(data,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader,
                             show_progress=True,
                             )
    document = loader.load()

    return document

def text_split(extracted_data):
    """
    Split the extracted text into chunks
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks


def download_embedding_model():
    """
    Download the embedding model
    """
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    return embeddings