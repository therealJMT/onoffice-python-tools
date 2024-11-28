"""
Tests for the OnOffice SDK client.
"""

import pytest
from onoffice_sdk import OnOfficeClient

def test_sdk_import():
    """Test that we can import the SDK."""
    assert OnOfficeClient is not None

def test_client_initialization():
    """Test basic client initialization."""
    client = OnOfficeClient(token="test_token", secret="test_secret")
    assert client.token == "test_token"
    assert client.secret == "test_secret"

def test_estate_search(requests_mock):
    """Test estate search with a mocked API response."""
    client = OnOfficeClient(token="test_token", secret="test_secret")
    
    mock_response = {
        "status": {
            "code": 200,
            "message": "OK"
        },
        "response": {
            "data": [
                {"id": 1, "kaufpreis": 250000}
            ]
        }
    }
    requests_mock.post("https://api.onoffice.de/api/stable/api.php", json=mock_response)
    
    results = client.estate.search(
        filters={"kaufpreis": [{"op": "<", "val": 300000}]},
        fields=["Id", "kaufpreis"]
    )
    
    assert isinstance(results, dict)
    assert results["status"]["code"] == 200
    assert len(results["response"]["data"]) == 1
    assert results["response"]["data"][0]["kaufpreis"] == 250000

def test_estate_create(requests_mock):
    """Test estate creation."""
    client = OnOfficeClient(token="test_token", secret="test_secret")
    
    mock_response = {
        "status": {
            "code": 200,
            "message": "OK"
        },
        "response": {
            "data": {
                "id": 123
            }
        }
    }
    requests_mock.post("https://api.onoffice.de/api/stable/api.php", json=mock_response)
    
    estate_data = {
        "objektart": "haus",
        "kaufpreis": 250000,
        "lage": "Berlin"
    }
    result = client.estate.create(estate_data)
    
    assert result["status"]["code"] == 200
    assert result["response"]["data"]["id"] == 123

def test_estate_update(requests_mock):
    """Test estate update."""
    client = OnOfficeClient(token="test_token", secret="test_secret")
    
    mock_response = {
        "status": {
            "code": 200,
            "message": "OK"
        },
        "response": {
            "success": True
        }
    }
    requests_mock.post("https://api.onoffice.de/api/stable/api.php", json=mock_response)
    
    result = client.estate.update(123, {"kaufpreis": 260000})
    
    assert result["status"]["code"] == 200
    assert result["response"]["success"] is True

def test_estate_delete(requests_mock):
    """Test estate deletion."""
    client = OnOfficeClient(token="test_token", secret="test_secret")
    
    mock_response = {
        "status": {
            "code": 200,
            "message": "OK"
        },
        "response": {
            "success": True
        }
    }
    requests_mock.post("https://api.onoffice.de/api/stable/api.php", json=mock_response)
    
    result = client.estate.delete(123)
    
    assert result["status"]["code"] == 200
    assert result["response"]["success"] is True

def test_estate_get(requests_mock):
    """Test getting a single estate."""
    client = OnOfficeClient(token="test_token", secret="test_secret")
    
    mock_response = {
        "status": {
            "code": 200,
            "message": "OK"
        },
        "response": {
            "data": [
                {
                    "id": 123,
                    "kaufpreis": 250000,
                    "lage": "Berlin"
                }
            ]
        }
    }
    requests_mock.post("https://api.onoffice.de/api/stable/api.php", json=mock_response)
    
    result = client.estate.get(123, fields=["Id", "kaufpreis", "lage"])
    
    assert result["status"]["code"] == 200
    assert result["response"]["data"][0]["id"] == 123
    assert result["response"]["data"][0]["kaufpreis"] == 250000
    assert result["response"]["data"][0]["lage"] == "Berlin"
