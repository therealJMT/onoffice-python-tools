"""
OnOffice SDK for Python

A comprehensive SDK for interacting with the OnOffice API.
"""

from .client import OnOfficeClient
from .exceptions import (
    OnOfficeAPIError,
    AuthenticationError,
    RateLimitError,
    ValidationError
)
from .version import __version__

__all__ = [
    'OnOfficeClient',
    'OnOfficeAPIError',
    'AuthenticationError',
    'RateLimitError',
    'ValidationError',
]
