from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'chave-secreta-super-segura'  # Usado para gerenciar sessões de usuário de maneira segura.

# Simulação de banco de dados de usuários
users = {
    'usuario1': 'senha123',
    'usuario2': 'minhasenha'
}

@app.route('/')
def home():
    if 'username' in session:
        return f'Olá, {session["username"]}! Você está logado. <a href="/logout">Logout</a>'
    return 'Você não está logado. <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['Telephone']
        password = request.form['password']

        # Verificando se o usuário existe e a senha está correta
        if username in users and users[username] == password:
            session['username'] = username  # Armazenando o nome do usuário na sessão
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove o usuário da sessão
    flash('Você saiu da sua conta!', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)