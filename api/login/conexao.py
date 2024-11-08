import pyodbc

   def LoginCharp (username, password):
    conn = pyodbc.connect('Driver={SQL Server};'
'Server=192.168.1.11;'
'Database=LoginCharp;'
'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('SELECT * FROM UserTeste')

    if data in usuarios:
        if usuarios[data] == password:
            return "Login bem-sucedido!"
        else:
            return "Senha incorreta!"
    else:
        return "Usuário não encontrado!"

        select from users where usuario = x and senha = x

