from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from .Tournament import Tournament
from .comparer import comparer
from .DataWriter import root_save_dir_path, write, SUFFIX
from application.models import ScoredParam
from application.database import db
from sqlalchemy.exc import SQLAlchemyError

compare_bp = Blueprint('compare_bp', __name__)


@compare_bp.route('/compare_image', methods=['POST'])
@login_required
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
        _save_param()
        return jsonify({"is_complete": True})

    count = comparer.tournament.get_match_num
    is_complete, (left_player, right_player) = comparer.tournament.new_match()
    if is_complete:
        _save_param()

    return jsonify({'left_image': left_player.decode(),
                    'right_image': right_player.decode(),
                    "count": count,
                    'is_complete': is_complete})


def _save_param():
    save_dir_path = \
        root_save_dir_path/current_user.name/comparer.image_name
    save_dir_path.mkdir(parents=True, exist_ok=True)

    save_file_path = str(save_dir_path/f'scored_param{SUFFIX}')
    write(save_file_path, comparer.player_list)

    new_param = ScoredParam(current_user.name, comparer.image_name)

    try:
        db.session.add(new_param)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise SQLAlchemyError
    finally:
        db.session.close()
