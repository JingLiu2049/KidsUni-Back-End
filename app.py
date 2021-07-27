from flask import Flask, Response,request
from flask.json import jsonify
import json

from flask.wrappers import Request

app = Flask(__name__)


@app.route('/aaa')
def indx():
    user = request.args
    return 'aaa'
@app.route('/login',methods=['POST'])
def login():
    req = request.get_json()
    user={}
    if req['email']== '123@123.com':
        user = {
            'status':1,
            'data':{'_id':111,
            'email':'test@test.com',
            'password':'123456',
            'role':'admin',
            'name':'xiaohei'}
        }
    else:
        user ={
            'status':0,
            'msg':'Incorrect password!'
        }
    response = Response(json.dumps(user),content_type='application/json')
    return response



if __name__ == '__main__':
    app.run(debug=True)