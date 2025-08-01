from flask import request, redirect, url_for, Blueprint
from flask_login import login_required
from models.producto_model import Producto
from views import producto_view

producto_bp = Blueprint('producto', __name__, url_prefix="/productos")

@producto_bp.route("/")
@login_required
def index():
    productos = Producto.get_all()
    return producto_view.list(productos)

@producto_bp.route("/create", methods = ['GET','POST'])
@login_required
def create():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        obs = request.form['obs']

        producto = Producto(descripcion, precio, obs)
        producto.save()
        return redirect(url_for('producto.index'))
    return producto_view.create()

@producto_bp.route("/edit/<int:id>", methods = ['GET','POST'])
@login_required
def edit(id):
    producto = Producto.get_by_id(id)
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        obs = request.form['obs']

        producto.update(descripcion=descripcion, precio=precio, obs=obs)
        return redirect(url_for('producto.index'))
    return producto_view.edit(producto)

@producto_bp.route("/delete/<int:id>")
@login_required
def delete(id):
    producto = Producto.get_by_id(id)
    producto.delete()
    return redirect(url_for('producto.index'))

