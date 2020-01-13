from application.database import db


class CompareData(db.Model):
    __tablename__ = 'compare_data'

    id = db.Column(db.Integer, primary_key=True)
    user_id = \
        db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=__tablename__)

    image_name = db.Column(db.String(100))
    tournament = db.Column(db.LargeBinary(length=2**18))

    def __init__(self, user, image_name: str, tournament):
        self.user = user
        self.image_name = image_name
        self.tournament = tournament
