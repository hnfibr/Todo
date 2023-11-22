#this is the web server which is used to receive http requests from
#clients and respond with html page. When it receives a request which
#requires business logic to be handled it forwards the request to
#the application-server which will process the task and respond to the
#web server, which will in turn respond to the client with what the
#application server responded to it

from flask import Flask, render_template, url_for,request, session, redirect, jsonify
import requests #this is the library used to send http requests to the application server
import json


app = Flask(__name__)
app.secret_key = 'hello'


#this is the function used to send requests module to send the http requests to the app-server by taking in an address and the data to be sent.
def send_request(address,data): 
    url = 'http://127.0.0.1:5100/' + address
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, json=data, headers=headers)
    
    return response.text













#this route is for creating or loging into an account
@app.route('/')
def access():

    if 'id' in session:

        return redirect(url_for('todo'))
    

    return render_template('access.html')


#if you have a valid session it will respond with the front-end for the todo app and also get your todos from the app server
#if you dont have a valid session then you'll get redirected to '/'
@app.route('/todo')
def todo():

    if 'id' in session:

        return render_template('todo.html')

    return redirect(url_for('access'))
    
#send a username and password to this address and the app-server will check them with the users database and send a success message (redirect to /todo) or a fail message
@app.route('/create_account', methods=['POST'])
def create_account():
    received_data = request.get_json()
    
    input = {'username':received_data['username'],'password':received_data['password']}

    app_server_response = json.loads(send_request('create_account', input))
    
   
    if app_server_response['msg'] == 'redirect':
        session['id'] = app_server_response['id']
        return jsonify({'msg':'','redirect':'/todo'})
    else:
        return jsonify({'msg':app_server_response['msg']})
    
#same as '/create_account' but the app-server but for loging in
@app.route('/login', methods=['POST'])
def login():
    received_data = request.get_json()
    
    input = {'username':received_data['username'],'password':received_data['password']}

    app_server_response = json.loads(send_request('login', input))

    if app_server_response['msg'] == 'redirect':
        
        session['id'] = app_server_response['id']
        return jsonify({'msg':'','redirect':'/todo'})
    else:
        return jsonify({'msg':app_server_response['msg']})
        



#this route will be called every time an account is accessed to respond with the username
#and also the todos and their order.        
@app.route('/read', methods=['POST'])
def read():
    if 'id' in session:
        id = session['id']
        
        response = send_request('/read',id)

        return response
    

    
#send your session id together with a data and this route will tell the app-server to create a new todo for the user with that id
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
    
    
    
    
    
#if __name__ == "__main__":
#    app.run(debug=True)