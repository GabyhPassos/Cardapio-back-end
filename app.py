from flask import Flask, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return ({
        json("homepage.html"),
    })

@app.route("/contatos")
def contatos():
    return ({ 
        json("contatos.html"),
    })

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return ({
        json("usuarios.html", nome_usuario=nome_usuario),
    })



if __name__ == "__main__":
    app.run(debug=True)