from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_talisman import Talisman
import os

app = Flask(__name__)
print('SENHAAAAAAAAAAAAA: ', os.getenv('DB_PASSWORD'))
if os.getenv('ENVIRONMENT_DEV') != 'True':
    Talisman(app, content_security_policy=None)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

from route_user import *
from route_game import *
from route_db import *

if __name__ == '__main__':
    app.run(host='0.0.0.0')
