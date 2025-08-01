from flask import request, redirect, url_for, Blueprint
from flask_login import login_required
from models.cliente_model import Cliente
from views import cliente_view

cliente_bp = Blueprint('cliente', __name__,url_prefix="/clientes")

@cliente_bp.route("/")
@login_required
def index():
    #recupera todos los registros de la tabla cliente en forma de objeto
    clientes = Cliente.get_all()
    return cliente_view.list(clientes)

@cliente_bp.route("/create", methods=['GET','POST'])
@login_required
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']

        cliente = Cliente (nombre, telefono)
        cliente.save()
        return redirect(url_for('cliente.index'))
    return cliente_view.create()

@cliente_bp.route("/edit/<int:id>", methods = ['GET', 'POST'])
@login_required
def edit(id):
    cliente = Cliente.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']

        #actualizar
        cliente.update(nombre=nombre, telefono=telefono)
        return redirect(url_for('cliente.index'))
    return cliente_view.edit(cliente)

@cliente_bp.route("/delete/<int:id>")
@login_required
def delete(id):
    cliente = Cliente.get_by_id(id)
    cliente.delete()
    return redirect(url_for('cliente.index'))