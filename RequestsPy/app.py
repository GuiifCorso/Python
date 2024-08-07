from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'  # For SQLite
# Use appropriate URI for PostgreSQL or MySQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

clients = []  # List to store client data

db = SQLAlchemy(app)

class Client(db.Model):  # Create a model for your Client table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10))
    spends = db.Column(db.Float)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_client', methods=['POST'])
def register_client():
    name = request.form.get('name')
    age = int(request.form.get('age'))  # Convert to integer
    gender = request.form.get('gender')
    spends = float(request.form.get('spends'))  # Convert to float

    existing_client = Client.query.filter_by(name=name).all()
    if existing_client:
        return "Client with this name already exists!"

    new_client = Client(name=name, age=age, gender=gender, spends=spends)
    db.session.add(new_client)  # Add the new client to the session
    db.session.commit()  # Commit the changes to the database

    return "Client registered successfully!"

@app.route('/get_clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()  # Query all clients from the database
    client_list = [{'name': c.name, 'age': c.age, 'gender': c.gender, 'spends': c.spends} for c in clients]
    return jsonify(client_list)  # Return the list of client dictionaries



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
