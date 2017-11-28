import os

from flask import Flask


app = Flask(__name__)
app.debug = os.environ.get('DEBUG', False)
app.server_protocol = os.environ.get('SERVER_PROTOCOL')
app.server_host = os.environ.get('SERVER_HOST')
