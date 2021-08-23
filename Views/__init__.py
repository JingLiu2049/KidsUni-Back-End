from flask import blueprints
from Views.account import accountBlue
from Views.events import eventsBlue

def init_blues(app):
    app.register_blueprint(blueprint = accountBlue)
    app.register_blueprint(blueprint = eventsBlue)