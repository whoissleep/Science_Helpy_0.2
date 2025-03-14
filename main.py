from download_pdf import download_all_papers
from RAG import RAG_answer
from model import Model
from langchain.prompts import PromptTemplate

from config import PATH_TO_PDFS_URL

def main():
    # PATH_TO_PDFS_URL = "/home/whoissleep/Документы/VS_CODE/Scince_Helpy_0.2/papers.txt"
    download_all_papers(PATH_TO_PDFS_URL)
    model = Model()
    query = "Что такое attention?"
    rag_answer = RAG_answer(query)
    print("[INFO] RAG ANSWERED!")

    template = PromptTemplate(
        input_variables=["rag_context", "query"],
        template="""
        Контекст из научных источников:
        {rag_context}

        Вопрос: {query}

        На основе предоставленного контекста дай максимально развернутый научный ответ.
        Структура ответа:
        1. Определение
        2. Ключевые механизмы
        3. Применение
        4. Научная значимость
        """
    )
    prompt = template.invoke({
        "rag_context": rag_answer,
        "query": query
    })
    print("[INFO] Model invoke...")
    answer = model.generate(prompt=prompt)
    print(answer)

if __name__ == "__main__":
    main()

