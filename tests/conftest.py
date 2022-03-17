import pytest
from flask import Flask
from app import my_app


@pytest.fixture()
def app():
    app: Flask = my_app()
    app.config['TESTING'] = True

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def post_keys():
    return ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
