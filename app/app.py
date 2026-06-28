from flask import Flask, render_template

from task_service import get_tasks

app = Flask(__name__)


@app.route("/")
def home():
    tasks = get_tasks() #get data from task_service.py
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)