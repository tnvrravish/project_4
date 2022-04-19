def test_request_git_page(application, client):
    """This makes the Git page"""
    response = client.get("/git")
    assert response.status_code == 200


def test_page_not_found(client):
    """This Tests Page Not Fount"""
    response = client.get('/page1')
    assert response.status_code == 404


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/welcome"' in response.data
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index" in response.data


def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/welcome")
    assert response.status_code == 200
    assert b"welcome" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
