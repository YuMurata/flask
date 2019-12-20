from flask import Flask
from application.database import initialize_database
from application.views import bp_list
from application.auth import create_login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object('application.config.Config')

    initialize_database(app)

    for bp in bp_list:
        app.register_blueprint(bp)

    return app


app = create_app()
login_manager = create_login_manager(app)
