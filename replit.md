# multic4ll

A Python library for aggregating results from multiple Ethereum contract calls.

## Overview
This is a fork of the original [banteg/multicall.py](https://github.com/banteg/multicall.py) project, intended for development testing purposes.

## Project Structure
```
multicall/           # Main package source code
  __init__.py        # Package exports (Call, Multicall, Signature)
  call.py            # Call class implementation
  constants.py       # Network constants and addresses
  exceptions.py      # Custom exceptions
  loggers.py         # Logging configuration
  multicall.py       # Multicall class implementation
  signature.py       # Signature class implementation
  utils.py           # Utility functions
examples/            # Example usage scripts
tests/               # Test suite
dist/                # Built distribution files (wheel and sdist)
```

## Build System
- **Build Tool**: Poetry
- **Package Name**: multic4ll
- **Version**: 0.0.1

## Dependencies
- Python: >=3.8, <3.11
- web3: ^5.27 (with specific version exclusions)
- eth_retry: ^0.1.8

## Building for PyPI
The package has been configured and built. Distribution files are in the `dist/` folder:
- `multic4ll-0.0.1-py3-none-any.whl` (wheel)
- `multic4ll-0.0.1.tar.gz` (source distribution)

### To upload to PyPI:
```bash
# Using Poetry
poetry publish

# Using Twine
twine upload dist/*

# To upload to TestPyPI first
twine upload --repository testpypi dist/*
```

## Recent Changes
- 2024: Added `packages` configuration to pyproject.toml to properly include the multicall folder
- 2024: Added `readme` field to include readme.md as long description
- 2024: Regenerated poetry.lock file to sync with pyproject.toml changes
