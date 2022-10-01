#CRIANDO A BASE DE DADOS
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS alfred_db character set UTF8mb4 collate utf8mb4_bin")

#RODANDO COMANDO PARA CRIAR TABELAS
import mysql.connector
cnx = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='alfred_db'
)

cursor = cnx.cursor()

def executeScriptsFromFile(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except IOError as msg:
            print(msg)

executeScriptsFromFile('scripts/sql/create_db_and_tables.sql')
cnx.commit()

#COMANDO PARA POPULAR TABELAS
def populate_tables(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except IOError as msg:
            print(msg)

populate_tables('scripts/sql/insert_tables.sql')
cnx.commit()