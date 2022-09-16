from flask import Flask, render_template, request, redirect, session, flash, url_for


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


user1 = User('Samuel Constantino', 'samuel', '123')
user2 = User('User One', 'user1', '123')
user3 = User('User Two', 'user2', '123')

users = {
    user1.username: user1,
    user2.username: user2,
    user3.username: user3,
}

game1 = Game('Game 1', 'Category 1', 'Console 1')
game2 = Game('Game 2', 'Category 2', 'Console 2')
game3 = Game('Game 3', 'Category 3', 'Console 3')

games = [game1, game2, game3]

app = Flask(__name__)
app.secret_key = 'cookie_secret_key'
host = '0.0.0.0'
port = 8080


@app.route('/')
def index():
    return render_template('list.html', title="Jogos", games=games)


@app.route('/new')
def new():
    if 'user_jogoteca' not in session or session['user_jogoteca'] is None:
        return redirect(url_for('login', next_page=url_for('new')))
    return render_template('new.html', title="Novo Jogo")


@app.route('/create', methods=['POST', ])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    new_game = Game(name, category, console)
    games.append(new_game)

    return redirect(url_for('index'))


@app.route('/login')
def login():
    next_page = request.args.get('next_page')
    return render_template('login.html', title='Faça seu login', next_page=next_page)


@app.route('/auth', methods=['POST', ])
def auth():
    username = request.form['username']
    password = request.form['password']
    next_page = request.form['next_page']

    if username in users:
        if password == users[username].password:
            session['user_jogoteca'] = username
            flash(users[username].name + ' logado com sucesso')
            return redirect(next_page)

    flash('logado não logado')
    return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session['user_jogoteca'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))


app.run(host, port, debug=True)
