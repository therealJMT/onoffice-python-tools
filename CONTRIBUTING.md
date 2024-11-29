# Contributing to OnOffice Python SDK

First off, thank you for considering contributing to the OnOffice Python SDK! It's people like you that make this SDK better for everyone.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/onoffice-python-tools.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate the environment: 
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
5. Install development dependencies: `pip install -e ".[dev]"`

## Development Process

1. Create a new branch for your feature: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run the test suite: `pytest`
4. Update documentation if needed
5. Update CHANGELOG.md
6. Commit your changes: `git commit -m "Add some feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Submit a Pull Request

## Code Style

- Follow PEP 8 guidelines
- Add type hints to all functions
- Include docstrings for all public methods
- Keep functions focused and concise
- Write meaningful commit messages

## Testing

- Write tests for all new features
- Ensure all tests pass before submitting PR
- Include both unit tests and integration tests
- Use mock data for API responses

## Documentation

- Update README.md if adding new features
- Add docstrings to all new classes and methods
- Include examples for new functionality
- Update CHANGELOG.md with your changes

## Questions?

Feel free to open an issue for any questions or concerns.
