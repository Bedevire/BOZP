from flask import Flask
from query_llm import Query_LLM

app = Flask("LLM app")
query_llm = Query_LLM(url='http://localhost:11434/api/generate')

@app.route('/')
def hello():
    return "Hello vole"


@app.route('/answer/<query>')
def answer(query):
    response = query_llm.get_llm_response(query)
    return f'Your query is {query}, answer is {response}'