from flask import Flask, redirect, request, render_template

app = Flask(__name__)

todos = []

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form.get("todo")
    todos.append(todo)
    return redirect("/")

if __name__ == "__main__":
    app.run()
