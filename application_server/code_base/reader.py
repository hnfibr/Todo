#this code is for reading todos of a user from the database
#to send it back to the user 

# from flask import jsonify
import json

def read(id, Data):
    required_user = Data.query.filter_by(id=id).first()
    
    return json.dumps({'username':required_user.username, 'todos':required_user.todos, 'order':required_user.order})
    
