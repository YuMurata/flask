from flask_login import LoginManager


def create_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "users.login"  # login_viewのrouteを設定

    return login_manager
