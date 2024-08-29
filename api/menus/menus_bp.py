import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from flask import Blueprint, jsonify

menus_bp = Blueprint('menus_bp', __name__)

@menus_bp.route('/')
def index(): 
    return {'index': 'menus'}

@menus_bp.get('/menus')
def items_menu():
    return jsonify({"content": "['Brigadeiro', 'Cookies']"})

@menus_bp.route('/', methods=['POST'])
def inserir_menus_bp():
    pass

@menus_bp.route('/<int:menus_bp_id>/update', methods = ['PUT'])
def atualizar_menus_bp(menus_bp_id):
    pass

@menus_bp.route('/<int:menus_bp_id>/delete', methods = ['DELETE'])
def deletar_menus_bp(menus_bp_id):
    pass

