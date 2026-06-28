from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    tasks = [
        {"name": "Deploy Docker Container", "completed": False},
        {"name": "Configure GitHub Actions", "completed": True},
        {"name": "Deploy to Kubernetes", "completed": False},
    ]

    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)