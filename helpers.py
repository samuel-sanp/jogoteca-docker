import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, PasswordField


class GameForm(FlaskForm):
    name = StringField('Nome', [validators.DataRequired(), validators.Length(min=1, max=50)])
    category = StringField('Categoria', [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=20)])
    submit = SubmitField('Salvar')


class LoginForm(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    password = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    submit = SubmitField('Entrar')


def get_image(id):
    for image_name in os.listdir(app.config['UPLOADS_PATH']):
        if f'capa-{id}' in image_name:
            return image_name

    return 'capa_padrao.jpg'


def remove_image(id):
    image = get_image(id)

    if image != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOADS_PATH'], image))
