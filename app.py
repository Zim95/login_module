from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config.exceptions import register_error_handler
from config import settings
from open_oauth.resources import Ping
from flask_oauthlib.provider import OAuth2Provider


app = Flask(__name__)
app = register_error_handler(app)


# DATABASE CONFIGURATION
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['BUNDLE_ERRORS'] = settings.BUNDLE_ERRORS


db = SQLAlchemy(app)
api = Api(app)
oauth = OAuth2Provider(app)


api.add_resource(Ping, '/ping')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)