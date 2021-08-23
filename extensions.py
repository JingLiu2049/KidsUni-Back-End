from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrates = Migrate()

def init_extentions(app):
    db.init_app(app = app)
    migrates.init_app(app=app,db=db)