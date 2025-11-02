from flask import Flask
from routes.home import home_routes
from routes.cliente import cliente_rout


app = Flask(__name__)

app.register_blueprint(home_routes)
app.register_blueprint(cliente_rout, url_prefix="/cliente")

if __name__ == "__main__":
    app.run(debug=True)
