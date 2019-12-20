from flask import Blueprint, render_template
from application.models import User

user_list_bp = Blueprint('user_list_bp', __name__)


@user_list_bp.route('/user_list')
def user_list():
    print(User.query().all())
    return 'aho'
