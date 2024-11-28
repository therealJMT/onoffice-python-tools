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
            action_id=self.client.ACTION_READ,
            parameters=parameters
        )

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new estate.
        
        Args:
            data (dict): Estate data to create
            
        Returns:
            dict: Creation result
            
        Examples:
            >>> client.estate.create({
            ...     "objektart": "haus",
            ...     "kaufpreis": 250000,
            ...     "lage": "Berlin"
            ... })
        """
        return self.client._make_request(
            resource_type="estate",
            action_id=self.client.ACTION_CREATE,
            parameters={"data": data}
        )

    def update(self, estate_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an existing estate.
        
        Args:
            estate_id (int): ID of the estate to update
            data (dict): Updated estate data
            
        Returns:
            dict: Update result
            
        Examples:
            >>> client.estate.update(123, {
            ...     "kaufpreis": 260000
            ... })
        """
        return self.client._make_request(
            resource_type="estate",
            action_id=self.client.ACTION_MODIFY,
            parameters={
                "data": {
                    "elements": [{
                        "id": estate_id,
                        **data
                    }]
                }
            }
        )

    def delete(self, estate_id: int) -> Dict[str, Any]:
        """
        Delete an estate.
        
        Args:
            estate_id (int): ID of the estate to delete
            
        Returns:
            dict: Deletion result
            
        Examples:
            >>> client.estate.delete(123)
        """
        return self.client._make_request(
            resource_type="estate",
            action_id=self.client.ACTION_DELETE,
            parameters={
                "data": {
                    "elements": [{
                        "id": estate_id
                    }]
                }
            }
        )

    def get(self, estate_id: int, fields: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Get a single estate by ID.
        
        Args:
            estate_id (int): ID of the estate to retrieve
            fields (list, optional): Fields to return
            
        Returns:
            dict: Estate data
            
        Examples:
            >>> client.estate.get(123, fields=["kaufpreis", "lage"])
        """
        fields = fields or ["Id", "kaufpreis", "lage"]
        return self.client._make_request(
            resource_type="estate",
            action_id=self.client.ACTION_READ,
            parameters={
                "data": fields,
                "filter": {
                    "Id": [{
                        "op": "=",
                        "val": estate_id
                    }]
                }
            }
        )
