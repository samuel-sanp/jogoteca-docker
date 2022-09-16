from flask import Flask, render_template, request, redirect, session, flash


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


app = Flask(__name__)
app.secret_key = 'cookie_secret_key'
host = '0.0.0.0'
port = 8080

game1 = Game('Game 1', 'Category 1', 'Console 1')
game2 = Game('Game 2', 'Category 2', 'Console 2')
game3 = Game('Game 3', 'Category 3', 'Console 3')
games = [game1, game2, game3]


@app.route('/')
def index():
    return render_template('list.html', title="Jogos", games=games)


@app.route('/new')
def new():
    return render_template('new.html', title="Novo Jogo")


@app.route('/create', methods=['POST', ])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    new_game = Game(name, category, console)
    games.append(new_game)

    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html', title='Faça seu login')


@app.route('/auth', methods=['POST', ])
def auth():
    username = request.form['username']
    password = request.form['password']

    if username == 'user' and password == '123':
        session['user_jogoteca'] = username
        flash(username + ' logado com sucesso')
        return redirect('/')
    else:
        flash('logado não logado')
        return redirect('/login')

app.run(host, port, debug=True)
