# Projeto 1 - Pipeline PySpark Para Extrair, Transformar e Carregar Arquivos JSON em Banco de Dados

# Import
# pip install sqlite3
import sqlite3

# Conecta ao banco de dados SQLite (cria se o arquivo não existir)
conexao = sqlite3.connect('../../../storage/dsa-usuarios.db')

# Cria a tabela
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS dsa_usuarios (
    uuid TEXT PRIMARY KEY,
    name TEXT,
    cpf TEXT,
    email TEXT,
    salary INTEGER,
    city TEXT,
    profession TEXT
)
""")
# Grava e fecha a conexão
conexao.commit()
conexao.close()
