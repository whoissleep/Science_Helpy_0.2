from langchain_huggingface import HuggingFaceEmbeddings

from config import MODEL_NAME
# model_name = "deepvk/USER-bge-m3"


def create_embeddings(model_name=MODEL_NAME):
    return HuggingFaceEmbeddings(model_name=model_name)
