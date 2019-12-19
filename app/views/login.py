from flask import Blueprint, render_template

login_bp = Blueprint('login_bp', __name__)


@login_bp.route('/login')
def login():
    return render_template('login/login.html')


@login_bp.route('/registar')
def registar():
    return render_template('login/registar.html')
