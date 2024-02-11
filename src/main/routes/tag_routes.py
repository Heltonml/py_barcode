from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.tag_creator_view import TagCreatorView
from src.errors.error_handler import handle_errors
from src.validators.tag_creator_validator import tag_creator_validator

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/tag', methods=['POST'])
def create_tag():
    reponse = None
    try:
        tag_creator_validator(request)
        tag_creator_view = TagCreatorView()
        http_request = HttpRequest(body=request.json)
        reponse = tag_creator_view.validate_and_create(http_request)
    except Exception as exception:
        reponse = handle_errors(exception)

    return jsonify(reponse.body), reponse.status_code
