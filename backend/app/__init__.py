from flask import Flask
from app.routes.recipe_routes import recipe_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(recipe_bp, url_prefix="/api/recipes")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
