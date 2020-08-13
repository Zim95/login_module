from flask import Flask
from flask_restful import Api
from flask_oauthlib.provider import OAuth2Provider
from flask_sqlalchemy import SQLAlchemy


def create_app(config=None):
    app = Flask(__name__)
    api = Api(app)
    oauth = OAuth2Provider(app)
    db = SQLAlchemy(app)
    return {
        'app': app,
        'api': api,
        'oauth': oauth,
        'db': db
    }
