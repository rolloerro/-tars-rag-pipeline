<div align="center">

<img src="https://raw.githubusercontent.com/rolloerro/-tars-rag-pipeline/main/assets/logo.png" alt="Digital World Medicine Logo" width="140"/>

# 🧠 TARS RAG Pipeline  
### Intelligent Medical Knowledge Engine  
**Part of the [Digital World Medicine](https://github.com/rolloerro) global initiative**

---

[![Digital World Medicine AI Project](https://img.shields.io/badge/Digital%20World%20Medicine-AI%20Project-blueviolet?style=for-the-badge&logo=github)](https://github.com/rolloerro)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Ready-orange?style=for-the-badge&logo=python)](https://python.langchain.com)
[![RAG](https://img.shields.io/badge/RAG-Search%20Pipeline-success?style=for-the-badge&logo=openai)](https://github.com/openai)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 🌍 Overview

**TARS RAG Pipeline** — это интеллектуальный движок для поиска и анализа медицинских знаний на основе Retrieval-Augmented Generation (RAG).  
Проект разработан в рамках экосистемы **Digital World Medicine (DWM)** — глобальной инициативы по внедрению искусственного интеллекта в медицину, неотложную помощь и телемедицинские системы.

---

## ⚙️ Features

✅ Индексация медицинских PDF-документов  
✅ Поиск контекста и формирование ответов через **RAG**  
✅ Встроенная API-инфраструктура на **FastAPI**  
✅ Поддержка **LangChain** и **ChromaDB**  
✅ Возможность интеграции в Telegram/Slack-боты  
✅ Архитектура, готовая для работы в медицинских системах и проектах FDT, SMP, PANIC

---

## 🧩 Tech Stack

| Компонент | Технология |
|------------|-------------|
| Backend API | FastAPI |
| AI Core | LangChain + ChromaDB |
| Embeddings | all-MiniLM-L6-v2 |
| Language | Python 3.12 |
| Deployment | Docker / Uvicorn |
| Docs | OpenAPI (Swagger UI) |

---

## 🚀 Quick Start

```bash
git clone https://github.com/rolloerro/-tars-rag-pipeline.git
cd tars_rag
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
Открой в браузере:

arduino
Копировать код
http://127.0.0.1:8000/docs
📡 API Routes
Endpoint	Method	Description
/build_index	POST	Индексирует все PDF из /data
/query	POST	Выполняет интеллектуальный поиск по базе знаний
/docs	GET	Swagger UI (тест API)

🧬 Digital World Medicine
Проект является частью глобальной AI-инициативы DWM (Digital World Medicine), включающей:

🧠 FDT — фотодинамическая терапия и онкология

🚑 SMP — медицина катастроф и скорая помощь

💭 PANIC — AI-боты для психологической поддержки

🤝 Authors
👨‍⚕️ Vladimir Kopylov — врач, инженер, разработчик AI-платформ
🤖 TARS — интеллектуальный ассистент и RAG-инженер

🪙 License
Этот проект распространяется под лицензией MIT.

<div align="center">
Digital World Medicine © 2025
"We bring intelligence into life-saving systems."



