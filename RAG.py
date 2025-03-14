from database import prepare_RAG_system

def RAG_answer(query):
    PATH_TO_PDFS = "/home/whoissleep/Документы/VS_CODE/Scince_Helpy_0.2/pdfs"
    vectorestorage = prepare_RAG_system(PATH_TO_PDFS)
    retriever = vectorestorage.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 1}
    )

    rel_docs = retriever.invoke(query)
    clear_list_of_docs = []
    for doc in rel_docs:
        print(doc.page_content)
        clear_list_of_docs.append(doc.page_content) 

    return clear_list_of_docs