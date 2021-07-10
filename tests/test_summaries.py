import json

TEST_URL = 'https://foo.bar'


def test_create_summary(test_app_with_db):
    """Test method post for append summaries."""
    response = test_app_with_db.post('/summaries/', data=json.dumps({'url': TEST_URL}))

    assert response.status_code == 201
    assert response.json()['url'] == TEST_URL


def test_create_summaries_invalid_json(test_app):
    """Test bad example post for append summaries."""
    response = test_app.post('/summaries/', data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', 'url'],
                'msg': 'field required',
                'type': 'value_error.missing',
            },
        ],
    }


def test_read_summary(test_app_with_db):
    """Test method get for read summaries."""
    response = test_app_with_db.post('/summaries/', data=json.dumps({'url': TEST_URL}))
    summary_id = response.json()['id']

    response = test_app_with_db.get(f'/summaries/{summary_id}/')
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict['id'] == summary_id
    assert response_dict['url'] == TEST_URL
    assert response_dict['summary']
    assert response_dict['created_at']


def test_read_summary_incorrect_id(test_app_with_db):
    """Test code answer 404."""
    response = test_app_with_db.get('/summaries/999/')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Summary not found'


def test_remove_summary(test_app_with_db):
    """Test method DELETE by url."""
    response = test_app_with_db.post(
        '/summaries/',
        data=json.dumps({'url': TEST_URL}),
    )
    summary_id = response.json()['id']

    response = test_app_with_db.delete(f'/summaries/{summary_id}/')
    assert response.status_code == 200
    assert response.json() == {'id': summary_id, 'url': TEST_URL}


def test_remove_summary_incorrect_id(test_app_with_db):
    """Test method DELETE by id."""
    response = test_app_with_db.delete('/summaries/999/')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Summary not found'
