#!/bin/sh

python3 -m build
python3 -m twine upload --repository testpypi dist/*
