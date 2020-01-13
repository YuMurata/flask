from flask import render_template, request, Blueprint, jsonify, abort
from flask_login import login_required
from application.services.compare \
    import (CompareSession, Tournament, DataWriter)
from application.models import ScoredParam
from application.database import db
from flask_login import current_user
from application.error import InternalServerError

compare_bp = Blueprint('compare_bp', __name__)


@compare_bp.route('/select', methods=['POST'])
@login_required
def select():
    image_name = request.form['select']

    if not CompareSession.is_in_session():
        CompareSession.add(image_name)

    comparer = CompareSession.get()
    comparer.tournament = comparer.make_tournament(image_name)

    count = comparer.tournament.get_match_num
    is_complete, (left_player, right_player) = comparer.tournament.new_match()
    CompareSession.commit(comparer)

    return render_template('image/compare.html',
                           left_image=left_player.decode(),
                           right_image=right_player.decode(),
                           count=count)


@compare_bp.route('/compare', methods=['POST'])
@login_required
def compare():
    keycode = request.form['key']

    keycode_map = {
        'left': Tournament.GameWin.LEFT,
        'right': Tournament.GameWin.RIGHT,
        'both_win': Tournament.GameWin.BOTH_WIN,
        'both_lose': Tournament.GameWin.BOTH_LOSE,
    }

    comparer = CompareSession.get()
    comparer.tournament.compete(keycode_map[keycode])

    def save_param():
        save_file_path = \
            str(DataWriter.get_save_file_path(
                current_user.name, comparer.image_name))
        DataWriter.write(save_file_path, comparer.tournament.player_list)

        if not ScoredParam.is_in_database(current_user, comparer.image_name):
            new_param = ScoredParam(current_user, comparer.image_name)

            try:
                db.session.add(new_param)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
                abort(InternalServerError.code)
            finally:
                db.session.close()

    if comparer.tournament.is_complete:
        save_param()
        CompareSession.delete()
        return jsonify({"is_complete": True})

    count = comparer.tournament.get_match_num
    is_complete, (left_player, right_player) = comparer.tournament.new_match()
    if is_complete:
        save_param()
        CompareSession.delete()

    CompareSession.commit(comparer)
    return jsonify({'left_image': left_player.decode(),
                    'right_image': right_player.decode(),
                    "count": count,
                    'is_complete': is_complete})
