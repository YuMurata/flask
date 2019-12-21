from flask import Blueprint, render_template, request, flash, redirect, url_for
from application.services import auth

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
            return redirect(url_for('index'))


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
            flash('新規登録に成功しました')
            return redirect(url_for('index_bp.index'))

