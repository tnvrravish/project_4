


def test_request_git_page(application,client):
    """This makes the Git page"""
    response = client.get("/git")
    assert response.status_code == 200


def test_page_not_found(client):
    """This Tests Page Not Fount"""
    response = client.get('/page1')
    assert response.status_code == 404
