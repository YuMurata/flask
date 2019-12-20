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

        except auth.AuthException as e:
            flash(e, Category.FAILED)
            return render_template('auth/login.html')

        else:
            flash('ログインしました。', Category.SUCCESS)
            return redirect(url_for('index'))


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('auth/signup.html')

    else:
        try:
            auth.signup(request.form)

        except auth.UserExistedEcxeption as e:
            flash(e, Category.FAILED)

        else:
            flash('新規登録に成功しました。', Category.SUCCESS)

        finally:
            return redirect(url_for('index_bp.index'))
