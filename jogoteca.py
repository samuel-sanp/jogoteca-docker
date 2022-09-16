from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'cookie_secret_key'
host = '0.0.0.0'
port = 8080

app.config['SQLALCHEMY_DATAbASE_URI'] = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='root',
        password='samuel1234',
        server='127.0.0.1',
        database='jogoteca',
    )

db = SQLAlchemy(app)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Users(db.Model):
    username = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/')
def index():
    games = Games.query.order_by(Games.id)
    print(games)
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
