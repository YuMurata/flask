from application.database import db
from application.models.user import User
from .exception import AuthException
from sqlalchemy.exc import SQLAlchemyError
import typing


class SignupException(AuthException):
    pass


def signup(data: dict) -> typing.NoReturn:
    user_id = data.get('user_id')
    name = data.get('name')
    password = data.get('password')

    if not name or not name or not password:
        raise SignupException('空欄があります')

    user = User.query.filter_by(user_id=user_id).first()
    if user:
        raise SignupException('このIDは既に使われています')

    if not user_id.isalnum():
        raise SignupException('ユーザ名は英数字のみにして下さい')

    required_password_length = 8
    if len(password) < required_password_length:
        raise SignupException(
            f'パスワードは {required_password_length} 文字以上にして下さい')

    new_user = User(user_id, name, password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise SQLAlchemyError
    finally:
        db.session.close()
