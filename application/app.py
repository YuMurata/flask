from flask import Flask, render_template
from .views import bp_list
from .database import init_db
from .auth import create_login_manager
from . import models





@app.route('/image')
def image():
    return render_template('image.html')
