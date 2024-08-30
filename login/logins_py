import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from flask import Blueprint, jsonify

login = Blueprint('login', __name__)

@login.route('/')
def index(): 
    return {'index': 'login'}

@login.get('login')
def items_login():
    return jsonify({"content": "['Nome', 'email' , telefone , 'senha']"})

@login.route('/', methods=['POST'])
def inserir_login():
    pass

@login.route('/<int:login_id>/update', methods = ['PUT'])
def atualizar_login(login_id):
    pass

@login.route('/<int:login_id>/delete', methods = ['DELETE'])
def deletar_login(login_id):
    pass