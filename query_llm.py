import requests


class   Query_LLM:

    TEST_QUERY = "Vytvor mi testovacích 10 otázok ohľadom BOZP. Ku každej vytvor 4 odpovede, pričom len jedna z nich bude správna. Použi Slovenčinu."

    def __init__(self, url: str) -> None:
        self.url = url

    def get_llm_response(self, query: str):
        url = 'http://localhost:11434/api/generate'

        payload = {
            "model": "jobautomation/OpenEuroLLM-Slovak:latest",
            "prompt": query,
            "stream": False
        }

        response = requests.post(url, json=payload)
        answer = response.json()["response"]
        print(answer)

        return answer

