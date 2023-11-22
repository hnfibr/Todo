#This is the application server which will receive requests which require
#business logic from the web server to process them and respond with the
#correct status for the task

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PickleType
# from flask_cors import CORS
import json


from code_base import access
from code_base import reader
from code_base import create
from code_base import edit
from code_base import delete

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)

# CORS(app, resourses={r"/logout": {"origins": "http://127.0.0.1:5000"}})


class Data(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(50),nullable=False)
    todos=db.Column(PickleType, default=[])
    order=db.Column(PickleType, default=[])
    amount=db.Column(db.Integer, default=0)
    
    
    def __repr__(self):
        return '<Task %r>' % self.id
        







#for creating an account
@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.get_json()
    
    return access.createAccount(data['username'],data['password'], Data, db)
    

#for logging into an account
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    return access.loginAccount(data['username'],data['password'], Data, db)




    
@app.route('/read', methods=['POST'])
def read():
    id = request.get_json()
    
    return reader.read(id, Data)



#for creating a todo
@app.route('/create', methods=['POST'])
def create():
    pass
    
    
    
@app.route('/edit', methods=['POST'])
def edit():
    pass
    
    
@app.route('/delete', methods=['POST'])
def delete():
    pass


@app.route('/logout', methods=['POST'])
def logout():
    pass











if __name__ == "__main__":
    app.run(debug=True, port=5100)