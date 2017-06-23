"""
Author: Derek Nelsen
Date: 06/21/2017

This is our global configuration file. In blueprints
this can be referenced with the current_app flask import.
"""

# For development, keep this on true
DEBUG = True

# Database
# sqlite3 for development
SQLALCHEMY_DATABASE_URI = 'sqlite:////dev.db'

# If set to True, this causes a lot of overhead
SQLALCHEMY_TRACK_MODIFICATIONS = False


# SECRET_KEY generator:
# binascii.hexlify(os.urandom(24))
SECRET_KEY = '41a73f77538d6845acbf1c76381ac2165895477a5252866c'