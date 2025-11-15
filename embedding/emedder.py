import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

dataset_name="KG_Data"
def format_triplet(subject, predicate, obj):
    return f"{subject} {predicate} {obj}"

def embed_and_store(triplet_csv_path, source_name, persist_directory="data/chroma"):
    # Load triplets
    df = pd.read_csv(triplet_csv_path)

    # Format triplets into natural language sentences
    sentences = [
        format_triplet(row['subject'], row['predicate'], row['object']) 
        for _, row in df.iterrows()
    ]

    # Create unique IDs
    ids = [f"{source_name}_{i}" for i in range(len(sentences))]

    # Load embedding model
    model = SentenceTransformer("BAAI/bge-small-en-v1.5")
    embeddings = model.encode(sentences).tolist()

    # Initialize ChromaDB client
    client = chromadb.PersistentClient(path=persist_directory)
    collection = client.get_or_create_collection(dataset_name)

    # Add to ChromaDB
    collection.add(
        documents=sentences,
        ids=ids,
        metadatas=[{"dataset": dataset_name, "source": source_name} for _ in ids],
        embeddings=embeddings
    )
    print(f"Stored {len(sentences)} triplets from '{source_name}' in collection '{dataset_name}'.")

if __name__ == "__main__":
    embed_and_store("data/triplets/isro_archives_triplets.csv",source_name="ISRO_Archives")
