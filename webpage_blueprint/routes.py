from flask import Blueprint, render_template

webpage = Blueprint('webpage', __name__)


@webpage.route('/')
def index():
    return render_template('index.html')
