from flask import Flask, render_template, request
from scrapping import search_winner

app = Flask('Sorteio Instagram')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sorteio', methods=['POST'])
def sorteio():
    url = request.form['url']
    winner = search_winner(url)
    return render_template('result.html', winner=winner)

app.run()