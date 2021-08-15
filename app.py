from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Configure sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todoslist(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/edit")
def home():
    todos_list = Todoslist.query.all()
    return render_template("base.html", todos_list=todos_list)


@app.route("/")
def listTodos():
    todos_list = Todoslist.query.all()
    return render_template("list.html", todos_list=todos_list)


@app.route("/add", methods=["POST"])
def addTodos():    
    task = request.form.get("task")
    new_todos = Todoslist(task=task, complete=False)
    db.session.add(new_todos)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def updateTodos(todo_id):
    todo = Todoslist.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def deleteTodos(todo_id):
    todo = Todoslist.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    # app.run()
    db.create_all()
    app.run(debug=True)
