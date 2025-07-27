from database import db

class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    #método para obtener los usuarios y guardarlos en la db
    def save(self):
        db.session.add(self)
        db.session.commit()

    #metodo para devolver los usuarios de la tabla clientes
    @staticmethod
    def get_all():
        return Cliente.query.all()

    #metodo para devolver solo un registro:
    @staticmethod
    def get_by_id(id):
        return Cliente.query.get(id)

    #metodo para actualizar
    def update(self, nombre=None, telefono=None):
        if nombre and telefono:
            self.nombre = nombre
            self.telefono = telefono
        db.session.commit()

    #metodo para eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()