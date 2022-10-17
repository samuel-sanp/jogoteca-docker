from app import app
import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash
import os


@app.route('/initdb')
def db_init():
    password = None
    with open(os.getenv('DB_PASSWORD')) as f:
        password = f.read()

    print("Conectando...")
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            # password= os.getenv('DB_PASSWORD')
            password=password
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('usuário ou senha do banco de dados inválido(s)')
            return err
            # return f"{os.getenv('DB_SGBD')} {os.getenv('DB_USER')} {password} {os.getenv('DB_SERVER')} {os.getenv('DB_DATABASE')} {os.getenv('DB_HOST')}"
            # return 'usuário ou senha do banco de dados inválido(s)'
        else:
            print(err)
            return err.msg

    cursor = conn.cursor()

    cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")

    cursor.execute("CREATE DATABASE `jogoteca`;")

    cursor.execute("USE `jogoteca`;")

    # criando tabelas
    TABLES = {}
    TABLES['Games'] = ('''
          CREATE TABLE `games` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `name` varchar(50) NOT NULL,
          `category` varchar(40) NOT NULL,
          `console` varchar(20) NOT NULL,
          PRIMARY KEY (`id`)
          ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

    TABLES['Users'] = ('''
          CREATE TABLE `users` (
          `name` varchar(20) NOT NULL,
          `username` varchar(8) NOT NULL,
          `password` varchar(100) NOT NULL,
          PRIMARY KEY (`username`)
          ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

    for tabela_nome in TABLES:
        tabela_sql = TABLES[tabela_nome]
        try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('Já existe')
            else:
                print(err.msg)
        else:
            print('OK')

    # inserindo usuarios
    usuario_sql = 'INSERT INTO users (name, username, password) VALUES (%s, %s, %s)'
    usuarios = [
        ("Samuel Constantino", "samuel", generate_password_hash("123").decode('utf-8')),
        ("Teste", "teste", generate_password_hash("123").decode('utf-8')),
    ]
    cursor.executemany(usuario_sql, usuarios)

    cursor.execute('select * from jogoteca.users')
    print(' -------------  Usuários:  -------------')
    for user in cursor.fetchall():
        print(user[1])

    # inserindo jogos
    jogos_sql = 'INSERT INTO games (name, category, console) VALUES (%s, %s, %s)'
    jogos = [
        ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
        ('Counter Strike', 'Corrida', 'PS2'),
    ]
    cursor.executemany(jogos_sql, jogos)

    cursor.execute('select * from jogoteca.games')
    print('-------------  Jogos:  -------------')
    for jogo in cursor.fetchall():
        print(jogo[1])

    # commitando se não nada tem efeito
    conn.commit()

    cursor.close()
    conn.close()

    return 'Banco de dados populado com sucesso!'