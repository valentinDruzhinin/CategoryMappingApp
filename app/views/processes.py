from flask import jsonify
from app.tasks import category_batch_processing


def process(process_id):
    """Checks status of running task"""
    proc = category_batch_processing.AsyncResult(process_id)
    return jsonify({
        'state': proc.state
    })
