import os

SECRET_KEY = 'cookie_secret_key'
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='root',
        password='samuel1234',
        server='127.0.0.1',
        database='jogoteca',
    )
UPLOADS_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'