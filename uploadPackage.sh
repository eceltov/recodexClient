#!/bin/sh

./venv/bin/python3 -m build
./venv/bin/python3 -m twine upload --repository testpypi dist/*
rm dist/*
