from database import db

class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float(3,2), nullable=False)
    obs = db.Column(db.String(100), nullable=False)

    def __init__(self, descripcion, precio, obs):
        self.descripcion = descripcion
        self.precio = precio
        self.obs = obs

    #objeto de tipo usuario y guardarlo en la bd
    def save(self):
        db.session.add(self)
        db.session.commit()

    #met para devolver los productos a la tabla
    @staticmethod
    def get_all():
        return Producto.query.all()
    
    #met para recuperar un registro
    @staticmethod
    def get_by_id(id):
        return Producto.query.get(id)
    
    #met para actualizar
    def update(self, descripcion=None, precio=None, obs=None):
        if descripcion and precio and obs:
            self.descripcion = descripcion
            self.precio = precio
            self.obs = obs
        db.session.commit()

    #met delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()

