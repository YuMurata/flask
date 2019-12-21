from flask import Flask
from .database import initialize_database
from .views import bp_list
from .auth import create_login_manager
from .config import get_config


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config('debug'))

    initialize_database(app)

    for bp in bp_list:
        app.register_blueprint(bp)

    return app


app = create_app()
login_manager = create_login_manager(app)
