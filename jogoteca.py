from flask import Flask, render_template

app = Flask(__name__)
host = '0.0.0.0'
port = 8080


@app.route('/')
def hello():
    games = ['game 1', 'game 2', 'game 3']
    return render_template('list.html', title="Jogos", games=games)


app.run(host, port)
