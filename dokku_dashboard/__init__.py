import os

from flask import Flask


app = Flask(__name__)
app.debug = os.environ.get('DEBUG', False)
