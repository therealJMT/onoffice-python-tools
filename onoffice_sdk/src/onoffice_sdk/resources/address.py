"""
Address resource handler for the OnOffice API.
"""

from typing import Dict, List, Any, Optional

class AddressResource:
    """
    Handler for address-related API endpoints.
    """
    
    def __init__(self, client):
        self.client = client
    
    def search(
        self,
        filters: Optional[Dict[str, List[Dict[str, Any]]]] = None,
        fields: Optional[List[str]] = None,
        limit: int = 100,
        offset: int = 0,
        sort_by: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Search for addresses with given filters.
        
        Args:
            filters (dict, optional): Search filters
            fields (list, optional): Fields to return
            limit (int, optional): Maximum number of results. Defaults to 100
            offset (int, optional): Number of results to skip. Defaults to 0
            sort_by (dict, optional): Sorting criteria
            
        Returns:
            dict: Search results
        """
        fields = fields or ["Id", "Vorname", "Name", "Email"]
        parameters = {
            "data": fields,
            "listlimit": limit,
            "listoffset": offset,
        }
        
        if filters:
            parameters["filter"] = filters
            
        if sort_by:
            parameters["sortby"] = sort_by
        
        return self.client._make_request(
            resource_type="address",
            action_id="urn:onoffice-de-ns:smart:2.5:smartml:action:read",
            parameters=parameters
        )
    
    def get(self, address_id: int, fields: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Get a single address by ID.
        
        Args:
            address_id (int): Address ID
            fields (list, optional): Fields to return
            
        Returns:
            dict: Address details
        """
        fields = fields or ["Id", "Vorname", "Name", "Email"]
        parameters = {
            "data": fields,
            "filter": {
                "Id": [{"op": "=", "val": address_id}]
            }
        }
        
        return self.client._make_request(
            resource_type="address",
            action_id="urn:onoffice-de-ns:smart:2.5:smartml:action:read",
            parameters=parameters
        )
    
    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new address.
        
        Args:
            data (dict): Address data
            
        Returns:
            dict: Created address details
        """
        parameters = {
            "data": data
        }
        
        return self.client._make_request(
            resource_type="address",
            action_id="urn:onoffice-de-ns:smart:2.5:smartml:action:create",
            parameters=parameters
        )
    
    def update(self, address_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an existing address.
        
        Args:
            address_id (int): Address ID
            data (dict): Updated address data
            
        Returns:
            dict: Updated address details
        """
        parameters = {
            "data": {
                "Id": address_id,
                **data
            }
        }
        
        return self.client._make_request(
            resource_type="address",
            action_id="urn:onoffice-de-ns:smart:2.5:smartml:action:modify",
            parameters=parameters
        )
