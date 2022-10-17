import os

SECRET_KEY = os.getenv('DB_SECRET_KEY')

SGBD = os.getenv('DB_SGBD')
user = os.getenv('DB_USER')
server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')

password = None
with open(os.getenv('DB_PASSWORD')) as f:
    password = f.read()

SQLALCHEMY_DATABASE_URI = f"{SGBD}://{user}:{password}@{server}/{database}"

UPLOADS_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'