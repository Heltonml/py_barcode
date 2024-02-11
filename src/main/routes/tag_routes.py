from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.tag_creator_view import TagCreatorView

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/tag', methods=['POST'])
def create_tag():
    tag_creator_view = TagCreatorView()
    print(request.json)
    http_request = HttpRequest(body=request.json)
    reponse = tag_creator_view.validate_and_create(http_request)

    return jsonify(reponse.body), reponse.status_code
