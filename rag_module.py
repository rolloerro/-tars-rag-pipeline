import os
import chromadb
from chromadb.config import Settings
from pypdf import PdfReader
from openai import OpenAI

# === Настройки ===
DATA_DIR = "data"
CHROMA_PATH = "./chroma_data"
COLLECTION_NAME = "medical_docs"

# === Инициализация Chroma ===
client = chromadb.PersistentClient(path=CHROMA_PATH, settings=Settings(allow_reset=True))
collection = client.get_or_create_collection(name=COLLECTION_NAME)

# === Модель OpenAI ===
client_openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(pdf_path):
    """Извлечение текста из PDF."""
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def build_index():
    """Индексация всех PDF из /data."""
    existing = collection.get()
    if existing and "ids" in existing and existing["ids"]:
        collection.delete(ids=existing["ids"])

    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".pdf"):
            path = os.path.join(DATA_DIR, filename)
            text = extract_text_from_pdf(path)
            chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
            for i, chunk in enumerate(chunks):
                collection.add(
                    ids=[f"{filename}_{i}"],
                    documents=[chunk],
                    metadatas=[{"source": filename}]
                )

    return {"status": "ok", "message": "PDF файлы успешно проиндексированы."}

def search_query(query, n_results=3):
    """Поиск по индексу с кратким ответом модели."""
    results = collection.query(query_texts=[query], n_results=n_results)
    docs = [doc for doc_list in results['documents'] for doc in doc_list]
    context = "\n\n".join(docs)

    prompt = f"Ответь на медицинский запрос кратко, используя контекст:\n\n{context}\n\nЗапрос: {query}"

    completion = client_openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = completion.choices[0].message.content.strip()
    return {"query": query, "answer": answer, "docs_used": len(docs)}
