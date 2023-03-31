import sqlite3 as conector
from  modelo_atividade import Municipio, Dengue
conexao = None
cursor = None

try:
    conexao = conector.connect("meu_banco2.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    with open("DENGUE.ods") as arquivo:
        arquivo.readline()  # Descarta o cabeçalho
        for linha in arquivo:
            codigo, nome, casos_2018, casos_2019 = linha.strip().split(';')
            print(codigo, nome, casos_2018, casos_2019)

            municipio = Municipio(codigo, nome)
            camando = '''INSERT INTO Municipio VALUES (:codigo, :nome);'''
            cursor.execute(camando, vars(municipio))

            dengue_2018 = Dengue(codigo, 2018, int(casos_2018))
            dengue_2019 = Dengue(codigo, 2019, int(casos_2019))
            comando = '''INSERT INTO Dengue VALUES (:codigo, :ano :casos);'''
            cursor.execute(comando, vars(dengue_2018))
            cursor.execute(comando, vars(dengue_2019))


except conector.DatabaseError as erro:
    cursor = conexao.cursor()
    print(f"Erro de banco de dados: {erro}")

finally:
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
