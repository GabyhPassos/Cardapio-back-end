import SQLEXPRESS

def consultar_banco(query, parametros=()):
    try:
        # Conectar ao banco de dados
        conexao = SQLEXPRESS.connect('LoginCharp')
        cursor = conexao.cursor()

        # Executar a consulta
        cursor.execute(query, parametros)

        # Obter os resultados
        resultado = cursor.fetchall()

        # Fechar a conexão
        cursor.close()
        conexao.close()

        return resultado

    except SQLEXPRESS.Error as erro:
        print(f"Erro ao consultar o banco de dados: {erro}")
        return None

# Exemplo de uma consulta
consulta = "SELECT * FROM Users WHERE Telefone > ?"
parametros = (18,)
resultados = consultar_banco(consulta, parametros)

for linha in resultados:
    print(linha)