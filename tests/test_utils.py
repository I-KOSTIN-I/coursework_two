import pytest
from flask import url_for

import utils


def tests_posts(client):
    posts = utils.get_posts_all()
    assert isinstance(posts, list)


def test_file():
    with pytest.raises(FileNotFoundError) as exc:
        utils.get_json_data("wrong")


def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b"SKYPROGRAM" in resp.data


@pytest.mark.parametrize('word, count', [('еда', 1), ('еда', 1)])
def test_search(client, word, count):
    # word = 'еда'
    # count = len(utils.search_for_posts(word))

    resp = client.get(f'/search/?s={word}')
    assert resp.status_code == 200
    assert f"Найдено постов: {count}" in resp.data.decode('utf-8')


def test_post(client):

    resp = client.get('/post/1')
    assert resp.status_code == 200
    assert b"leo" in resp.data


def test_get_user_post(client):

    resp = client.get('/users/hank')
    assert resp.status_code == 200
    assert b"hank" in resp.data