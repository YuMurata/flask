from flask import render_template, request
from flask_login import login_required
from application.services.compare_image import image_path_dict
from application.services.compare_image import compare_bp, Comparer, ComparerSession


@compare_bp.route('/image')
@login_required
def image():
    image_dict_list = [
        {
            'path': 'static/images/'+image_path.name,
            'name': name,
            'is_compared': True
        }
        for name, image_path in image_path_dict.items()
    ]
    n = 4
    image_dict_table = [image_dict_list[idx:idx+n]
                        for idx in range(0, len(image_dict_list), n)]

    return render_template('image/image_list.html',
                           image_dict_table=image_dict_table)


@compare_bp.route('/select_image', methods=['POST'])
@login_required
def select_image():
    image_name = request.form['select']

    if not ComparerSession.is_in_session():
        ComparerSession.add_in_session(
            Comparer.gen_from_image_name(image_name))

    comparer = ComparerSession.get_from_session()
    count = comparer.tournament.get_match_num
    is_complete, (left_player, right_player) = comparer.tournament.new_match()

    return render_template('image/compare.html',
                           left_image=left_player.decode(),
                           right_image=right_player.decode(),
                           count=count)
