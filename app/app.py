from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>🚀 DevOps Task Manager</h1>
    <p>CI/CD Pipeline Project</p>
    <p>Application is running successfully!</p>
    """


if __name__ == "__main__":
    app.run(debug=True)