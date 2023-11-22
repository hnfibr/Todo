#codebase for creating and logging into an account
#it also handles the creation of sessions

import json


def createAccount(username, password, Data, db):
    #check if the username is available
    #if it is send a message
    #if it is not then create
    #if success then redirect
    
    
    is_username_taken = Data.query.filter_by(username=username).first()
    
    if is_username_taken == None:
        add = Data(username=username, password=password)
        
        try:
            db.session.add(add)
            db.session.commit()
            
            id =add.id
            
            return json.dumps({'msg':'redirect','id':id})
            
        except:
            return json.dumps({'msg':'Please try again later!'})
    
    else:
        return json.dumps({'msg':'Username is taken!'})



def loginAccount(username,password, Data, db):
    #check if the username is available
    #check if the passwords match
    #if they do then redirect to todo
    #if not tell them sorry
    try:
        is_user_available = Data.query.filter_by(username = username).first()
        
        if is_user_available == None:
            return json.dumps({'msg':'Username not found.'})
        else:
            if is_user_available.password == password:
                id = is_user_available.id
                return json.dumps({'msg':'redirect','id':id})
            else:
                return ({'msg':'Incorrect password.'})
    except:
        return ({'msg':'Please try again later!'})
        

