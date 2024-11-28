"""
Estate resource handler for the OnOffice API.
"""

from typing import Dict, List, Any, Optional

class EstateResource:
    """
    Handler for estate-related API endpoints.
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
        Search for estates with given filters.
        
        Args:
            filters (dict, optional): Search filters
            fields (list, optional): Fields to return. Defaults to ["Id", "kaufpreis", "lage"]
            limit (int, optional): Maximum number of results. Defaults to 100
            offset (int, optional): Number of results to skip. Defaults to 0
            sort_by (dict, optional): Sorting criteria. Example: {"kaufpreis": "ASC"}
        
        Returns:
            dict: Search results
            
        Examples:
            >>> client.estate.search(
            ...     filters={"status": [{"op": "=", "val": 1}]},
            ...     fields=["Id", "kaufpreis", "lage"],
            ...     sort_by={"kaufpreis": "ASC"}
            ... )
        """
        fields = fields or ["Id", "kaufpreis", "lage"]
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
            resource_type="estate",
            action_id="urn:onoffice-de-ns:smart:2.5:smartml:action:read",
            parameters=parameters
        )
    
    def get(self, estate_id: int, fields: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Get a single estate by ID.
        
        Args:
            estate_id (int): Estate ID
            fields (list, optional): Fields to return
            
        Returns:
            dict: Estate details
        """
        fields = fields or ["Id", "kaufpreis", "lage"]
        parameters = {
            "data": fields,
            "filter": {
                "Id": [{"op": "=", "val": estate_id}]
            }
        }
        
        return self.client._make_request(
            resource_type="estate",
            action_id="urn:onoffice-de-ns:smart:2.5:smartml:action:read",
            parameters=parameters
        )
    
    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new estate.
        
        Args:
            data (dict): Estate data
            
        Returns:
            dict: Created estate details
        """
        parameters = {
            "data": data
        }
        
        return self.client._make_request(
            resource_type="estate",
            action_id="urn:onoffice-de-ns:smart:2.5:smartml:action:create",
            parameters=parameters
        )
    
    def update(self, estate_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an existing estate.
        
        Args:
            estate_id (int): Estate ID
            data (dict): Updated estate data
            
        Returns:
            dict: Updated estate details
        """
        parameters = {
            "data": {
                "Id": estate_id,
                **data
            }
        }
        
        return self.client._make_request(
            resource_type="estate",
            action_id="urn:onoffice-de-ns:smart:2.5:smartml:action:modify",
            parameters=parameters
        )
