from flask import Flask
from configuracao import configure_all

#Inicia o Flask
app = Flask(__name__)
 
configure_all(app) 

#iniciar o projeto
if __name__ == "__main__":
    app.run(debug=True)