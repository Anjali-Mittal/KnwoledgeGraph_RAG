from cypher_generator import get_cypher_query_from_llm
from embedding.chroma_utils import get_similiar_triplets
from get_response import explain_results
from dotenv import load_dotenv
from py2neo import Graph
import os

load_dotenv()
password=os.getenv("NEO4J_PASSWORD")

# Connect to Neo4j
graph = Graph("neo4j://127.0.0.1:7687", auth=("neo4j", password))


def run_cypher_on_neo4j(cypher_query):
    try:
        return graph.run(cypher_query).data()
    except Exception as e:
        return [{"error": str(e)}]

def ask_kg(question):
    matches = get_similiar_triplets(question)
    triplets_context = [text for text, _ in matches]
    cypher = get_cypher_query_from_llm(question,triplets_context)
    results = run_cypher_on_neo4j(cypher)
    explanation = explain_results(question, results)
    return cypher, explanation