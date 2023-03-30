from flask import Blueprint
from . import controllers

banca = Blueprint('banca', __name__)

banca.add_url_rule(
    '/producto', view_func=controllers.crudProducto, methods=['GET', 'POST', 'PUT','DELETE'])

banca.add_url_rule(
    '/categorias', view_func=controllers.crudCategoria, methods=['GET', 'POST', 'PUT','DELETE'])


