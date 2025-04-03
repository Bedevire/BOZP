import requests


class   Query_LLM:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_llm_response(self, query: str):
        url = 'http://localhost:11434/api/generate'

        payload = {
            "model": "llama3.2:latest",
            "prompt": query,
            "stream": False
        }

        response = requests.post(url, json=payload)
        answer = response.json()["response"]
        print(answer)

        return answer

