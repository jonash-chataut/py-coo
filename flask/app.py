from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todolist.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_executed = db.Column(db.DateTime , default = datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        title=request.form['title']
        desc= request.form['desc']
        todo = Todo(title=title,desc = desc)
        db.session.add(todo)
        db.session.commit()
    alltodos = Todo.query.all()
    return render_template("index.html", alltodos=alltodos)

@app.route("/show")
def products():
    alltodos = Todo.query.all()
    print(alltodos)
    return "The products are here"

@app.route("/update")
def update():
    alltodos = Todo.query.all()
    print(alltodos)
    return "The products are here"

@app.route("/delete/<int:sno>")
def delete(sno):
    todo_del = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo_del)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    # to create the database file 
    # with app.app_context():
    #     db.create_all() 
    app.run(debug=True,port=8000)
