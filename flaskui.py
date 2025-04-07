from flask import Flask, render_template, redirect, url_for
from query_llm import Query_LLM
import ragbot_local as rl
import os
import json


LLM_URL = 'http://localhost:11434/api/generate'
CHROME_DB_PATH = 'chromadb/chroma.sqlite3'


def start_app():

    global app 
    global query_llm
    global questions 

    app = Flask("LLM app")
    query_llm = Query_LLM(url=LLM_URL)
    questions = rl.read_test_questions()

    if not os.path.exists(CHROME_DB_PATH):
        docs = rl.load_dir('docs')
        print(f'Reading documents: got {len(docs)}')
    else:
        print('Chroma DB already exists, no Doc ingestion needed.')

    rl.init_chat()
    

start_app()

@app.route('/')
def home():
    return render_template("chat.html", questions=questions)


@app.route('/answer/<query>')
def answer(query):
    response = rl.llm_answer(query, -1)
    return response

app.run(debug=True)

# To run this Flask app, run this command: flask --app flaskui.py run
#   - or, add the line app.run() at the end of this file and run the command python3 flaskui.py, 