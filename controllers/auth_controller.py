from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import UserMixin
from models.vendedor_model import Vendedor

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasenia = request.form['contrasenia']

        vendedor = Vendedor.query.filter_by(nombre=nombre).first()

        if vendedor and vendedor.verify_password(contrasenia):
            session['vendedor_id'] = vendedor.id
            session['vendedor_nombre'] = vendedor.nombre
            return redirect(url_for('producto.index'))  # o donde quieras redirigir
        else:
            flash('Nombre o contraseña incorrectos')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
