"""
Author: Derek Nelsen
Date: 06/21/2017

This is where the app is imported and run from
"""

from application import create_app


# Point to the configuration file
# Run the app
app = create_app('config_dev.py')
app.run()