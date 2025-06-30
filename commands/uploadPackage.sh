#!/bin/sh

# Uploads the package to test PyPI.
# This requires you to have an account and a matching authentication token.

./venv/bin/python3 -m build
./venv/bin/python3 -m twine upload --repository testpypi dist/*
rm dist/*
