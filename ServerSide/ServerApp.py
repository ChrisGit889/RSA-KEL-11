from flask import Flask , jsonify, request , make_response
import json

app = Flask(__name__)

"""
    Login details store list of tups
    (email, public_key)
"""
loginDetails: list[tuple[str,int , int]] = []

"""
    Messages stores send address and message
"""
messages : list[tuple[str,str]]= []

@app.route('/' , methods=['GET'])
def getHome():
    return jsonify({"message":'Hello. This is a trial message'})

@app.route('/login/' , methods=['POST'])
def postLoginDetails():
    data = json.loads(request.data)
    if not (data["email"] or data["n"] or data['e']):
        response = make_response(jsonify({'message':'LOGIN INCOMPLETE'}))
        response.headers.set('Content-Type', 'application/json')
        response.status_code = 422
        return response
    
    found = False
    for i in loginDetails:
        if data['email'] == i[0]:
            i[1] = data['e']
            i[2] = data['n']
            found = True
    
    if not found :
        loginDetails.append((data['email'],data['e'] , data['n']))


    response = make_response(jsonify({'mesage':'Login success'}))
    response.headers.set('Content-Type', 'application/json')
    response.status_code = 202
    return response

@app.route('/users/',methods=['GET'])
def getUsers():
    users = [{'email': i[0] , 'e': i[1] , 'n' : i[2]} for i in loginDetails]
    return jsonify({'users': users})

@app.route('/send/' , methods=['POST'])
def postMessage():
    data = json.loads(request.data)
    if not (data['email']):
        response = make_response(jsonify({'message':'Message not sent'}))
        response.headers.set('Content-Type', 'application/json')
        response.status_code = 422
        return response
    
    messages.append((data['email'] , data['message']))
    print(messages)
    response = make_response(jsonify({'mesage':'Message sent'}))
    response.headers.set('Content-Type', 'application/json')
    response.status_code = 202
    return response

@app.route('/messages/<name>' , methods=['GET'])
def getMessages(name):
    if name not in [i[0] for i in messages]:
        response = make_response(jsonify({'messages':[]}))
        response.headers.set('Content-Type' , 'application/json')
        response.status_code = 202
        return response
    
    toSend = []
    for i in messages:
        if i[0] == name:
            toSend.append(i[1])
    
    response = make_response(jsonify({'messages' : toSend}))
    response.headers.set('Content-Type' , 'application/json')
    response.status_code = 202
    return response


app.run()