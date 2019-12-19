from flask import Flask, render_template
from .views import bp_list

app = Flask(__name__)
for bp in bp_list:
    app.register_blueprint(bp)


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
