from flask import Flask, Response,request,session
from flask.json import jsonify
import settings
import extensions
import Views

app = Flask(__name__)
app.config.from_object(settings.envs.get('develop'))
extensions.init_extentions(app)
Views.init_blues(app)






if __name__ == '__main__':
    app.run(debug=True)