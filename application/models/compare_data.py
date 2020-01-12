from application.database import db
from sqlalchemy.exc import SQLAlchemyError


class CompareData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), primary_key=True)

    score = db.Column(db.Integer)
    brightness = db.Column(db.Float)
    saturation = db.Column(db.Float)
    contrast = db.Column(db.Float)
    sharpness = db.Column(db.Float)

    def __init__(self, user_name: str, param: dict):
        self.user_name = user_name

        self.brightness = param['brightness']
        self.saturation = param['saturation']
        self.contrast = param['contrast']
        self.sharpness = param['sharpness']

        self.score = 1

    def score_up(self):
        self.score *= 2

        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise SQLAlchemyError
        finally:
            db.session.close()

    def to_dict(self):
        return {
            'param': {
                'brightness': self.brightness,
                'saturation': self.saturation,
                'contrast': self.contrast,
                'sharpness': self.sharpness,
            },
            'score': self.score
        }
