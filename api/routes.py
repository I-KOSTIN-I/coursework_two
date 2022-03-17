from flask import Blueprint, jsonify
from utils import get_posts_all, get_post_by_pk


api_bp = Blueprint('api', __name__)


@api_bp.route('/posts')
def get_posts():
    posts = get_posts_all()

    return jsonify(posts)


@api_bp.route('/posts/<int:post_id>')
def get_one_post(post_id):
    post = get_post_by_pk(post_id)
    if post is None:
        return {'error': 'Пост не найден'}, 404

    return jsonify(post)




