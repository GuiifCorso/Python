from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get_login_data", methods=['POST'])
def log_data():
    name = request.form.get('lname')
    password = request.form.get('lpassword')

    user = User.query.filter_by(name=name).first()

    if user and bcrypt.checkpw(password.encode("utf-8"), user.password):
        return "Correct data"
    else:
        return "Incorrect data"


@app.route("/get_reg_data", methods=['POST'])   
def reg_data():
    name = request.form.get('rname')
    password = request.form.get('rpassword')

    hash_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    registered = User.query.filter_by(name=name).first()
    if registered:
        return "User registered"
    else:
        new_user = User(name=name, password=hash_pass)
        db.session.add(new_user)
        db.session.commit()
        return "Registered successfully"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
