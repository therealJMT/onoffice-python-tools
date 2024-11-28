# OnOffice API Client

A Python client for interacting with the OnOffice API using HMAC2 authentication. This client provides a simple and secure way to make authenticated requests to OnOffice API endpoints.

## Features

- HMAC2 authentication
- Environment variable based configuration
- Simple interface for API requests
- Type hints for better code completion
- Comprehensive error handling

## Requirements

- Python 3.6+
- requests
- python-dotenv

## Installation

1. Clone this repository or download the `onoffice_api_client.py` file
2. Install the required packages:

```bash
pip install requests python-dotenv
```

3. Create a `.env` file in your project directory with your OnOffice API credentials:

```
ONOFFICE_API_TOKEN=your_token
ONOFFICE_API_SECRET=your_secret
```

## Usage

```python
from onoffice_api_client import send_onoffice_api_request
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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

# Make API request
result = send_onoffice_api_request(
    token=os.getenv('ONOFFICE_API_TOKEN'),
    secret=os.getenv('ONOFFICE_API_SECRET'),
    resourcetype='estate',
    actionid='urn:onoffice-de-ns:smart:2.5:smartml:action:read',
    parameters=parameters
)

print(result)
```

## Security

- Never commit your `.env` file to version control
- Keep your API credentials secure
- Use environment variables for sensitive data

## License

MIT License - Feel free to use and modify as needed.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements.
