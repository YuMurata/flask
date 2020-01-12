from application.database import db


class CompareData(db.Model):
    __tablename__ = 'compare_data'

    id = db.Column(db.Integer, primary_key=True)
    user_id = \
        db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=__tablename__)

    image_name = db.Column(db.String)
    tournament = db.Column(db.PickleType)

    def __init__(self, user, image_name: str, tournament):
        self.user = user
        self.image_name = image_name
        self.tournament = tournament
