from flask import Flask,request,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from configparser import ConfigParser



app = Flask(__name__)

CORS(app)

file = 'configuration.ini'
config = ConfigParser()
config.read(file)

userName = config['connection']['username']
password = config['connection']['password']


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pyodbc://{userName}:{password}@localhost/contactsDB?driver=MySQL+ODBC+9.2+ANSI+Driver&Trusted_Connection=yes'.format(userName=userName, password=password)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    
@app.before_request
def create_table():
    if not hasattr(app,'tables_created'):
        db.create_all()
        app.tables_created = True
    
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/submit',methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    email= data.get('email')
    message = data.get('message')
    
    new_contact = Contact(name=name, email=email, message=message)
    db.session.add(new_contact)
    db.session.commit()
    
    response_message = f"Thank You, {name} your message is received"
    return jsonify({'message':response_message})



if __name__ == '__main__':
    app.run(debug=True)