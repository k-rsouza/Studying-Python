from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "key"
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///database.db'    # config fixa para caminho do banco
db = SQLAlchemy(app)   # criando instancia do ORM e passando a classe como parametro

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)

