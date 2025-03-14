from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

PATH_TO_PDFS = "/home/whoissleep/Документы/VS_CODE/Scince_Helpy_0.2/pdfs"

class PDFChunker:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def load_pdfs(self, path_to_pdfs):
        docs = []

        for file in os.listdir(path_to_pdfs):
            if file.endswith(".pdf"):
                filepath = os.path.join(path_to_pdfs, file)
                pdf_loader = PyMuPDFLoader(filepath)

                pdf_documents = pdf_loader.load()
                docs.extend(pdf_documents)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                " ",
                ".",
                ""
            ]
        )
        split_docs = text_splitter.split_documents(docs)
        return split_docs