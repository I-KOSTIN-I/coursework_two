def tests_get_posts(client, post_keys):
    response = client.get('/api/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list)

    for key in response.json:
        if set(key.keys()) != set(post_keys):
            assert False

    assert True


def tests_get_one_post_no_exist(client):
    response = client.get('/api/posts/12345')
    assert response.status_code == 404
    assert response.json == {'error': 'Пост не найден'}
