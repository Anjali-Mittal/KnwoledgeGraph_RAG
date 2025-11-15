ISRO Knowledge Graph RAG

A lightweight, fast, and interactive Knowledge Graph–powered RAG system that lets users query structured ISRO data (missions, satellites, launch vehicles, centers, events, etc.) using natural language.
The system retrieves relevant triplets, converts queries into Cypher, executes graph lookups, and returns graph-grounded answers along with visualizations.

🔍 Features

GraphRAG pipeline combining dense embedding search + graph retrieval

ChromaDB for local vector storage

MiniLM / BGE-small embeddings

Cypher generation from natural language

Neo4j / In-memory graph simulation for subgraph extraction

Gradio Chat UI for user interaction

Graph visualization rendered on the UI

Works fully offline (optional)

Ready for HuggingFace Spaces deployment

📁 Project Structure
ISRO_KnowledgeGraph_RAG/
│── app.py                 # Main Gradio application
│── backend.py             # Retrieval + Cypher + Response pipeline
│── cypher_generator.py    # Natural language → Cypher
│── get_response.py        # Final LLM answer formatting
│── fallback_llm.py        # Backup LLM logic
│── config/                # Config files
│── data/
│   └── triplets.csv       # ISRO triplets dataset
│── embedding/
│   └── chroma_utils.py    # ChromaDB vector logic
│── ingest/
│   └── main_ingest.py     # Triplet ingestion + embedding generation
│── static/
│   └── graph.js           # Graph visualization logic
│── requirements.txt
│── README.md
└── .env (Not uploaded — use HF secrets)

🚀 How It Works

Embeddings are generated for each ISRO triplet and stored in ChromaDB.

User asks a question → embeddings retrieved → top-k relevant triplets fetched.

Model converts query into Cypher.

Graph engine executes Cypher on a Neo4j-like memory graph.

Results + visualization returned to the UI.

Example questions the system supports:

“Which ISRO missions used the PSLV launcher?”

“List satellites launched in 2018.”
