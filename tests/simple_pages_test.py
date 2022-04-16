
def test_request_home_page(application,client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'Home' in response.data
    assert b'Git/GitHub' in response.data

def test_request_git_page(application,client):
    """This makes the Git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b'Home' in response.data
    assert b'Git/GitHub' in response.data

def test_page_not_found(client):
    """This Tests Page Not Fount"""
    response = client.get('/page1')
    assert response.status_code == 404
