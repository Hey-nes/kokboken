from flask import request, jsonify, Blueprint
from app.services import recipe_service
from app.repositories.db_manager import get_connection

recipe_bp = Blueprint("recipe_bp", __name__)


@recipe_bp.route("/", methods=["POST"])
def post_recipe():
    data = request.get_json()
    db_connection = None

    try:
        db_connection = get_connection()
        result = recipe_service.add_new_recipe(db_connection, data)
        return jsonify(result), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
