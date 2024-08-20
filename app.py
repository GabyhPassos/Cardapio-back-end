import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return jsonify("homepage.html")

@app.route("/contatos")
def contatos():
    return jsonify("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return jsonify("usuarios.html", nome_usuario=nome_usuario)



if __name__ == "__main__":
    app.run(debug=True)