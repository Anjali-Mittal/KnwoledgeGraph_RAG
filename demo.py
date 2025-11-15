from embedding.chroma_utils import get_similiar_triplets
from cypher_generator import get_cypher_query_from_llm
from get_response import explain_results
from backend import run_cypher_on_neo4j

# Step 1: Get relevant triplets from Chroma
question = "Which rocket was used to launnch the Chandrayaan? Why was it chosen explain in technical terms? What other satellites were launched using that same rocket and in what year and orbit?"
matches = get_similiar_triplets(question)
triplet_context = [text for text, _ in matches]

# Step 2: Generate Cypher
cypher_query = get_cypher_query_from_llm(question,triplet_context)
print("Cypher:", cypher_query)

# Step 3: Simulated Neo4j output
neo4j_result =run_cypher_on_neo4j(cypher_query)

# Step 4: Generate Explanation
answer = explain_results(question, neo4j_result)
print("Explanation:", answer)