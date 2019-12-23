from flask import render_template, request
from flask_login import login_required
from application.services.compare_image import image_path_dict
from application.services.compare_image import compare_bp, comparer


@compare_bp.route('/image')
@login_required
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


@compare_bp.route('/select_image', methods=['POST'])
@login_required
def select_image():
    image_name = request.form['select']

    comparer.make_tournament(image_name)
    count = comparer.tournament.get_match_num
    is_complete, (left_player, right_player) = comparer.tournament.new_match()

    return render_template('compare.html',
                           left_image=left_player.decode(),
                           right_image=right_player.decode(),
                           count=count)
