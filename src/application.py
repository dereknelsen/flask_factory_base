"""
Author: Derek Nelsen
Date: 06/21/2017

This is the main hub for the application. It's kept in
function form to allow for easy testing and to enable
us to have multiple app instances running.
"""

from flask import Flask
from extensions import db


def create_app(config_filename):
    """
    Creates the app instance

    :param config_filename: Set configuration file
    :return: app
    """

    # Initiate the app
    app = Flask(__name__)

    # Point to the configuration file
    app.config.from_pyfile(config_filename)

    # Create our database
    db.init_app(app)

    # Import our blueprints
    from blueprints.admin.views import admin

    # Register our blueprints
    app.register_blueprint(admin)

    # Give the run.py file our app
    return app

