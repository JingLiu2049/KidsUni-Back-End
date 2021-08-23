from extensions import db
class Users(db.Model):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
    _id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    role = db.Column(db.String(20))
    name = db.Column(db.String(50))

    def keys(self):
        return("_id","email","password","role","name")
    def __getitem__(self,item):
        return getattr(self,item)