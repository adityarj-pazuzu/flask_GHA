"""
This module contains tests for the Flask app.
"""

import pytest
from app import app  # Import the Flask app


@pytest.fixture
def client():
    """
    Fixture to set up the test client for Flask app.
    """
    with app.test_client() as flask_client:
        yield flask_client


def test_hello_world(client):
    """
    Test the '/' route to ensure it returns the correct response.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World"
