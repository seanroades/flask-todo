from flask import Flask, redirect, request, render_template # Import manner

app = Flask(__name__)

todos = []

@app.route("/") # Routing
def index():
    return render_template("index.html", todos=todos) # Page rendering

@app.route("/add", methods=["POST"])
def add():
    todo = request.form.get("todo") # request.get 
    todos.append(todo)
    return redirect("/") # redirect  # Pythonic functions 

if __name__ == "__main__":
    app.run()
