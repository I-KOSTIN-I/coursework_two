from flask import Blueprint, render_template
import utils

webpage = Blueprint('webpage', __name__)


@webpage.route('/')
def index():
    return render_template('index.html')


@webpage.route('/post/<int:post_id>')
def get_post(post_id):
    post = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_by_post_id(post_id)

    return render_template('post.html', post=post, comments=comments)


@webpage.route('/search/', methods=['GET'])
def seach():
    pass
