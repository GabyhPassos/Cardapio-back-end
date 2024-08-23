import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from flask import Blueprint, jsonify

menus_bp = Blueprint('menus_bp', __name__)

@menus_bp.route('/')
def index(): 
    return {'index': 'menus'}

@menus_bp.get('/menus')
def items_menu():
    return jsonify({"content": "['Pizzas', 'Esfihas']"})