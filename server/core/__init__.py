from flask import Flask
from .db import db

def factory():
    app = Flask(__name__)
    app.config.from_object('core.config.BaseConfig')
    db.init_app(app)

    return app