from flask import json
from werkzeug.exceptions import HTTPException


def register_exceptions_handler(app):

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Handler for all server HTTP exceptions. Provides responses in common format"""
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response
