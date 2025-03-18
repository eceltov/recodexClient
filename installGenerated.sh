#!/bin/bash

# uninstall old version if present
pip3 uninstall -y swagger-client

cd generated
python3 setup.py install
cd ..
