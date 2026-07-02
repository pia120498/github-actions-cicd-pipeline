from flask import Flask, render_template, request, redirect
from flask import jsonify
from task_service import get_tasks, add_task

app = Flask(__name__)


@app.route("/")
def home():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)


# @app.route("/health")
# def health():
#     return {
#         "status": "healthy"
#     }, 200


@app.route("/add", methods=["POST"])
def create_task():
    task_name = request.form["task"]

    if task_name.strip():
        add_task(task_name)

    return redirect("/")

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)