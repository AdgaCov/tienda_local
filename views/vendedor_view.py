from flask import render_template

def list(vendedores):
    return render_template('vendedores/index.html', vendedores=vendedores)

def create():
    return render_template('vendedores/create.html')

def edit(vendedor):
    return render_template('vendedores/edit.html', vendedor=vendedor)