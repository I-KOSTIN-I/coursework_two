import json
import pprint

from exceptions import DataLayerError

PATH = 'data/data.json'


def get_posts_all():
    """возвращает посты"""
    try:
        with open('data/comments.json', 'r', encoding='utf=8') as file:
            posts = json.load(file)
        return posts

    except (FileNotFoundError, json.JSONDecodeError):
        raise DataLayerError('Что-то не так с файлом')


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя"""
    names = get_posts_all()
    posts_user = []
    name_lower = user_name.lower()

    for name in names:
        poster_name = name['poster_name'].lower()
        if name_lower in poster_name:
            posts_user.append(name)

        return posts_user


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста"""
    commentaries = get_posts_all()
    all_commentaries = []
    for commentary in commentaries:
        if commentary['post_id'] == post_id:
            all_commentaries.append(commentary)

    return all_commentaries


def search_for_posts(query):
    """возвращает список словарей по вхождению query"""
    pass


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post


print(get_post_by_pk(2))
