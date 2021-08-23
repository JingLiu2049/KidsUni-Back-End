from flask import Blueprint,request,Response,json
from models.account import Users,db

accountBlue = Blueprint('account',__name__)

@accountBlue.route('/login',methods=['POST'])
def login():
    req = request.get_json()
    theUser = Users.query.filter_by(email=req['email']).first()
    result ={}
    if theUser and theUser.password == req['password']:
        result ={
            'status':1,
            'data':dict(theUser)
        }
    elif theUser and  theUser.password != req['password']:
        result ={
        'status':0,
        'msg':'Incorrect Password!'
        }
    elif not theUser:
        result ={
        'status':0,
        'msg':'Incorrect Email Address!'
        }
    else:
        result ={
        'status':0,
        'msg':'Incorrect Input, please check your Email address or Password!'
        }

    response = Response(json.dumps(result),content_type='application/json')
    return response


