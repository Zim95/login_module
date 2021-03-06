from werkzeug.exceptions import HTTPException, default_exceptions
from flask import jsonify


def register_error_handler(app):
    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code  = e.code
        return jsonify(error=str(e)), code

    for ex in default_exceptions:
        app.register_error_handler(ex, handle_error)
    return app
