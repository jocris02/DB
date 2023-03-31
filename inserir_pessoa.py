import sqlite3 as conector
from modelo import Pessoa

conexao = conector.connect("meu_banco.db")
cursor = conexao.cursor()

# Criação do objeto do tipo pessoa
pessoa = Pessoa(1850000032, 'Gohan', '1991-05-30', True)

# Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa VALUES(:cpf, :nome, :data_nascimento, :usa_oculos);'''

cursor.execute(comando, vars(pessoa))
print(vars(pessoa))

conexao.commit()

cursor.close()
conexao.close()