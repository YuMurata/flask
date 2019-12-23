from application.database import db


class ScoredParam(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    image_name = db.Column(db.String(100))

    user_name = db.Column(db.String(100))

    def __init__(self, user_name: str, image_name: str):
        self.user_name = user_name
        self.image_name = image_name
