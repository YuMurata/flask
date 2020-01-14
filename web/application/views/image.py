from flask import render_template, Blueprint
from flask_login import login_required
from application.models import ScoredParam
from application.services.compare import image_path_dict
from flask_login import current_user


image_bp = Blueprint('image_bp', __name__)


@image_bp.route('/image_list')
@login_required
def image_list():
    image_dict_list = [
        {
            'path': 'static/images/'+image_path.name,
            'name': name,
            'is_compared': ScoredParam.is_in_database(current_user, name)
        }
        for name, image_path in image_path_dict.items()
    ]
    n = 4
    image_dict_table = [image_dict_list[idx:idx+n]
                        for idx in range(0, len(image_dict_list), n)]

    return render_template('image/image_list.html',
                           image_dict_table=image_dict_table)
