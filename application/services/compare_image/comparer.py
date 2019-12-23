from .Tournament.Tournament import Player, Tournament
from .ImageEnhancer import ImageEnhancer, generate_random_param_list
import io
import base64
from .image_path import image_path_dict


class EnhancePlayer(Player):
    def __init__(self, param, enhancer: ImageEnhancer):
        super().__init__(param)
        self.enhancer = enhancer

    def decode(self):
        image = self.enhancer.enhance(self.param)

        output = io.BytesIO()
        image.save(output, format='PNG')

        base64_image = base64.b64encode(
            output.getvalue()).decode().replace("'", "")

        return 'data:image/png;base64,'+base64_image


class Comparer:
    def make_tournament(self, image_name: str):
        self.image_name = image_name
        enhancer = ImageEnhancer(image_path_dict[image_name])
        self.player_list = [EnhancePlayer(param, enhancer)
                            for param in generate_random_param_list(100)]
        self.tournament = Tournament(self.player_list)


comparer = Comparer()
