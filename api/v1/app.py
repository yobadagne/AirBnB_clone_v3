#!/usr/bin/python3
""" api app.py file """

from flask import Flask
import os
from models import storage
from api.v1.views import app_views
app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(err):
    """ close storage """
    storage.close()
if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = os.environ.get('HBNB_API_PORT', '5000')
    app.run(host=host, port=int(port), threaded=True)
