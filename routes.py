from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app, db
from models import Games, Users


@app.route('/')
def index():
    games = Games.query.order_by(Games.id)
    return render_template('list.html', title="Jogos", games=games)


@app.route('/login')
def login():
    next_page = request.args.get('next_page')
    return render_template('login.html', title='Faça seu login', next_page=next_page)


@app.route('/auth', methods=['POST', ])
def auth():
    username = request.form['username']
    password = request.form['password']
    next_page = request.form['next_page']

    user = Users.query.filter_by(username=username).first()

    if user:
        if password == user.password:
            session['user_jogoteca'] = username
            flash(user.name + ' logado com sucesso')
            return redirect(next_page)

    flash('login incorreto')
    return redirect(url_for('login'))


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

    game = Games.query.filter_by(name=name).first()

    if game:
        flash('Jogo já existente!')
        return redirect(url_for('index'))

    new_game = Games(name=name, category=category, console=console)
    db.session.add(new_game)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/edit/<int:id>')
def edit(id):
    if 'user_jogoteca' not in session or session['user_jogoteca'] is None:
        return redirect(url_for('login', next_page=url_for('edit', id=id)))

    game = Games.query.filter_by(id=id).first()
    return render_template('edit.html', title="Editar Jogo", game=game)


@app.route('/update', methods=['POST', ])
def update():
    id = request.form['id']
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    game = Games.query.filter_by(id=id).first()

    game.name = name
    game.category = category
    game.console = console

    db.session.add(game)
    db.session.commit()

    return redirect(url_for('index'))




@app.route('/logout')
def logout():
    session['user_jogoteca'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))
