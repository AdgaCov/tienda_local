from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Vendedor(db.Model, UserMixin):
    __tablename__ = "vendedores"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable = False)
    contrasenia = db.Column(db.String(80), nullable = False)
    telefono = db.Column(db.String(20), nullable = False)

    #relacion
    prestamos = db.relationship('Prestamo', back_populates='vendedor')

    def __init__(self, nombre, contrasenia, telefono):
        self.nombre = nombre
        self.contrasenia = self.hash_password(contrasenia)
        self.telefono = telefono
    
    #contraseña
    @staticmethod
    def hash_password(contrasenia):
        return generate_password_hash(contrasenia)
    
    def verify_password(self, contrasenia):
        return check_password_hash(self.contrasenia, contrasenia)
    
    #tener un obj de tipo usuario y guardarlo en la db
    def save(self):
        db.session.add(self)
        db.session.commit()

    #metodo para devolver a los vendedores y guardarlos en la bd
    @staticmethod
    def get_all():
        return Vendedor.query.all()
    
    #metodo para recuperar solo un registro
    @staticmethod
    def get_by_id(id):
        return Vendedor.query.get(id)
    
    #metodo para actualizar
    def update(self, nombre=None, contrasenia=None, telefono=None):
        if nombre:
            self.nombre = nombre
        if contrasenia:
            self.contrasenia = self.hash_password(contrasenia)
        if telefono:
            self.telefono = telefono
        db.session.commit()

    #metodo para eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    