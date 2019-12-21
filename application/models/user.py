from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from application.database import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    max_id_length = 1000
    user_id = db.Column(db.String(max_id_length))

    max_name_length = 1000
    name = db.Column(db.String(max_name_length))

    password = db.Column(db.String(100))

    def __init__(self,user_id:str, name: str, password: str):
        self.user_id = user_id
        self.name = name
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, clean_password):
        return check_password_hash(self.password, clean_password)
