"""Tests for the OnOffice client."""

import pytest
import requests_mock
from onoffice_sdk import OnOfficeClient
from onoffice_sdk.exceptions import OnOfficeAuthError

def test_client_initialization():
    """Test basic client initialization."""
    client = OnOfficeClient(token="test", secret="test")
    assert client.token == "test"
    assert client.secret == "test"

def test_client_missing_credentials():
    """Test client initialization with missing credentials."""
    with pytest.raises(ValueError):
        OnOfficeClient(token="", secret="test")
    with pytest.raises(ValueError):
        OnOfficeClient(token="test", secret="")

@pytest.mark.asyncio
async def test_estate_search(mock_client, mock_estate_response):
    """Test estate search functionality."""
    with requests_mock.Mocker() as m:
        m.post("https://api.onoffice.de/api/v1", json=mock_estate_response)
        
        result = await mock_client.estate.search(
            filters={"type": [{"op": "=", "val": "house"}]},
            fields=["id", "type", "price", "location"]
        )
        
        assert result["data"]["records"][0]["id"] == "12345"
        assert result["data"]["records"][0]["type"] == "house"
