from flask import Flask, jsonify, request

app = Flask(__name__)


tasks = []


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    if not request.json or "title" not in request.json:
        return jsonify({"error": "Missing title"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": request.json["title"],
        "completed": False
    }
    tasks.append(task)
    return jsonify({"message": "Task added", "task": task}), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    task["title"] = request.json.get("title", task["title"])
    task["completed"] = request.json.get("completed", task["completed"])
    return jsonify({"message": "Task updated", "task": task})


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
