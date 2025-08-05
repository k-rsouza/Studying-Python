from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "Pagina sobre"





# Garante que so quando executado manualmente o servidor sera subido dessa forma
# Mas esta forma é recomendada apenas para desenvolvimento local
if __name__ == "__main__":
    app.run(debug=True)
