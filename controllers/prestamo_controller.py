from flask import request, redirect, url_for, Blueprint

from models.cliente_model import Cliente
from models.producto_model import Producto
from models.vendedor_model import Vendedor
from models.prestamo_model import Prestamo

from views import cliente_view, producto_view, vendedor_view, prestamo_view

prestamo_bp = Blueprint ('prestamo', __name__, url_prefix="/prestamos")

@prestamo_bp.route("/")
def index():
    prestamos = Prestamo.get_all()
    return prestamo_view.list(prestamos)

@prestamo_bp.route("/create", methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        producto_id = request.form['producto_id']
        vendedor_id = request.form['vendedor_id']
        estado = request.form['estado']

        prestamo = Prestamo(cliente_id=cliente_id, producto_id=producto_id, vendedor_id=vendedor_id, estado=estado)
        prestamo.save()
        return redirect(url_for('prestamo.index'))
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    vendedores = Vendedor.query.all()

    return prestamo_view.create(clientes, productos, vendedores)

@prestamo_bp.route("/edit/<int:id>", methods = ['GET', 'POST'])
def edit(id):
    prestamo = Prestamo.get_by_id(id)
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        producto_id = request.form['producto_id']
        vendedor_id = request.form['vendedor_id']
        estado = request.form['estado']

        prestamo.update(cliente_id=cliente_id, producto_id=producto_id, vendedor_id=vendedor_id, estado=estado)
        return redirect(url_for('prestamo.index'))
    
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    vendedores = Vendedor.query.all()
    return prestamo_view.edit(prestamo, clientes, productos, vendedores)
    
@prestamo_bp.route("/delete/<int:id>")
def delete(id):
    prestamo = Prestamo.get_by_id(id)
    prestamo.delete()
    return redirect(url_for('prestamo.index'))
