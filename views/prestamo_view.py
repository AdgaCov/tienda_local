from flask import render_template

def list(prestamos):
    return render_template('prestamos/index.html', prestamos=prestamos)

def create(clientes, productos, vendedores):
    return render_template('prestamos/create.html', clientes=clientes, productos=productos, vendedores=vendedores)

def edit(prestamo, clientes, productos, vendedores):
    return render_template('prestamos/edit.html', prestamo=prestamo, clientes=clientes, productos=productos, vendedores=vendedores)
