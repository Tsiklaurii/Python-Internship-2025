def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_404_page(client):
    response = client.get('/unknown')
    assert response.status_code == 404
    assert b"Not Found" in response.data

def test_index_content(client):
    response = client.get('/about')
    assert b"There is no friend as loyal as a book." in response.data