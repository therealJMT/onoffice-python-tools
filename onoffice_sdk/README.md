# OnOffice Python SDK

A modern, Pythonic SDK for interacting with the OnOffice API. This SDK provides a simple and intuitive interface for working with OnOffice's estate and address management features.

## Features

- 🔒 Secure HMAC2 authentication
- 🏠 Complete Estate management
- 👥 Address/Contact management
- ⚡ Modern async-ready design
- 🛡️ Type hints for better IDE support
- 📝 Comprehensive documentation
- 🧪 Example code included

## Installation

```bash
# Clone the repository
git clone https://github.com/therealJMT/onoffice-python-tools.git
cd onoffice-python-tools/onoffice_sdk

# Install the package locally
pip install .

# Or install in development mode if you plan to modify the code
pip install -e .
```

## Quick Start

```python
from onoffice_sdk import OnOfficeClient

# Initialize the client
client = OnOfficeClient(
    token=os.getenv("ONOFFICE_API_TOKEN"),  # Use environment variables
    secret=os.getenv("ONOFFICE_API_SECRET")  # Never hardcode credentials
)

# Search for estates
estates = client.estate.search(
    filters={
        "status": [{"op": "=", "val": 1}],
        "kaufpreis": [{"op": "<", "val": 300000}]
    },
    fields=["Id", "kaufpreis", "lage"],
    sort_by={"kaufpreis": "ASC"}
)

# Get a single estate
estate = client.estate.get(estate_id=123)

# Create a new address
new_address = client.address.create({
    "Vorname": "John",
    "Name": "Doe",
    "Email": "john.doe@example.com"
})
```

## Environment Variables

Create a `.env` file in your project directory:

```env
ONOFFICE_API_TOKEN=your_token_here
ONOFFICE_API_SECRET=your_secret_here
```

Then in your code:

```python
from dotenv import load_dotenv
import os

load_dotenv()

client = OnOfficeClient(
    token=os.getenv('ONOFFICE_API_TOKEN'),
    secret=os.getenv('ONOFFICE_API_SECRET')
)
```

## Security Best Practices

⚠️ **Important Security Notes:**

1. **Environment Variables**: Always use environment variables for your API credentials. Never hardcode them in your code.
   ```bash
   # .env file (Add to .gitignore!)
   ONOFFICE_API_TOKEN=your_actual_token
   ONOFFICE_API_SECRET=your_actual_secret
   ```

2. **Version Control**: 
   - Never commit `.env` files to version control
   - Never commit actual API credentials
   - Always use placeholder values in examples

3. **Production Usage**:
   - Use secure secret management in production
   - Rotate credentials regularly
   - Use the minimum required permissions

## Error Handling

The SDK provides specific exceptions for different error cases:

```python
from onoffice_sdk import OnOfficeClient, AuthenticationError, RateLimitError

try:
    client = OnOfficeClient(token="invalid", secret="invalid")
    estates = client.estate.search()
except AuthenticationError:
    print("Authentication failed")
except RateLimitError as e:
    print(f"Rate limit exceeded. Try again after {e.reset_time}")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Available Resources

### Estate Resource

- `search()`: Search for estates with filters
- `get()`: Get a single estate by ID
- `create()`: Create a new estate
- `update()`: Update an existing estate

### Address Resource

- `search()`: Search for addresses with filters
- `get()`: Get a single address by ID
- `create()`: Create a new address
- `update()`: Update an existing address

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
