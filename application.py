from flask import Flask
from flask_mongoengine import MongoEngine

#setup DB
db = MongoEngine


def create_app(**config_override):
    app = Flask(__name__)

    app.config.from_pyfile("settings.py")

    app.config.update(config_override)

    db.init_app(app)

    from counter.views import counter_app

    app.register_blueprint(counter_app)

    return app