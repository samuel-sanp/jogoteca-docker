import os

SECRET_KEY = os.getenv('DB_SECRET_KEY')

SGBD = os.getenv('DB_SGBD')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
print('SENHAAAAAAAAAAAAA: ', password)
server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABSE')

SQLALCHEMY_DATABASE_URI = f"{SGBD}://{user}:{password}@{server}/{database}"

UPLOADS_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'