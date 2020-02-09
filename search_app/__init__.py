from flask import Flask

from search_app import config


def create_app(configuration=config.BaseConfig):

    app = Flask(__name__)
    app.config.from_object(configuration)

    with app.app_context():
        from views import bp
        app.register_blueprint(bp)

    return app
