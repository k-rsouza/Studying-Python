from flask import Flask, request
from models.task import Task

app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete
# Tabela: Tarefa

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    print(data)
    return 'Test'

# Garante que so quando executado manualmente o servidor sera subido dessa forma
# Mas esta forma é recomendada apenas para desenvolvimento local
if __name__ == "__main__":
    app.run(debug=True)
