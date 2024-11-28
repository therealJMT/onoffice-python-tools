"""
Example of using the OnOffice SDK to search for estates.
"""

import os
from dotenv import load_dotenv
from onoffice_sdk import OnOfficeClient

# Load environment variables from .env file
load_dotenv()

def main():
    # Initialize the client
    client = OnOfficeClient(
        token=os.getenv('ONOFFICE_API_TOKEN'),
        secret=os.getenv('ONOFFICE_API_SECRET')
    )
    
    try:
        # Search for estates
        results = client.estate.search(
            filters={
                "status": [{"op": "=", "val": 1}],
                "kaufpreis": [{"op": "<", "val": 300000}]
            },
            fields=["Id", "kaufpreis", "lage"],
            sort_by={"kaufpreis": "ASC"},
            limit=10
        )
        
        # Print results
        print("Found estates:")
        for estate in results.get('data', {}).get('records', []):
            print(f"ID: {estate.get('Id')}")
            print(f"Price: {estate.get('kaufpreis')}")
            print(f"Location: {estate.get('lage')}")
            print("-" * 40)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
