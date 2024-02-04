from flask import Flask, render_template, request, redirect
from cs50 import SQL


app = Flask(__name__)
db = SQL("sqlite:///tasks.db")


@app.route('/')
def index():
    tasks = db.execute("SELECT * FROM todo")
    return render_template("index.html", tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    task = request.form.get("task")
    db.execute("INSERT INTO todo (task, status) VALUES (?, ?)", task, -1)
    return redirect('/')


@app.route('/update/<int:task_id>')
def update(task_id):
    curr_status = db.execute("SELECT status FROM todo WHERE id = ?", task_id)[0]['status']
    new_status = -1 * curr_status
    db.execute("UPDATE todo SET status = ? WHERE id = ?", new_status, task_id)
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete(task_id):
    db.execute("DELETE FROM todo WHERE id = ?", task_id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
