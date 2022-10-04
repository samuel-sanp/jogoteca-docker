from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app
from models import Users
from helpers import LoginForm
from flask_bcrypt import check_password_hash


@app.route('/login')
def login():
    next_page = request.args.get('next_page')
    form = LoginForm()
    return render_template('login.html', title='Faça seu login', next_page=next_page, form=form)


@app.route('/auth', methods=['POST', ])
def auth():
    form = LoginForm(request.form)
    username = form.nickname.data
    password = form.password.data
    next_page = request.form['next_page']

    user = Users.query.filter_by(username=username).first()

    is_auth = check_password_hash(user.password, password)

    if user and is_auth:
        session['user_jogoteca'] = username
        flash(user.name + ' logado com sucesso')

        if next_page == 'None':
            return redirect('/')

        return redirect(next_page)


    flash('login incorreto')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['user_jogoteca'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))