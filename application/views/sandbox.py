from flask import Blueprint, render_template, request
from application.models import User
from pathlib import Path
sandbox_bp = Blueprint('sandbox_bp', __name__)


images_dir_path = Path(r'./application/static/images')
image_dict_list = [
    {
        'path': 'static/images/'+image_path.name,
        'name': image_path.stem
    }
    for image_path in images_dir_path.iterdir()
]

@sandbox_bp.route('/image')
def image():
    image_dict_list.extend(image_dict_list)
    print(image_dict_list)
    return render_template('image.html', image_dict_list=image_dict_list)


@sandbox_bp.route('/select_image', methods=['POST'])
def select_image():
    return request.form['select']