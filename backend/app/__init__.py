from flask import Flask
from flask_cors import CORS
from app.routes.recipe_routes import recipe_bp
import os

frontend_url = os.getenv("FRONTEND_URL")


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": frontend_url}})
    app.register_blueprint(recipe_bp, url_prefix="/api/recipes")
    return app
