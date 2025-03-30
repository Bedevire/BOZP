from flask import Flask, render_template, redirect, url_for
from query_llm import Query_LLM


LLM_URL = 'http://localhost:11434/api/generate'

app = Flask("LLM app")
query_llm = Query_LLM(url=LLM_URL)

print('Running the flask app flaskui')

@app.route('/')
def home():
    #return render_template('index.html')
    return render_template("chat.html")



@app.route('/answer/<query>')
def answer(query):
    response = query_llm.get_llm_response(query)
    return response

# http://127.0.0.1:5000/static/js/main.js

app.run(debug=True) 
# To run this Flask app, run this command: flask --app flaskui.py run
#   - or, add the line app.run() at the end of this file and run the command python3 flaskui.py, 