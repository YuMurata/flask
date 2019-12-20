from flask import Blueprint, render_template

index_bp = Blueprint('index_bp', __name__)


@index_bp.route('/')
def index():
    html = render_template('index.html')
    return html
