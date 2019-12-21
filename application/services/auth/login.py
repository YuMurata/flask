from .exception import AuthException
from application.models import User
import typing
from flask_login import login_user


class LoginException(AuthException):
    pass


def login(data: dict) -> typing.NoReturn:
    user_id = data.get('user_id')
    password = data.get('password')
    remember = True if data.get('remember') else False

    if not user_id or not password:
        raise LoginException('空欄があります')

    user = User.query.filter_by(user_id=user_id).first()

    is_no_user = user is None
    if is_no_user:
        raise LoginException('ユーザーが存在しません')

    is_wrong_password = not user.check_password(password)
    if is_wrong_password:
        raise LoginException('パスワードが間違っています')

    login_user(user, remember=remember)
