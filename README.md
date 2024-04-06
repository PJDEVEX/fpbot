# fpbot

# medical-bot

## How to set up the project

- Clone the repo
```bash
Project repo: 
```
- Activate virtual environment
```bash
conda activate env
```
- Install project dependencies
```bash
pip3 install -r requirements.txt
```

- .env
```bash
import os

PINECONE_API_KEY=xxxxxxxxxxxxxxxxxxxxxx
PINECONE_INDEX_NAME=xxx-xxxxxxxxxxxxxxx
PINECONE_ENV=xxxxxxxxxxxxxxxxxxxxxxxxxx

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
EMBEDDING_MODEL_NAME=xxxxxxxxxxxxxxxxxx

```



- Chat Model

The chat model used is [llama-2-7b-chat.ggmlv3.q4_0.bin](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin) that can be downloaded from [here...](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_0.bin?download=true)

- Embedding Model
  - The embedding model used is [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). 
  - Please copy ```bash sentence-transformers/all-MiniLM-L6-v2``` and past in .env file.
  - It uses 384 dimensions.


## Project Architect

<details>
  <summary>Click here...</summary>
  <img src="https://res.cloudinary.com/pjdevex/image/upload/v1711904175/project_architecture_wowaqd.webp" alt="Project Architect">
</details>

### Tech Stack

<details>
<summary>Click here...</summary>

|#|Component|Dependancy/Library|version|Badge|Purpose|Ref|
|---|:---|:---|:---|:---|:---|:---|
|1|Programming Language| Python|3.8|![Python](https://img.shields.io/badge/Python-3.x-blue.svg)|Interpriter|[Python](https://www.python.org/)|
|2|Generative AI Framework(s)|LangChain|0.0.225|[![langchain](https://img.shields.io/badge/langchain-0.0.225-orange)](https://pypi.org/project/langchain/0.0.225/)|Framework for building the application with LLMs through composability|[Langchain](https://python.langchain.com/docs/get_started/introduction)
|3|"|LLamaIndex||[![LLama Index](https://img.shields.io/badge/LLama_Index-G.%20Framework-<COLOR>.svg)](https://your-link-url)|data framework for building LLM applications|[lamaIndex](https://www.llamaindex.ai/)
|4| Frontend-webapp|Flask|3.0.2|[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green)](https://flask.palletsprojects.com/)|||
|5|LLM|Meta Llama2||[![Meta LLama2](https://img.shields.io/badge/Meta_LLama2-LLM-blueviolet)](https://example.com)||[Meta Llama2](https://llama.meta.com/llama2/)|
|6|VectorDB|Pinecone|3.2.2|[![Pinecone Client](https://img.shields.io/badge/Pinecone_Client-orange?style=for-the-badge&logo=python)](https://pypi.org/project/pinecone-client/)|VectorDB|[Pinecone](https://python.langchain.com/docs/integrations/vectorstores/pinecone)|
|7|Transformer|ctransformers|0.2.5|[![ctransformers](https://img.shields.io/badge/ctransformers-v0.2.5-orange)](https://pypi.org/project/ctransformers/0.2.5/)|Python bindings for the Transformer models implemented in C/C++ using GGML library.|[C Transformers](https://python.langchain.com/docs/integrations/llms/ctransformers)|
|8|Embedding tool|sentence-transformers|2.2.2|[![sentence-transformers](https://img.shields.io/pypi/v/sentence-transformers.svg?color=orange)](https://pypi.org/project/sentence-transformers/)| Multilingual Sentence, Paragraph, and Image Embeddings using BERT & Co.|[Sentence Transformers on Hugging Face](https://python.langchain.com/docs/integrations/text_embedding/sentence_transformers)|

</details>



### 