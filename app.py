from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for tasks
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'Description for Task 1',
        'completed': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'Description for Task 2',
        'completed': True
    }
]

# API endpoint for creating a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'completed': False
    }
    tasks.append(new_task)
    return jsonify({'message': 'Task created successfully', 'task': new_task}), 201

# API endpoint for retrieving all tasks
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    return jsonify({'tasks': tasks})

# API endpoint for retrieving a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify({'task': task})

# API endpoint for updating an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    task['title'] = request.json['title']
    task['description'] = request.json['description']
    task['completed'] = request.json['completed']
    return jsonify({'message': 'Task updated successfully', 'task': task})

# API endpoint for deleting a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)