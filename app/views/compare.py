from flask import Blueprint, render_template, request, jsonify
from app.process import to_base64, image_path_dict
from PIL import Image

compare_bp = Blueprint('bp', __name__)


@compare_bp.route('/compare', methods=['GET', 'POST'])
def compare():
    if request.method == 'POST':
        key = request.form['key']
        image_path = image_path_dict['giraffe'] if key == 'F' else image_path_dict['heart']
        giraffe = to_base64(Image.open(image_path))
        return jsonify({'left_image': giraffe,
                        'right_image': giraffe,
                        "count": 10})

    heart = to_base64(Image.open(image_path_dict['heart']))
    return render_template('compare.html',
                           left_image=heart,
                           right_image=heart,
                           count=100)
