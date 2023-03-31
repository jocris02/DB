import sqlite3 as conector
try:
    # Abertura de conexão
    conexao = conector.connect("meu_banco.db")
    cursor = conexao.cursor()

    # execução de um comando: SELECT... CREATE...
    comando = """CREATE TABLE Pessoa(
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf));"""
    cursor.execute(comando)

    comando = """CREATE TABLE Marca(
                        id INTEGER NOT NULL,
                        nome TEXT NOT NULL,
                        sigla CHARACTER(2) NOT NULL,
                        PRIMARY KEY (id));"""
    cursor.execute(comando)

    comando = """CREATE TABLE Veiculo(
                       placa CHARACTER(7) NOT NULL,
                       ano INTEGER NOT NULL,
                       cor TEXT NOT NULL,
                       proprietario INTEGER NOT NULL,
                       marca INTEGER NOT NULL,
                       PRIMARY KEY(placa),
                       FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                       FOREIGN KEY(marca) REFERENCES Marca(id));"""
    cursor.execute(comando)



    # Efetivação do comando
    conexao.commit()
except conector.DatabaseError as err:
    print(f"Erro do banco de dados: {err}")

finally:
    # Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()

