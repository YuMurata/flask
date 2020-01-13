from flask import render_template, request, Blueprint, abort
from application.services.compare \
    import (image_path_dict, EnhanceEncoder, DataWriter)
from flask_login import login_required, current_user
from application.error import InternalServerError
import json

scored_data_bp = Blueprint('scored_data_bp', __name__)


@scored_data_bp.route('/scored_image_list', methods=['POST'])
@login_required
def scored_image_list():
    image_name = request.form['select']

    scored_param_path = \
        DataWriter.get_save_file_path(current_user.name, image_name)

    if not scored_param_path.exists():
        abort(InternalServerError.code)

    image_path = image_path_dict[image_name]
    encoder = EnhanceEncoder(image_path)

    with open(str(scored_param_path), 'r') as fp:
        scored_param_dict = {
            scored_param['score']: scored_param['param']
            for scored_param in json.load(fp)
        }

    scored_param_list = \
        sorted(scored_param_dict.items(), key=lambda x: x[0], reverse=True)
    print(scored_param_list)

    image_list = [encoder.Encode(scored_param[1])
                  for scored_param in scored_param_list]

    return render_template('image/scored_param.html',
                           image_list=image_list, image_name=image_name)
