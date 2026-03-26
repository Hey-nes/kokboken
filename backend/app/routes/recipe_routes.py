from flask import request, jsonify, Blueprint
from app.services import recipe_service
from app.repositories.db_manager import get_connection

recipe_bp = Blueprint("recipe_bp", __name__)


# Route to create a recipe
@recipe_bp.route("/", methods=["POST"])
def post_recipe():
    data = request.get_json()
    db_connection = None

    try:
        db_connection = get_connection()
        result = recipe_service.add_new_recipe(db_connection, data)
        return (
            jsonify(
                {"message": f"Recipe with ID: {result} created", "id": result}
            ),
            201,
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    finally:
        if db_connection:
            db_connection.close()


# Route to fetch all recipes
@recipe_bp.route("/", methods=["GET"])
def get_recipes():
    db_connection = None

    try:
        db_connection = get_connection()
        recipes = recipe_service.get_all_recipes(db_connection)
        return jsonify(recipes), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    finally:
        if db_connection:
            db_connection.close()


# Route to fetch recipe by ID
@recipe_bp.route("/id/<int:recipe_id>", methods=["GET"])
def get_recipe_by_id(recipe_id):
    db_connection = None

    try:
        db_connection = get_connection()
        recipe = recipe_service.get_recipe_by_id(db_connection, recipe_id)
        if recipe:
            return jsonify(recipe), 200
        else:
            return jsonify({"error": "Not Found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    finally:
        if db_connection:
            db_connection.close()


# Route to update a specific recipe
@recipe_bp.route("/id/<int:recipe_id>", methods=["PUT"])
def update_recipe(recipe_id):
    data = request.get_json()
    db_connection = None

    try:
        db_connection = get_connection()
        result = recipe_service.update_recipe(db_connection, recipe_id, data)

        return (
            jsonify(
                {"message": f"Recipe with ID: {recipe_id} updated", "id": recipe_id}
            ),
            200,
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    finally:
        if db_connection:
            db_connection.close()


# Route to delete a specific recipe
@recipe_bp.route("/id/<int:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    db_connection = None

    try:
        db_connection = get_connection()
        result = recipe_service.delete_recipe(db_connection, recipe_id)

        return (
            jsonify(
                {"message": f"Recipe with ID: {recipe_id} deleted", "id": recipe_id}
            ),
            200,
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    finally:
        if db_connection:
            db_connection.close()
