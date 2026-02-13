from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Security Headers configuration
talisman = Talisman(app, content_security_policy=None)
