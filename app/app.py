from flask import Flask, render_template
from .views import bp_list
from .database import init_db
from . import models


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_db(app)

    for bp in bp_list:
        app.register_blueprint(bp)

    return app


app = create_app()


@app.route('/')
def hello():
    return 'hello world'


@app.route('/image')
def image():
    return render_template('image.html')


@app.route('/index')
def index():
    html = render_template('index.html')
    return html
