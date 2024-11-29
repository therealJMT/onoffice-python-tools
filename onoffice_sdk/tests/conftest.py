"""Test configuration and fixtures for the OnOffice SDK."""

import pytest
from onoffice_sdk import OnOfficeClient

@pytest.fixture
def mock_client():
    """Create a mock OnOffice client for testing."""
    return OnOfficeClient(
        token="test_token",
        secret="test_secret"
    )

@pytest.fixture
def mock_estate_response():
    """Sample estate response data for testing."""
    return {
        "data": {
            "records": [
                {
                    "id": "12345",
                    "type": "house",
                    "price": 250000,
                    "location": "Sample City"
                }
            ],
            "total": 1
        },
        "status": {
            "code": 200,
            "message": "Success"
        }
    }
