import os
import requests
from dotenv import load_dotenv
from fallback_llm import call_llama_fallback


load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
api_url = os.getenv("OPENROUTER_API_URL")
MODEL = "mistralai/mistral-7b-instruct:free"

SYSTEM_PROMPT = """
You are an expert Cypher query generator for a Neo4j graph containing ISRO-related data.

The user's query is semantically matched to top relevant triplets using a vector database. You are provided these triplets.
Each triplet is in the form:
"subject predicate object"
e.g., "Chandrayaan-1 launched_by PSLV"
Your task is to:
1. Parse each triplet into (subject) -[predicate]-> (object).
2. Generate Cypher queries that reflect the relationships and node types implied by the triplets.
3. Use the relationship name exactly as provided in the triplet (case-sensitive).
4. Use node labels like `Mission`, `Vehicle`, `Satellite`, etc. only if obvious, otherwise just match on `name`.
Only return a valid Cypher query. Do not add explanations.
User Question: {user_question}
Top Retrieved Triplets:
{triplets}
Cypher:
"""

def get_cypher_query_from_llm(user_question, triplets):
    triplet_block = "\n".join(triplets)
    prompt = SYSTEM_PROMPT.format(
        user_question=user_question,
        triplets=triplet_block
    )
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_question}
        ]
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        if not response.ok:
            raise Exception(f"Primary model error: {response.status_code} {response.text}")
        return response.json()["choices"][0]["message"]["content"].strip()
    
    except Exception as e:
        print("Falling back to TinyLlama due to:", e)
        result = call_llama_fallback(prompt)
        return result


