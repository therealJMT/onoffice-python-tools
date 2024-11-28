"""
OnOffice API Client

Main client class for interacting with the OnOffice API.
"""

import time
import hmac
import hashlib
import base64
from typing import Dict, List, Any, Optional
import requests
from .exceptions import AuthenticationError, RateLimitError, ValidationError, OnOfficeAPIError

class OnOfficeClient:
    """
    Main client class for interacting with the OnOffice API.
    
    Args:
        token (str): Your OnOffice API token
        secret (str): Your OnOffice API secret
        api_version (str, optional): API version to use. Defaults to 'stable'.
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
    
    Examples:
        >>> client = OnOfficeClient(token="your_token", secret="your_secret")
        >>> estates = client.estate.search(filters={"status": [{"op": "=", "val": 1}]})
    """
    
    API_BASE_URL = 'https://api.onoffice.de/api/{version}/api.php'
    
    def __init__(
        self,
        token: str,
        secret: str,
        api_version: str = 'stable',
        timeout: int = 30
    ):
        self.token = token
        self.secret = secret
        self.api_version = api_version
        self.timeout = timeout
        self.session = requests.Session()
        
        # Initialize resource handlers
        self._estate = None
        self._address = None
    
    def _create_hmac2(
        self,
        timestamp: int,
        resource_type: str,
        action_id: str
    ) -> str:
        """
        Create HMAC2 signature for API authentication.
        
        Args:
            timestamp (int): Current Unix timestamp
            resource_type (str): Type of resource being accessed
            action_id (str): ID of the action being performed
            
        Returns:
            str: Base64 encoded HMAC signature
        """
        fields = [str(timestamp), self.token, resource_type, action_id]
        message = ''.join(fields)
        key = self.secret.encode('utf-8')
        msg = message.encode('utf-8')
        digest = hmac.new(key, msg, hashlib.sha256).digest()
        return base64.b64encode(digest).decode('utf-8')
    
    def _make_request(
        self,
        resource_type: str,
        action_id: str,
        parameters: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Make a request to the OnOffice API.
        
        Args:
            resource_type (str): Type of resource being accessed
            action_id (str): ID of the action being performed
            parameters (dict): Request parameters
            
        Returns:
            dict: API response
            
        Raises:
            AuthenticationError: If authentication fails
            RateLimitError: If rate limit is exceeded
            ValidationError: If request validation fails
            OnOfficeAPIError: For other API errors
        """
        timestamp = int(time.time())
        hmac2 = self._create_hmac2(timestamp, resource_type, action_id)
        
        action_data = {
            "actionid": action_id,
            "resourceid": "",
            "resourcetype": resource_type,
            "identifier": "",
            "timestamp": timestamp,
            "hmac": hmac2,
            "hmac_version": "2",
            "parameters": parameters
        }
        
        request_data = {
            "token": self.token,
            "request": {
                "actions": [action_data]
            }
        }
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        try:
            response = self.session.post(
                self.API_BASE_URL.format(version=self.api_version),
                json=request_data,
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            
            # Check for API errors
            if data.get('status', {}).get('code') != 200:
                error = data.get('status', {})
                if error.get('code') == 401:
                    raise AuthenticationError("Authentication failed", response=data)
                elif error.get('code') == 429:
                    raise RateLimitError(
                        "Rate limit exceeded",
                        reset_time=error.get('reset_time')
                    )
                elif error.get('code') == 400:
                    raise ValidationError("Validation failed", errors=error.get('errors'))
                else:
                    raise OnOfficeAPIError(
                        f"API error: {error.get('message')}",
                        response=data
                    )
            
            return data
            
        except requests.exceptions.RequestException as e:
            raise OnOfficeAPIError(f"Request failed: {str(e)}")
    
    @property
    def estate(self) -> 'EstateResource':
        """Get the estate resource handler."""
        if self._estate is None:
            from .resources.estate import EstateResource
            self._estate = EstateResource(self)
        return self._estate
    
    @property
    def address(self) -> 'AddressResource':
        """Get the address resource handler."""
        if self._address is None:
            from .resources.address import AddressResource
            self._address = AddressResource(self)
        return self._address
