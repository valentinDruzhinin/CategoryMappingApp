from flask import request, current_app, jsonify
from app.models import Category
from app.tasks import category_batch_processing


CATEGORY_FILTER_KEYS = ('name', 'mapping')


def categories():
    """Works with categories"""
    if request.method == 'GET':
        filter_params = {key: request.args[key] for key in CATEGORY_FILTER_KEYS if request.args.get(key)}
        return jsonify(
            [{'id': c.id} for c in current_app.categories.query(**filter_params)]
        )
    elif request.method == 'POST':
        request_body = request.get_json()
        if isinstance(request_body, list):
            task = category_batch_processing.delay(request_body)
            return jsonify({'process_id': task.id}), 202
        else:
            model = current_app.categories.add(Category(**request_body))
            return jsonify({'id': model.id})
