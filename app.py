from flask import Flask, Response,request,session
from flask.json import jsonify
import json

from flask.wrappers import Request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kidsUni_rebuilding_server'

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

        events = []
        topics = ['graduation','other','visit','community']
        locations=['Lincole Uni','Canterbury Uni','other']
        for i in range(29):
            events.append(
                {
                    '_id':f'{i}',
                    'title':f'{topics[i%4]} {i}',
                    'topic':f'{topics[i%4]}',
                    'date':f'{i+1}/06/2021',
                    'location':f'{locations[i%3]}',
                    'note':''
                }
            )
        session['events'] = events

        
    else:
        user ={
            'status':0,
            'msg':'Incorrect password!'
        }
    response = Response(json.dumps(user),content_type='application/json')
    return response

@app.route('/events',methods=['GET','POST','DELETE'])
def events():
    events = session['events']
    if request.method=='DELETE':
        eventObj = request.get_json()
        for i in events:
            if i.get('_id') == str(eventObj.get('_id')):
                events.remove(i)
                session['events'] = events
                break

    response = {'status':1,'data':events} 
    
    return jsonify(response)
@app.route('/events/update',methods=['POST'])
def updateEvent():
    if request.method == 'POST':
        formData = request.get_json()
        events = session['events']
        print(formData)
        if formData.get('_id') == 'new':
            print(formData)
            events.append(formData)
            session['events'] = events
            print(session['events'])
            response = {
                'status':1,
                'msg':'new event added'
            }
        else:
            for i in events:
                if i.get('_id') == formData.get('_id'):
                    events.remove(i)
                    events.append(formData)
                    session['events'] = events
            response = {
                'status':1,
                'msg':'event updated'
            }

        return jsonify(response)
if __name__ == '__main__':
    app.run(debug=True)