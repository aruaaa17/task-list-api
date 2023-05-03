from flask import Blueprint, request, jsonify
from app.models.task import Task
from app import db

# Define all routes with tasks_bp start with url_prefix (/tasks)
tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

# @blueprint_name.route("/endpoint/path/here", methods=["GET"])
# def endpoint_name():
#     my_beautiful_response_body = "Hello, World!"
#     return my_beautiful_response_body

@tasks_bp.route("", methods=["POST"])
def create_a_task():
    
    
    request_body = request.get_json()
    
    new_task = Task(title=request_body["title"], description=request_body["description"], completed_at=request_body["completed_at"])
    
    db.session.add(new_task)
    db.session.commit()
    
    return {
        "task": {
            "id": new_task.task_id,
            "title": new_task.title,
            "description": new_task.description,
            "is_complete": new_task.is_complete
        }
    }, 201
    
@tasks_bp.route("", method=["GET"])
def get_saved_tasks():
    tasks = Task.query.all()
    task_response = []
    # Question: Isn't query.all() return result as a list already? why append again?
    if not tasks:
        for task in tasks:
    # Question: will this work without to_dict()?
            task_response.append(task)
        return jsonify(task_response), 200
    else:
        return task_response, 200