from flask import Blueprint, render_template, request
from pathlib import Path
from application.services.compare_image import image_path_dict, to_base64
from PIL import Image


sandbox_bp = Blueprint('sandbox_bp', __name__)

image_dict_list = [
    {
        'path': 'static/images/'+image_path.name,
        'name': name
    }
    for name, image_path in image_path_dict.items()
]


@sandbox_bp.route('/image')
def image():
    # image_dict_list.extend(image_dict_list)
    print(image_dict_list)
    return render_template('image.html', image_dict_list=image_dict_list)


@sandbox_bp.route('/select_image', methods=['POST'])
def select_image():
    name = request.form['select']

    image = Image.open(image_path_dict[name]).convert('RGB')

    return render_template('compare.html',
                           left_image=to_base64(image),
                           right_image=to_base64(image),
                           count=100)

