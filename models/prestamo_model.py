from database import db

class Prestamo(db.Model):
    __tablename__ = "prestamos"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    vendedor_id = db.Column(db.Integer, db.ForeignKey('vendedores.id'), nullable=False)
    estado = db.Column(db.String(80), nullable=False)
    
    cliente = db.relationship('Cliente', back_populates= 'prestamos')
    producto = db.relationship('Producto', back_populates='prestamos')
    vendedor = db.relationship('Vendedor', back_populates='prestamos')

    def __init__ (self, cliente_id, producto_id, vendedor_id, estado):
        self.cliente_id = cliente_id
        self.producto_id = producto_id
        self.vendedor_id = vendedor_id
        self.estado = estado
    
    #tener un obj de tipo prestamo y guardarlo en la bd
    def save(self):
        db.session.add(self)
        db.session.commit()

    #devolver prestamos
    @staticmethod
    def get_all():
        return Prestamo.query.all()
    
    #recuperar solo un registro
    @staticmethod
    def get_by_id(id):
        return Prestamo.query.get(id)
    
    #met para actualizar
    def update(self, cliente_id=None, producto_id=None, vendedor_id=None, estado=None):
        if cliente_id and producto_id and vendedor_id and estado:
            self.cliente_id = cliente_id
            self.producto_id = producto_id
            self.vendedor_id = vendedor_id
            self.estado = estado
        db.session.commit()

    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()