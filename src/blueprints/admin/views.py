"""
Author: Derek Nelsen
Date: 06/21/2017

The admin blueprint deals with superuser privledges. It allows for
high-level management of the site, and shouldn't be accessed by
regular accounts.
"""

from flask import Blueprint, render_template, url_for

# Create our blueprint
admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')


# Index route
@admin.route('/')
def index():
    return render_template('admin/admin-index.html')

