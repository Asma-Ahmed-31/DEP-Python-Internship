from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and setup database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ToDo model
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Create the database
with app.app_context():
    db.create_all()

# To-Do list resource
@app.route('/todos', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'GET':
        todos = ToDo.query.all()
        return jsonify([{'id': todo.id, 'task': todo.task, 'completed': todo.completed} for todo in todos]), 200
    elif request.method == 'POST':
        data = request.get_json()
        if 'task' not in data:
            abort(400)  # Bad request
        
        new_todo = ToDo(task=data['task'])
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({'id': new_todo.id, 'task': new_todo.task, 'completed': new_todo.completed}), 201

# Individual To-Do item resource
@app.route('/todos/<int:todo_id>', methods=['GET', 'PUT', 'DELETE'])
def todo_item(todo_id):
    todo = ToDo.query.get_or_404(todo_id)
    if request.method == 'GET':
        return jsonify({'id': todo.id, 'task': todo.task, 'completed': todo.completed}), 200
    elif request.method == 'PUT':
        data = request.get_json()
        todo.task = data.get('task', todo.task)
        todo.completed = data.get('completed', todo.completed)
        db.session.commit()
        return jsonify({'id': todo.id, 'task': todo.task, 'completed': todo.completed}), 200
    elif request.method == 'DELETE':
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message": "To-Do item deleted successfully!"}), 200

# New endpoint to get the count of To-Do items
@app.route('/todos/count', methods=['GET'])
def todo_count():
    count = ToDo.query.count()
    return jsonify({'count': count}), 200

app.run(debug=True)  # Run the Flask application