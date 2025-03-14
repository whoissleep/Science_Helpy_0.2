from langchain_huggingface import HuggingFaceEmbeddings

model_name = "deepvk/USER-bge-m3"

def create_embeddings(model_name=model_name):
    return HuggingFaceEmbeddings(model_name=model_name)