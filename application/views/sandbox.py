from flask import Blueprint, render_template
from application.services.compare_image import image_path_dict

sandbox_bp = Blueprint('sandbox_bp', __name__)


@sandbox_bp.route('/sandbox')
def image():
    image_dict_list = [
        {
            'path': 'static/images/'+image_path.name,
            'name': name
        }
        for name, image_path in image_path_dict.items()
    ]
    image_dict_list.extend(image_dict_list[:2])
    n = 4
    image_dict_table = [image_dict_list[idx:idx+n]
                        for idx in range(0, len(image_dict_list), n)]
    print(image_dict_table)

    return render_template('image.html', image_dict_table=image_dict_table)
