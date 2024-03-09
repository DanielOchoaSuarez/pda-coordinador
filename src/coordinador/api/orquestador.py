from flask import Blueprint, jsonify

ab = Blueprint('orquestador', __name__)


@ab.route('/ping', methods=['GET'])
def health():
    return jsonify({'result': 'pong'})
