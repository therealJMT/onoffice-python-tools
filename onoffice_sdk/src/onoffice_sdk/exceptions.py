"""
Custom exceptions for the OnOffice SDK.
"""

class OnOfficeAPIError(Exception):
    """Base exception for OnOffice API errors."""
    def __init__(self, message, response=None):
        super().__init__(message)
        self.response = response

class AuthenticationError(OnOfficeAPIError):
    """Raised when authentication fails."""
    pass

class RateLimitError(OnOfficeAPIError):
    """Raised when API rate limit is exceeded."""
    def __init__(self, message, reset_time=None):
        super().__init__(message)
        self.reset_time = reset_time

class ValidationError(OnOfficeAPIError):
    """Raised when request validation fails."""
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors or {}
