from flask import render_template, request
from flask_login import login_required
from application.services.compare_image import image_path_dict
from application.services.compare_image import compare_bp, CompareSession


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

    if not CompareSession.is_in_session():
        CompareSession.add(image_name)

    comparer = CompareSession.get()
    if comparer.image_name != image_name:
        comparer.tournament = comparer.make_tournament(image_name)

    count = comparer.tournament.get_match_num
    is_complete, (left_player, right_player) = comparer.tournament.new_match()
    CompareSession.commit(comparer)

    after_player = CompareSession.get().tournament.current_player_index_list
    print('before:', comparer.tournament.current_player_index_list)
    print('after: ', after_player)

    return render_template('image/compare.html',
                           left_image=left_player.decode(),
                           right_image=right_player.decode(),
                           count=count)
