import json
import pprint

from exceptions import DataLayerError

PATH_DATA = 'data/data.json'
PATH_COMMENTS = 'data/comments.json'


def get_json_data(path):
    with open(path) as file:
        return json.load(file)


def get_posts_all():
    """возвращает посты"""
    try:
        posts = get_json_data(PATH_DATA)
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
    commentaries = get_json_data(PATH_COMMENTS)
    all_commentaries = []
    for commentary in commentaries:
        if commentary['post_id'] == post_id:
            all_commentaries.append(commentary)

    return all_commentaries


def search_for_posts(query):
    """возвращает список словарей по вхождению query"""
    posts = get_json_data(PATH_DATA)
    found_content = []
    for post in posts:
        if query.lower() in post['content'].lower():
            found_content.append(post)

    return found_content


    pass


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    posts = get_json_data(PATH_DATA)
    found_post = None
    for post in posts:
        if post['pk'] == pk:
            found_post = post
            break
    return found_post


#print(get_post_by_pk(2))
#print(get_comments_by_post_id(4))
#print(search_for_posts('ничего'))
