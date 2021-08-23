from logging import error
from flask import Blueprint,request,Response,json,jsonify
from models.events import Events,db
from datetime import datetime as dt
from sqlalchemy import update

eventsBlue = Blueprint('events',__name__)

def getEventList():
    events = db.session.query(Events).order_by('_id').all()
    results=[]
    for i in events:
        i.date = i.date.strftime('%d-%m-%Y')
        results.append(dict(i))
    return results

@eventsBlue.route('/events',methods=['GET','POST','DELETE'])
def events():
    results = getEventList()
    response = {'status':1,'data':results} 
    return jsonify(response)

@eventsBlue.route('/events/delete',methods=['DELETE'])
def deleteEvent():
    status = None
    msg=''
    try:
        eventToDelete = request.get_json()
        theEvent = Events.query.filter_by(_id=eventToDelete["_id"]).first()
        db.session.delete(theEvent)
        db.session.commit()
    except Exception as e:
        print(e)
        status=0
        msg="Operation incorrect, please try again."
    else:
        status=1
        msg="Event has been deleted."
    finally:
        results = getEventList()
    response = {
        "status":status,
        "data":results,
        "msg":msg
    }
    return jsonify(response)

@eventsBlue.route('/events/add',methods=['POST'])
def addEvent():
    formData = request.get_json()
    try:
        formData.pop('_id')
        formData['date'] = dt.strptime(formData['date'],'%d/%m/%Y')
        newEvent = Events(**formData)
        db.session.add(newEvent)
        db.session.commit()
        
    except Exception as e:
        print(e)
        response = {
            'status':0,
            'msg':'Operation incorrect, please try again.'
        }
    else:
        response = {
            'status':1,
            'msg':'New event added.'
        }

    return jsonify(response)



@eventsBlue.route('/events/update',methods=['POST'])
def updateEvent():
    formData = request.get_json()
    try:
        formData['date'] = dt.strptime(formData['date'],'%d/%m/%Y')
        
        Events.query.filter_by(_id=formData["_id"]).update(formData)
        
        db.session.commit()
        
    except Exception as e:
        print(e)
        response = {
            'status':0,
            'msg':'Operation incorrect, please try again.'
        }
    else:
        response = {
            'status':1,
            'msg':'Event has been updated.'
        }

    return jsonify(response)
