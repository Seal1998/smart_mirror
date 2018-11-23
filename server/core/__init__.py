from flask import Flask

def factory():
    app = Flask(__name__)
    app.config.from_object('core.config.BaseConfig')
    from .settings_bp import blueprint as settings
    app.register_blueprint(settings)

    return app