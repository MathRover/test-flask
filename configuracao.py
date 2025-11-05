from routes.home import home_routes
from routes.cliente import cliente_rout
from database.database import db
from database.models.cliente import Cliente

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_routes)
    app.register_blueprint(cliente_rout, url_prefix="/cliente")

def configure_db():
    db.connect()
    db.create_tables([Cliente])


