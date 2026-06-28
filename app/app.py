from flask import Flask, render_template, request, redirect

from task_service import get_tasks, add_task

app = Flask(__name__)


@app.route("/")
def home():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def create_task():
    task_name = request.form["task"]

    if task_name.strip():
        add_task(task_name)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)