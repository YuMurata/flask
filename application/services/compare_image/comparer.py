from .Tournament.Tournament import Player, Tournament
from .ImageEnhancer import generate_random_param_list
from .enhance_encoder import EnhanceEncoder
from .image_path import image_path_dict


class EnhancePlayer(Player):
    def __init__(self, param, encoder: EnhanceEncoder):
        super().__init__(param)
        self.encoder = encoder

    def decode(self):
        return self.encoder.Encode(self.param)


class Comparer:
    def make_tournament(self, image_name: str):
        self.image_name = image_name
        encoder = EnhanceEncoder(image_path_dict[image_name])
        self.player_list = [EnhancePlayer(param, encoder)
                            for param in generate_random_param_list(100)]
        self.tournament = Tournament(self.player_list)


comparer_dict = {}

def get_comparer(user_name):
    return comparer_dict.setdefault(user_name, Comparer())
