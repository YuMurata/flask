from flask import Blueprint, render_template, request
from application.services.compare_image import image_path_dict, EnhanceEncoder, ImageEnhancer

sandbox_bp = Blueprint('sandbox_bp', __name__)


@sandbox_bp.route('/sandbox')
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
