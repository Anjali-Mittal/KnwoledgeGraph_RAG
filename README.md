🚀 ISRO Knowledge Graph RAG

A lightweight, fast, and interactive ISRO Knowledge Explorer powered by GraphRAG, Cypher-based retrieval, and an LLM chatbot UI.
This project allows users to query structured ISRO datasets (missions, satellites, launch vehicles, centers, etc.) using natural language and get accurate, graph-grounded answers along with graph visualizations.

🔍 Overview

This project builds a retrieval-augmented chatbot that uses:

ChromaDB – Stores embeddings and metadata for triplets

MiniLM / BGE Small – Sentence embedding models

Cypher Query Generator – Converts natural language → Cypher

Neo4j / Memgraph Simulation – Local lightweight graph representation

Gradio Chat UI – Frontend for users to ask questions

Graph Visualization API – Renders subgraphs on the UI

The system allows users to explore ISRO’s knowledge graph by asking questions like:

“Show me missions launched between 2010 and 2020.”
“Which satellites are used for remote sensing?”
“What launch vehicle was used for Cartosat-2?”
“List missions related to lunar exploration.”

✨ Features
✔ Chatbot Interface

Ask questions in natural language – backend converts them into Cypher queries.

✔ Graph-based Retrieval

Your data exists as triplets:
(source, relation, target)
Each user query retrieves the most relevant subgraph.

✔ Clean Graph Visualization

A Python JS library returns a JSON graph → rendered in Gradio.

✔ Offline-Friendly

Does not depend on cloud databases. Completely local if desired.

✔ Ready for HuggingFace Spaces Deployment

Supports:

requirements.txt

app.py

.env through HF Secrets

GPU / CPU modes

🗂 Project Structure
ISRO_KnowledgeGraph_RAG/
│── app.py                 # Main Gradio app
│── graph_utils.py         # Cypher generator + graph parsing
│── rag_engine.py          # Retrieval and LLM pipeline
│── data/
│   └── triplets.csv       # ISRO triplets dataset
│── embeddings/
│   └── embeddings_chroma/ # ChromaDB vector store
│── models/
│   └── bge-small          # Saved embedding model (optional)
│── static/
│   └── graph.js           # Visualization logic
│── requirements.txt
│── README.md
└── .env                   # (Only local, NEVER uploaded)
