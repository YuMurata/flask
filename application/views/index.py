from flask import Blueprint, render_template
from flask_login import current_user

index_bp = Blueprint('index_bp', __name__)


@index_bp.route('/')
def index():
    html = render_template('index.html')
    return html


@index_bp.route('/profile')
def profile():
    return render_template('auth/profile.html', name=current_user.name)
