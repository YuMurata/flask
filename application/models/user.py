from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from application.database import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))

    @classmethod
    def from_args(cls, name: str, password: str):
        instance = cls()
        instance.name = name

        if password is not None:
            instance.hash_password(password)

        return instance

    def hash_password(self, clean_password):
        self.password = generate_password_hash(
            str(clean_password), method='sha256')

    def check_password(self, clean_password):
        return check_password_hash(self.password, clean_password)
