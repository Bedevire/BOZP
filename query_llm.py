import requests


def get_llm_response(query: str):
    url = f'http://localhost:11434/api/generate'

    payload = {
        "model": "llama3.2:latest",
        "prompt": query,
        "stream": False
    }

    response = requests.post(url, json=payload)
    print(response.json()["response"])

get_llm_response("What is Sora?")