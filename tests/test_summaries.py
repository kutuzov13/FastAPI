import json

from status_code import (
    CREATE_CODE,
    NOT_FOUND_CODE,
    SUCCESSFUL_CODE,
    UNPROCESSABLE_CODE,
)

TEST_URL = 'https://foo.bar'


def test_create_summary(test_app_with_db):
    """Test method post for append summaries."""
    response = test_app_with_db.post('/summaries/', data=json.dumps({'url': TEST_URL}))

    assert response.status_code == CREATE_CODE
    assert response.json()['url'] == TEST_URL


def test_create_summaries_invalid_json(test_app):
    """Test bad example post for append summaries."""
    response = test_app.post('/summaries/', data=json.dumps({}))
    assert response.status_code == UNPROCESSABLE_CODE
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
    assert response.status_code == SUCCESSFUL_CODE

    response_dict = response.json()
    assert response_dict['id'] == summary_id
    assert response_dict['url'] == TEST_URL
    assert response_dict['summary']
    assert response_dict['created_at']


def test_read_summary_incorrect_id(test_app_with_db):
    """Test code answer 404."""
    response = test_app_with_db.get('/summaries/999/')
    assert response.status_code == NOT_FOUND_CODE
    assert response.json()['detail'] == 'Summary not found'
