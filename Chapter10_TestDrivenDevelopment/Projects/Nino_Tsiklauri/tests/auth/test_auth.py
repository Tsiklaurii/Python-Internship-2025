from flask_login import  current_user

def test_login(client):
    with client:
        client.post("/login", data={"username": "admin", "password": "wrongPass"})
        assert current_user.is_authenticated == False

        client.post("/login", data={"username": "admin", "password": "password123"})
        assert current_user.is_authenticated == True

def test_header_anonymous_user(client):
    response = client.get("/")
    html = response.data

    assert b"Log In" in html
    assert b"Registration" in html
    assert b"Profile" not in html
    assert b"Log out" not in html

def test_header_authenticated_user(client):
    with client:
        client.post("/login", data={"username": "admin", "password": "password123"})

        response = client.get("/")
        html = response.data

        assert b"Log In" not in html
        assert b"Registration" not in html
        assert b"Profile" in html
        assert b"Log Out" in html

def test_login_wrong_password(client):
    response = client.post("/login", data={"username": "admin", "password": "wrongPass"}, follow_redirects=True)
    assert b"Username or Password is incorrect" in response.data
