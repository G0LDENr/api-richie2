from flask import Blueprint

blueprintHome = Blueprint('home', __name__)
@blueprintHome.route('/home')
def home():
    return {"message": "Hola desde home"}