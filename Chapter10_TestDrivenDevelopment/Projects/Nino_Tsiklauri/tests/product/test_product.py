def test_add_product_unauthorized(client):
    response = client.get('/add_product', follow_redirects=True)
    assert response.request.path == "/"

def test_add_product(client):
    with client:
        client.post("/login", data={"username": "admin", "password": "password123"})

        response = client.get('/add_product', follow_redirects=True)
        assert b"Create Product" in response.data

def test_add_product(client):
    with client:
        client.post("/login", data={"username": "admin", "password": "password123"})

        response = client.get('/', follow_redirects=True)
        assert b"Add New Product" in response.data
        assert b"Edit" in response.data
        assert b"Delete" in response.data