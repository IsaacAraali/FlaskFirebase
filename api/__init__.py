from flask import Flask
from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("api/key.json")
default_app = initialize_app(cred)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345rtfescdvf'
    app.template_folder = '/home/musemeza/FlaskFirebase/templates'

    from .userAPI import userAPI
    from .courseAPI import courseAPI

    app.register_blueprint(userAPI, url_prefix='/user')
    app.register_blueprint(courseAPI, url_prefix='/course')

    return app