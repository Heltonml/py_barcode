from flask import Blueprint, request, jsonify

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/tag', methods=['POST'])
def create_tag():
    print(request.json)
    return jsonify({"msg": "OK"}), 200
