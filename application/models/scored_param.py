from application.database import db


class ScoredParam(db.Model):
    __tablename__ = 'scored_param'

    id = db.Column(db.Integer, primary_key=True)

    image_name = db.Column(db.String(100))

    user_id = \
        db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=__tablename__)

    def __init__(self, user, image_name: str):
        self.user = user
        self.image_name = image_name
