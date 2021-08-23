from extensions import db

class Events(db.Model):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


    _id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(200))
    topic = db.Column(db.String(200))
    date = db.Column(db.DateTime)
    location = db.Column(db.String)
    note = db.Column(db.Text)

    def keys(self):
        return("_id","title","topic","date","location","note")
    def __getitem__(self,item):
        return getattr(self,item)