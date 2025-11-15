# 🚀 ISRO Knowledge Graph RAG

ISRO Knowledge Graph RAG is an interactive system that allows users to explore ISRO missions, satellites, launch vehicles, and centers using natural language queries.
It uses GraphRAG, Cypher-based retrieval, and semantic search to generate accurate, graph-grounded answers — along with graph visualizations.

## Features

🧠 Retrieval-Augmented Generation over structured ISRO knowledge
🔍 Semantic Search using ChromaDB instead of keyword matching
🕸️ Graph-based reasoning using Cypher queries (via Neo4j)
⚡ Fast responses by retrieving only relevant triplets / subgraphs
💬 Clean Gradio chatbot UI for interacting with the graph
🔌 Fully local — no external APIs or cloud databases required

### 🛠️ Setup Instructions
### 1. Clone the repository

```bash
git clone https://github.com/Anjali-Mittal/KnwoledgeGraph_RAG.git
cd KnwoledgeGraph_RAG
```

### 2. Install dependencies

Use a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

### 3. Add environment variables

Create a .env (DO NOT upload this to GitHub):

NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
OPENROUTER_API_KEY=your_key


For HuggingFace deployment, add these to HF Spaces → Settings → Secrets.

### 4. Start the local Neo4j database

Make sure Neo4j Desktop or Memgraph Light is running.

### 5. Run the app
```python app.py```
The Gradio UI will open — ask any ISRO-related question.

## 📂 Directory Structure
```
ISRO_KnowledgeGraph_RAG/
├── app.py                       # Main Gradio application
├── backend.py                   # Retrieval + LLM logic
├── cypher_generator.py          # Natural language → Cypher conversion
├── fallback_llm.py              # Fallback logic when no context is found
├── get_response.py              # Final answer generation
├── data/
│   └── triplets.csv             # ISRO Knowledge Graph dataset
├── embedding/
│   ├── chroma_utils.py          # ChromaDB operations
│   └── models/                  # (Optional) stored embedding models
├── ingest/
│   └── main_ingest.py           # Ingestion pipeline for embeddings
├── config/
│   └── settings.py              # Central config
├── static/
│   └── graph.js                 # Visualization logic
├── .env                         # Not stored in repo
├── requirements.txt
└── README.md
```

## 🛰️ Example Queries
### Users can ask things like:

“What missions did ISRO launch in 2019?”
“Show me the relationship between PSLV and Chandrayaan.”
“Which centers handle satellite integration?”
“Explain the structure of ISRO launch vehicles.”

## 🤝 Contributing
#### Pull requests are welcome — especially improvements to:

Dataset coverage
Graph consistency
Model performance
UI/UX
