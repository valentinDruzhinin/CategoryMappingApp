from flask import request, current_app, Response, jsonify
from werkzeug import exceptions
from app.models import Category


def category(category_id):
    """Works with certain category"""
    if request.method == 'GET':
        categories = current_app.categories.query(id=category_id)
        if categories:
            return jsonify(categories[0].to_dict())
        raise exceptions.NotFound
    elif request.method == 'PUT':
        request_body = request.get_json()
        current_app.categories.update(
            Category(id=category_id, **request_body)
        )
        return Response(status=204)
    elif request.method == 'DELETE':
        current_app.categories.delete(Category(id=category_id))
        return Response(status=204)
