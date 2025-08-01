from flask import Flask, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from controllers import cliente_controller, vendedor_controller, producto_controller, prestamo_controller, auth_controller
from models.vendedor_model import Vendedor
from database import db

app = Flask(__name__)
app.secret_key = "miclavesecreta"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tienda.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

db.init_app(app)
app.register_blueprint(cliente_controller.cliente_bp)
app.register_blueprint(vendedor_controller.vendedor_bp)
app.register_blueprint(producto_controller.producto_bp)
app.register_blueprint(prestamo_controller.prestamo_bp)
app.register_blueprint(auth_controller.auth_bp)

@login_manager.user_loader
def load_user(user_id):
    return Vendedor.query.get(int(user_id))

@app.route("/")
def home():
    return redirect(url_for('auth.login'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)