import os

from flask import Flask
from . import routes
from ..instance import config


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config.Config())
    os.makedirs(app.instance_path, exist_ok=True)
    app.register_blueprint(routes.bp)
    print("SERVER READY")
    return app
