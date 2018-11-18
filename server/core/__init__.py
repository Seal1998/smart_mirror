from flask import Flask
from .db import db

def factory():
    app = Flask(__name__)
    app.config.from_object('core.config.BaseConfig')
    db.init_app(app)
    from .settings_bp import blueprint as settings
    app.register_blueprint(settings)

    return app