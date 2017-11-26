import os

from flask import Flask


app = Flask(__name__)

dotenv_path = os.path.join(os.getcwd(), '.env')
if os.path.isfile(dotenv_path):
    from dotenv import load_dotenv
    load_dotenv(dotenv_path)

app.debug = os.environ.get('DEBUG', False)
