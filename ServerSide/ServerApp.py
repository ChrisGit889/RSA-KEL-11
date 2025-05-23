from flask import Flask , jsonify, request , make_response
import json

app = Flask(__name__)

"""
    Login details store list of tups
    (email, public_key)
"""
loginDetails: list[tuple[str,int]] = []

@app.route('/' , methods=['GET'])
def getHome():
    return jsonify({"message":'Hello. This is a trial message'})

@app.route('/login/' , methods=['POST'])
def postLoginDetails():
    data = json.loads(request.data)
    if not (data["email"] or data["pubKey"]):
        response = make_response(jsonify({'message':'LOGIN INCOMPLETE'}))
        response.headers.set('Content-Type', 'application/json')
        response.status_code = 422
        return response
    
    found = False
    for i in loginDetails:
        if data['email'] == i[0]:
            i[1] = data['pubKey']
            found = True
    
    if not found :
        loginDetails.append(data['email'],data['pubKey'])


    response = make_response(jsonify({'mesage':'Login success'}))
    response.headers.set('Content-Type', 'application/json')
    response.status_code = 202
    return response

@app.route('/users/',methods=['GET'])
def getUsers():
    users = [{'name': i[0] , 'pubKey': i[1]} for i in loginDetails]
    return jsonify({'users': users})

app.run()