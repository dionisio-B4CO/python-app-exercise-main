def test_fetch_todos_endpoint(client):
    """
    Test the '/api/fetch_todos' endpoint.

    This test checks if the endpoint returns a response with a 200 status code
    and whether the expected message is present in the JSON response.

    Args:
        client: Flask test client.

    Returns:
        None
    """

    response = client.get('/api/fetch_todos')
    assert response.status_code == 200

    expected_message = 'TODOs fetched and saved!'
    assert response.json['message'] == expected_message
