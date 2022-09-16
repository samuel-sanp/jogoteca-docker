from flask import Flask, render_template


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


app = Flask(__name__)
host = '0.0.0.0'
port = 8080


@app.route('/')
def home():
    game1 = Game('Game 1', 'Category 1', 'Console 1')
    game2 = Game('Game 2', 'Category 2', 'Console 2')
    game3 = Game('Game 3', 'Category 3', 'Console 3')
    games = [game1, game2, game3]
    return render_template('list.html', title="Jogos", games=games)


@app.route('/new')
def new():
    return render_template('new.html', title="Novo Jogo")


app.run(host, port)
