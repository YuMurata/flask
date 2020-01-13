from .Tournament.Tournament import Player, Tournament
from .ImageEnhancer import generate_random_param_list
from .enhance_encoder import EnhanceEncoder
from .image_path import image_path_dict
from flask_login import current_user
from application.database import db
from application.models.compare_data import CompareData
from sqlalchemy.exc import SQLAlchemyError


class EnhancePlayer(Player):
    def __init__(self, param, encoder: EnhanceEncoder, score: int = 1):
        super().__init__(param, score)
        self.encoder = encoder

    def decode(self):
        return self.encoder.Encode(self.param)


class ComparerException(Exception):
    pass


class Comparer:
    def __init__(self, image_name: str, tournament: Tournament):
        self.image_name = image_name
        self.tournament = tournament

    @classmethod
    def make_tournament(cls, image_name: str) -> Tournament:
        player_num = 100
        encoder = EnhanceEncoder(image_path_dict[image_name])
        player_list = \
            [EnhancePlayer(param, encoder)
             for param in generate_random_param_list(player_num)]

        return Tournament(player_list)


class CompareSession:
    @classmethod
    def is_in_session(cls) -> bool:
        data = CompareData.query.filter_by(user=current_user).first()
        return data is not None

    @classmethod
    def get(cls) -> Comparer:
        if not cls.is_in_session():
            raise ComparerException

        data = CompareData.query.filter_by(user=current_user).first()
        return Comparer(data.image_name, data.tournament)

    @classmethod
    def add(cls, image_name: str):
        tournament = Comparer.make_tournament(image_name)
        compare_data = CompareData(current_user, image_name, tournament)

        try:
            db.session.add(compare_data)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise SQLAlchemyError
        finally:
            db.session.close()

    @classmethod
    def commit(cls, comparer: Comparer):
        compare_data = CompareData.query.filter_by(user=current_user).first()
        compare_data.image_name = comparer.image_name
        compare_data.tournament = comparer.tournament

        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise SQLAlchemyError
        finally:
            db.session.close()

    @classmethod
    def delete(cls):
        data = CompareData.query.filter_by(user=current_user).first()

        try:
            db.session.delete(data)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise SQLAlchemyError
        finally:
            db.session.close()
