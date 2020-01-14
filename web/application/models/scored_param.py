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

    @classmethod
    def is_in_database(cls, user, image_name: str):
        data = cls.query.filter_by(user=user, image_name=image_name).first()
        return data is not None
