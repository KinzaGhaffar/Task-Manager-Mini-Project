from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.secret_key = "Secret Key"

# Database connection
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/tasklist'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

from datetime import datetime

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
    description = db.Column(db.String(100))
    duedate = db.Column(db.String(100))
    priority = db.Column(db.String(10))
    status = db.Column(db.String(20))

    def __init__(self, task, description, duedate, priority, status):
        self.task = task
        self.description = description
        self.duedate = duedate
        self.priority = priority
        self.status = status


@app.route("/")
def index():
    all_data = Data.query.all()
    return render_template("index.html", tasks = all_data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        task = request.form['task']
        description = request.form['description']
        duedate = request.form['duedate']
        priority = request.form['priority']
        status = request.form['status']

        my_data = Data(task, description, duedate, priority, status)

        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.task = request.form['task']
        my_data.description = request.form['description']
        
        if request.form['duedate']:
            my_data.duedate = datetime.strptime(request.form['duedate'], '%Y-%m-%d')

        my_data.priority = request.form['priority']
        my_data.status = request.form['status']

        db.session.commit()
        return redirect(url_for('index'))



@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)

    db.session.commit()
    return redirect(url_for('index'))



if __name__ == "__main__":
    # Use Flask-Migrate commands for database migration
    from flask_migrate import upgrade

    # Ensure that you are within the application context
    with app.app_context():
        upgrade()

    # Run the Flask application
    app.run(debug=True)