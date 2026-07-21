# 🚀 Enterprise AI Business Copilot

An Enterprise AI Business Copilot that automatically analyzes uploaded business datasets, detects their schema using LLMs, computes business insights, and generates AI-powered strategic recommendations using Retrieval-Augmented Generation (RAG).

Unlike traditional analytics dashboards that require fixed column names, this application dynamically understands different business datasets and adapts its analytics pipeline automatically.

---

## ✨ Features

- 📂 Upload any business CSV dataset
- 🤖 AI-powered schema detection using GPT-4.1 Mini
- 🧠 Structured output using Pydantic
- ✅ Automatic schema validation
- 📊 Universal business analytics engine
- 📈 Advanced KPI computation
- 💡 AI-generated executive business summaries
- 📚 Retrieval-Augmented Generation (RAG)
- ⚡ FastAPI backend
- 🔍 ChromaDB vector database
- 🧩 Modular production-ready architecture

---

# Architecture

```text
                 Upload CSV
                      │
                      ▼
            AI Schema Detection
                      │
                      ▼
             Schema Validation
                      │
                      ▼
       Universal Analytics Engine
                      │
                      ▼
            Business KPI Engine
                      │
                      ▼
             Executive Summary
                      │
                      ▼
      Retrieval-Augmented Generation
                      │
                      ▼
           GPT Business Consultant
```

---

# Tech Stack

## Backend

- FastAPI
- Python
- Pandas
- Pydantic

## AI / LLM

- OpenAI GPT-4.1 Mini
- LangChain
- LangChain OpenAI
- HuggingFace Embeddings

## Vector Database

- ChromaDB

## Machine Learning

- Sentence Transformers
- all-MiniLM-L6-v2

---

# Project Structure

```text
app/
│
├── analytics/
│   └── metrics_engine.py
│
├── api/
│
├── core/
│   ├── config.py
│   └── llm.py
│
├── llm/
│
├── rag/
│   ├── document_loader.py
│   ├── embedding_model.py
│   ├── ingest.py
│   ├── rag_chain.py
│   ├── retriever.py
│   ├── text_splitter.py
│   └── vector_store.py
│
├── schema/
│   ├── detector.py
│   ├── mapper.py
│   ├── models.py
│   ├── prompt.py
│   └── column_accessor.py
│
├── services/
│
└── main.py
```

---

# How It Works

### 1. Upload Business Dataset

The user uploads any CSV file.

↓

### 2. AI Detects Schema

GPT automatically identifies columns such as:

- Revenue
- Profit
- Customer
- Region
- Department
- Invoice Date

↓

### 3. Schema Validation

The detected schema is validated against actual dataset columns.

↓

### 4. Analytics Engine

The analytics engine computes:

- Revenue
- Profit
- Profit Margin
- Worst Performing Categories
- Discount Analysis
- Business Health Score
- Loss Consistency
- Structural Inefficiencies

↓

### 5. RAG Pipeline

Relevant business knowledge is retrieved from a vector database.

↓

### 6. AI Business Consultant

GPT combines:

- Business metrics
- Retrieved business knowledge

to generate strategic recommendations.

---

# AI Pipeline

```text
CSV
 │
 ▼
Schema Detection (GPT)
 │
 ▼
Validated Mapping
 │
 ▼
Universal Analytics Engine
 │
 ▼
Business Metrics
 │
 ▼
Retriever
 │
 ▼
Relevant Business Knowledge
 │
 ▼
GPT-4.1 Mini
 │
 ▼
Business Recommendations
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```env
OPENAI_API_KEY=your_api_key
```

Run

```bash
uvicorn app.main:app --reload
```

---

# Future Improvements

- Interactive dashboard
- Natural language business querying
- Multi-file analysis
- SQL database support
- Automatic visualization generation
- PDF executive report generation
- Agentic workflow using LangGraph

---

# Author

**Mohit Kumar**

AI Engineer | Generative AI | LLM Applications | FastAPI | LangChain
