from flask import Blueprint, render_template, request
from application.services.compare_image import image_path_dict, EnhanceEncoder
from application.services.compare_image import ImageEnhancer, ComparerSession, Comparer

sandbox_bp = Blueprint('sandbox_bp', __name__)


@sandbox_bp.route('/sandbox')
def index():
    return 'sandbox'


@sandbox_bp.route('/sandbox_1')
def data():
    image_dict_list = [
        {
            'path': 'static/images/'+image_path.name,
            'name': name,
            'is_compared': True
        }
        for name, image_path in image_path_dict.items()
    ]
    image_dict_list[0]['is_compared'] = False
    n = 4
    image_dict_table = [image_dict_list[idx:idx+n]
                        for idx in range(0, len(image_dict_list), n)]

    return render_template('image/data.html', image_dict_table=image_dict_table)


@sandbox_bp.route('/sandbox_2', methods=['POST'])
def scored_param():
    image_name = request.form['select']

    image_path = image_path_dict[image_name]
    encoder = EnhanceEncoder(image_path)
    param_list = ImageEnhancer.generate_random_param_list(14)

    image_list = [encoder.Encode(param) for param in param_list]

    return render_template('image/scored_param.html', image_list=image_list)


@sandbox_bp.route('/sandbox_3')
def comparer():
    image_name = 'flower'

    if not ComparerSession.is_in_session():
        ComparerSession.add_in_session(Comparer.gen_from_image_name(image_name))

    comparer = ComparerSession.get_from_session()
    count = comparer.tournament.get_match_num
    is_complete, (left_player, right_player) = comparer.tournament.new_match()

    return render_template('image/compare.html',
                           left_image=left_player.decode(),
                           right_image=right_player.decode(),
                           count=count)
