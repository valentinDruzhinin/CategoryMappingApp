from flask import jsonify


def up():
    return jsonify({'status': 'happy'})
