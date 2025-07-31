from database import db

class Vendedor(db.Model):
    __tablename__ = "vendedores"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable = False)
    contrasenia = db.Column(db.String(80), nullable = False)
    telefono = db.Column(db.String(20), nullable = False)

    #relacion
    prestamos = db.relationship('Prestamo', back_populates='vendedor')

    def __init__(self, nombre, contrasenia, telefono):
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.telefono = telefono

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
        if nombre and contrasenia and telefono:
            self.nombre = nombre
            self.contrasenia = contrasenia
            self.telefono = telefono
        db.session.commit()

    #metodo para eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        