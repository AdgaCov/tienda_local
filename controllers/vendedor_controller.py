from flask import request, redirect, url_for, Blueprint
from models.vendedor_model import Vendedor
from views import vendedor_view

vendedor_bp = Blueprint('vendedor',__name__, url_prefix="/vendedores")

@vendedor_bp.route("/")
def index():
    vendedores = Vendedor.get_all()
    return vendedor_view.list(vendedores)

@vendedor_bp.route("/create", methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasenia = request.form['contrasenia']
        telefono = request.form['telefono']

        vendedor = Vendedor(nombre, contrasenia, telefono)
        vendedor.save()
        return redirect(url_for('vendedor.index'))
    return vendedor_view.create()

@vendedor_bp.route("/edit/<int:id>", methods = ['GET', 'POST'])
def edit(id):
    vendedor = Vendedor.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasenia = request.form['contrasenia']
        telefono = request.form['telefono']
        #actulizar
        vendedor.update(nombre=nombre, contrasenia=contrasenia, telefono=telefono)
        return redirect(url_for('vendedor.index'))
    return vendedor_view.edit(vendedor)

@vendedor_bp.route("/delete/<int:id>")
def delete(id):
    vendedor = Vendedor.get_by_id(id)
    vendedor.delete()
    return redirect(url_for('vendedor.index'))