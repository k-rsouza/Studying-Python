from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete
# Tabela: Tarefa

tasks = []
task_id_control = 1

# Create
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control   # global para usar a variável que foi criada fora do método sem dar erro
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data["title"], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})   # Retornando como JSON para boa prática de acordo com o padrão REST 


# Read
# Read possui 2 endpoints geralmente, o de listagem de todos os objetos, e o de listagem de um objeto específico
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]   # Faz o for dentro da lista iniciada como variavel, puxando o formato do metodo to_dict da classe task.py

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"message": "Não foi possível encontrar a atividade..."}), 404

# Update
#
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break             # Para melhora de performance, ao achar o item para de percorrer a lista

    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade..."}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    
    return jsonify({"message": "Tarefa atualizada com sucesso."})

# Delete
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break           # Para melhora de performance, ao achar o item para de percorrer a lista
    
    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade..."}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso!"})

# Garante que so quando executado manualmente o servidor sera subido dessa forma
# Mas esta forma é recomendada apenas para desenvolvimento local
if __name__ == "__main__":
    app.run(debug=True)
