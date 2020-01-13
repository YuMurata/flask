from flask import Flask
from .database import initialize_database
from .views import bp_list
from .auth import create_login_manager
from .config import get_config
from .models import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config('debug'))

    initialize_database(app)

    for bp in bp_list:
        app.register_blueprint(bp)

    login_manager = create_login_manager(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    return app


app = create_app()
