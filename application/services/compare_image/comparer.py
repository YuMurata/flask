from .Tournament.Tournament import Player, Tournament, PlayerGroup
from .ImageEnhancer import generate_random_param_list
from .enhance_encoder import EnhanceEncoder
from .image_path import image_path_dict
from flask import session
from application.models.compare_data import CompareData
from flask_login import current_user
from application.database import db
from sqlalchemy.exc import SQLAlchemyError


class EnhancePlayer(Player):
    def __init__(self, param, encoder: EnhanceEncoder, score: int = 1):
        super().__init__(param, score)
        self.encoder = encoder

    def decode(self):
        return self.encoder.Encode(self.param)


class EnhancePlayerGroup(PlayerGroup):
    def __init__(self, encoder: EnhanceEncoder):
        self.encoder = encoder

    def score_up(self, index: int):
        CompareData.query.filter_by(
            user_name=current_user.name).get(index+1).score_up()

    def get_player(self, index: int) -> EnhancePlayer:
        data = CompareData.query.filter_by(
            user_name=current_user.name).get(index+1).to_dict()

        return EnhancePlayer(data['param'], self.encoder, data['score'])


class ComparerException(Exception):
    pass


class Comparer:
    def __init__(self, image_name: str, tournament: Tournament):
        self.image_name = image_name
        self.tournament = tournament

    @classmethod
    def gen_from_image_name(cls, image_name: str):
        player_num = 100

        try:
            for param in generate_random_param_list(player_num):
                db.session.add(CompareData(current_user.name, param))
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise SQLAlchemyError
        finally:
            db.session.close()

        encoder = EnhanceEncoder(image_path_dict[image_name])
        player_group = EnhancePlayerGroup(encoder)

        current_player_index_list, next_player_index_list = \
            Tournament.make_player_index_list(player_num)
        tournament = \
            Tournament(player_group, current_player_index_list,
                       next_player_index_list)

        return cls(image_name, tournament)

    @classmethod
    def gen_from_dict(cls, session_dict: dict):
        image_name = session_dict['image_name']

        encoder = EnhanceEncoder(image_path_dict[image_name])
        player_group = EnhancePlayerGroup(encoder)

        tournament = \
            Tournament(player_group, session_dict['current_player_index_list'],
                       session_dict['next_player_index_list'])

        return cls(image_name, tournament)

    def to_dict(self) -> dict:
        return {
            'image_name': self.image_name,
            'current_player_index_list': self.tournament.current_player_index_list,
            'next_player_index_list': self.tournament.next_player_index_list,
        }


class ComparerSession:
    component_name = 'comparer'

    @classmethod
    def is_in_session(cls) -> bool:
        return cls.component_name in session

    @classmethod
    def get_from_session(cls) -> Comparer:
        if not cls.is_in_session():
            raise ComparerException

        return Comparer.gen_from_dict(session.get(cls.component_name))

    @classmethod
    def add_in_session(cls, comparer: Comparer):
        session[cls.component_name] = comparer.to_dict()
