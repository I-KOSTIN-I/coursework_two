from flask import Blueprint, render_template, request

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
def search_page():
    s = request.args.get('s', '')
    search_info = utils.search_for_posts(s)

    return render_template('search.html', search_info=search_info, s=s)


@webpage.route('/users/<username>')
def get_user_post():
    s = request.args.get('s', '')
    search_users = utils.get_posts_by_user(s)
    return render_template('user-feed.html', search_users=search_users, s=s)

