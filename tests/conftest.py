"""
Pytest configuration and shared fixtures.
"""

import pytest
from onoffice_sdk import OnOfficeClient

@pytest.fixture
def mock_client():
    """
    Returns a test client with dummy credentials.
    """
    return OnOfficeClient(
        token="test_token",
        secret="test_secret"
    )

@pytest.fixture
def mock_response():
    """
    Returns a standard mock response structure.
    """
    return {
        "status": {
            "code": 200,
            "message": "OK"
        },
        "response": {
            "data": []
        }
    }
