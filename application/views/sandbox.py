from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user
from application.services.compare_image import image_path_dict, to_base64
import application.services.compare_image.ImageEnhancer as IE
import application.services.compare_image.Tournament.Tournament as Tournament
import application.services.compare_image.DataWriter as DW


sandbox_bp = Blueprint('sandbox_bp', __name__)


class EnhancePlayer(Tournament.Player):
    def __init__(self, param, enhancer: IE.ImageEnhancer):
        super().__init__(param)
        self.enhancer = enhancer

    def decode(self):
        image = self.enhancer.enhance(self.param)
        return to_base64(image)


class Comparer:
    def make_tournament(self, image_name: str):
        self.image_name = image_name
        enhancer = IE.ImageEnhancer(image_path_dict[image_name])
        self.player_list = [EnhancePlayer(param, enhancer)
                            for param in IE.generate_random_param_list(100)]
        self.tournament = Tournament.Tournament(self.player_list)


comparer = Comparer()


@sandbox_bp.route('/image')
def image():
    image_dict_list = [
        {
            'path': 'static/images/'+image_path.name,
            'name': name
        }
        for name, image_path in image_path_dict.items()
    ]
    image_dict_list.extend(image_dict_list)
    return render_template('image.html', image_dict_list=image_dict_list)


@sandbox_bp.route('/select_image', methods=['POST'])
def select_image():
    image_name = request.form['select']

    comparer.make_tournament(image_name)
    count = comparer.tournament.get_match_num
    is_complete, (left_player, right_player) = comparer.tournament.new_match()

    return render_template('compare.html',
                           left_image=left_player.decode(),
                           right_image=right_player.decode(),
                           count=count)


@sandbox_bp.route('/compare_image', methods=['POST'])
def compare():
    keycode = request.form['key']

    keycode_map = {
        'left': Tournament.GameWin.LEFT,
        'right': Tournament.GameWin.RIGHT,
        'both_win': Tournament.GameWin.BOTH_WIN,
        'both_lose': Tournament.GameWin.BOTH_LOSE,
    }

    comparer.tournament.compete(keycode_map[keycode])
    if comparer.tournament.is_complete:
        save_dir_path = DW.root_save_dir_path/current_user.name/comparer.image_name
        save_dir_path.mkdir(parents=True, exist_ok=True)

        save_file_path = str(save_dir_path/f'scored_param{DW.SUFFIX}')
        DW.write(save_file_path, comparer.player_list)

        return jsonify({"is_complete": True})

    count = comparer.tournament.get_match_num
    is_complete, (left_player, right_player) = comparer.tournament.new_match()

    return jsonify({'left_image': left_player.decode(),
                    'right_image': right_player.decode(),
                    "count": count,
                    'is_complete': is_complete})
