from flask import Flask, request, jsonify
from Task import TaskToDo

app = Flask(__name__)

if __name__ == '__main__':
    task1 = TaskToDo("Task 1", "Reading").to_dict()
    task2 = TaskToDo("Task 2", "Writing").to_dict()

    tasks = [task1, task2]


@app.route('/todos/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    task = find_task_by_id(task_id)
    if task:
        return jsonify(task), 200
    return jsonify({"message": "Task not found"}), 404


@app.route('/todos', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200


@app.route('/todos', methods=['POST'])
def create_task():
    data = request.get_json()
    if "title" in data and "description" in data:
        new_task = TaskToDo(data["title"], data["description"]).to_dict()
        tasks.append(new_task)
        return jsonify(new_task), 201
    return jsonify({"message": "Invalid request data"}), 400


@app.route('/todos/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    task = find_task_by_id(task_id)
    if task:
        data = request.get_json()
        if "title" in data:
            task["title"] = data["title"]
        if "description" in data:
            task["description"] = data["description"]
        return jsonify(task), 200
    return jsonify({"message": "Task not found"}), 404


@app.route('/todos/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = find_task_by_id(task_id)
    if task:
        tasks.remove(task)
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"message": "Task not found"}), 404


def find_task_by_id(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


if __name__ == '__main__':
    app.run(debug=True)
