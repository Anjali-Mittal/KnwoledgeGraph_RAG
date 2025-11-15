import os
import requests
from dotenv import load_dotenv
from fallback_llm import call_llama_fallback

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
api_url = os.getenv("OPENROUTER_API_URL")
MODEL = "mistralai/mistral-7b-instruct:free"

def explain_results(question, results):
    prompt = f"Question: {question}\nResults: {results}\nExplain this in a crisp professional sentence.Respond in the same language as the user's question. If you can't respond in English"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        if not response.ok:
            raise Exception(f"OpenRouter failed: {response.status_code}")
        return response.json()["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print("Falling back to Llama due to:", e)
        result = call_llama_fallback(prompt)
        return result


