from flask import Blueprint, render_template, request, flash, redirect, url_for
from application.services import auth
from flask_login import login_required, logout_user

auth_bp = Blueprint('auth_bp', __name__)


class Category:
    SUCCESS = 'success'
    FAILED = 'failed'


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')

    else:
        try:
            auth.login(request.form)

        except auth.LoginException as e:
            flash(e)
            return render_template('auth/login.html')

        else:
            flash('ログインしました')
            return redirect(url_for('index_bp.index'))


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('auth/signup.html')

    else:
        try:
            auth.signup(request.form)

        except auth.SignupException as e:
            flash(str(e))
            return redirect(url_for('auth_bp.signup'))

        else:
            return redirect(url_for('index_bp.index'))


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index_bp.index'))
