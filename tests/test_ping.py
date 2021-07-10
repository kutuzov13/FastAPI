from status_code import SUCCESSFUL_CODE


def test_ping(test_app):
    """Test main url /ping."""
    response = test_app.get('/ping')
    assert response.status_code == SUCCESSFUL_CODE
    assert response.json() == {'environment': 'dev', 'ping': 'pong', 'testing': True}
