import SQLEXPRESS.connector
from SQLEXPRESS.connector import Error

def conectar_ao_banco(nome_banco):
try:
conexao = SQLEXPRESS.connect(
Trusted_Connection = yes,
database=LoginCharp
)
if conexao.is_connected():
print("Conexão estabelecida com sucesso!")
return conexao
except Error as erro:
print(f"Erro ao conectar ao banco de dados: {erro}")
return None

conexao = conectar_ao_banco(nome_banco)

if conexao:
# Execute operações no banco de dados aqui
cursor = conexao.cursor()

# Fechar a conexão após o uso
conexao.close()