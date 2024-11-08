import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from flask import Blueprint, jsonify, request
import bdlogin

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/')
def index():
    return {'login bp': 'index'}

@login_bp.route('/login', methods=['POST'])
def search_user():
    dataJson = request.json

    if (dataJson['phone'] != '' and dataJson['password'] != ''):
        if(bdlogin.search_user(dataJson=dataJson != False)):
            return {'status': True}
        else:
            return {'status': False}

