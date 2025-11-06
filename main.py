from fastapi import FastAPI
from rag_module import build_index, search_query

app = FastAPI(title="TARS RAG", version="0.1.0")

@app.post("/build_index")
async def build_index_endpoint():
    """Создание индекса PDF файлов"""
    return build_index()

@app.get("/search")
async def search_endpoint(q: str):
    """Поиск по PDF"""
    return search_query(q)
