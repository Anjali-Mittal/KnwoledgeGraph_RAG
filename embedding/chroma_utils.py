import chromadb
from sentence_transformers import SentenceTransformer

# Constants
DATASET_NAME = "KG_Data"
CHROMA_PATH = "data/chroma"
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# Load embedding model and ChromaDB client once
model = SentenceTransformer(EMBEDDING_MODEL)
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_collection(DATASET_NAME)

def get_similiar_triplets(query: str, top_k: int = 3):
    """
    Given a query, return top_k most semantically similar triplet sentences
    from the embedded ChromaDB collection.
    """
    query_embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    matched_texts = results.get("documents", [[]])[0]
    matched_metadatas = results.get("metadatas", [[]])[0]

    return list(zip(matched_texts, matched_metadatas))

# Test locally
if __name__ == "__main__":
    query = "What is the Chandrayaan? How many missions are there?"
    matches = get_similiar_triplets(query)
    for i, (text, meta) in enumerate(matches):
        print(f"{i + 1}. {text}")
