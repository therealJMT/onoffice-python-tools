"""
OnOffice API Client

This module provides a simple client for interacting with the OnOffice API using HMAC2 authentication.
It allows you to make authenticated requests to the OnOffice API endpoints with proper security measures.

Requirements:
    - Python 3.6+
    - requests
    - python-dotenv

Example usage:
    from onoffice_api_client import send_onoffice_api_request
    
    # Configure your environment variables in .env file:
    # ONOFFICE_API_TOKEN=your_token
    # ONOFFICE_API_SECRET=your_secret
    
    # Example parameters for retrieving estate data
    parameters = {
        "data": ["Id", "lage", "kaufpreis"],
        "filter": {
            "status": [{"op": "=", "val": 1}],
            "kaufpreis": [{"op": "<", "val": 300000}]
        },
        "listlimit": 100,
        "listoffset": 0,
        "sortby": {"kaufpreis": "ASC"}
    }
    
    result = send_onoffice_api_request(
        token=os.getenv('ONOFFICE_API_TOKEN'),
        secret=os.getenv('ONOFFICE_API_SECRET'),
        resourcetype='estate',
        actionid='urn:onoffice-de-ns:smart:2.5:smartml:action:read',
        parameters=parameters
    )
"""

import os
import hmac
import hashlib
import base64
import requests
import json
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_hmac2(token: str, secret: str, timestamp: int, resourcetype: str, actionid: str) -> str:
    """
    Create HMAC2 signature for OnOffice API authentication.
    
    Args:
        token (str): OnOffice API token
        secret (str): OnOffice API secret
        timestamp (int): Current Unix timestamp
        resourcetype (str): Type of resource being accessed
        actionid (str): ID of the action being performed
    
    Returns:
        str: Base64 encoded HMAC signature
    """
    fields = [str(timestamp), token, resourcetype, actionid]
    message = ''.join(fields)
    key = secret.encode('utf-8')
    msg = message.encode('utf-8')
    digest = hmac.new(key, msg, hashlib.sha256).digest()
    return base64.b64encode(digest).decode('utf-8')

def send_onoffice_api_request(token: str, secret: str, resourcetype: str, actionid: str, parameters: dict) -> dict:
    """
    Send an authenticated request to the OnOffice API.
    
    Args:
        token (str): OnOffice API token
        secret (str): OnOffice API secret
        resourcetype (str): Type of resource being accessed (e.g., 'estate')
        actionid (str): ID of the action being performed
        parameters (dict): Request parameters specific to the action
    
    Returns:
        dict: JSON response from the API
    
    Raises:
        requests.RequestException: If the API request fails
    """
    api_url = 'https://api.onoffice.de/api/stable/api.php'
    timestamp = int(time.time())

    hmac2 = create_hmac2(token, secret, timestamp, resourcetype, actionid)

    action_data = {
        "actionid": actionid,
        "resourceid": "",
        "resourcetype": resourcetype,
        "identifier": "",
        "timestamp": timestamp,
        "hmac": hmac2,
        "hmac_version": "2",
        "parameters": parameters
    }

    request_data = {
        "token": token,
        "request": {
            "actions": [action_data]
        }
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(api_url, json=request_data, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    """
    Example usage of the OnOffice API client.
    """
    # Get token and secret from environment variables
    token = os.getenv('ONOFFICE_API_TOKEN')
    secret = os.getenv('ONOFFICE_API_SECRET')

    # Check if token and secret are set
    if not token or not secret:
        print("Error: API token and secret must be set in .env file")
        print("Create a .env file with:")
        print("ONOFFICE_API_TOKEN=your_token")
        print("ONOFFICE_API_SECRET=your_secret")
        return

    # Example request to get estate data
    resourcetype = 'estate'
    actionid = 'urn:onoffice-de-ns:smart:2.5:smartml:action:read'

    parameters = {
        "data": ["Id", "lage", "kaufpreis"],
        "filter": {
            "status": [{"op": "=", "val": 1}],
            "kaufpreis": [{"op": "<", "val": 300000}]
        },
        "listlimit": 100,
        "listoffset": 0,
        "sortby": {"kaufpreis": "ASC"}
    }

    try:
        result = send_onoffice_api_request(token, secret, resourcetype, actionid, parameters)
        print("API Response:")
        print(json.dumps(result, indent=2))
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
