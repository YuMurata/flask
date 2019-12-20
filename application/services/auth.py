from flask_login import login_user
from application.database import db
from application.models.user import User


class AuthException(Exception):
    pass


class NoUserException(AuthException):
    pass


class WrongPasswordException(AuthException):
    pass


class UserExistedEcxeption(AuthException):
    pass


def signup(data: dict) -> User:
    name = data.get('name')
    password = data.get('password')

    user = User.query.filter_by(name).first()
    if user:
        raise UserExistedEcxeption('ユーザーは既に登録されています。')

    new_user = User.from_args(name, password)

    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)

    return user


def login(data: dict) -> User:
    name = data.get('name')
    password = data.get('password')
    remember = True if data.get('remember') else False

    user = User.query.filter_by(name=name).first()

    is_no_user = user is None
    if is_no_user:
        raise NoUserException('ユーザーが存在しません')

    is_wrong_password = not user.check_password(user.password, password)
    if is_wrong_password:
        raise WrongPasswordException('パスワードが間違っています')

    login_user(user, remember=remember)

    return user
