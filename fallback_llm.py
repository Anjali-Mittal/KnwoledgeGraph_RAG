import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
together_url=os.getenv("TOGETHER_URL")


def call_llama_fallback(prompt):
    try:
        response = requests.post(
            together_url,
            headers={
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            },
            timeout=30
        )

        if not response.ok:
            print("Llama fallback error:", response.status_code, response.text)
            return "Llama couldn't generate a response."

        return response.json()["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print("Llama fallback failed:", e)
        return "Sorry, the fallback model could not process the request."
