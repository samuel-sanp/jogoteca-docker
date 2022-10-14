import os
from dotenv import dotenv_values

config = dotenv_values(".env")

SECRET_KEY = config['DB_SECRET_KEY']
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD=config['DB_SGBD'],
        user=config['DB_USER'],
        password=config['DB_PASSWORD'],
        server=config['DB_SERVER'],
        database=config['DB_DATABSE'],
    )
UPLOADS_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'