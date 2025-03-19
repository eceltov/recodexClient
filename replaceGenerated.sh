#!/bin/bash

echo "Removing old generated code"
rm -r src/generated

echo "Generating new swagger document"
cd ../api
./generate-swagger > ../swagger.yaml

echo "Generating new client code"
cd ../recodexClient
./generate.sh

echo "Moving new generated client"
mv ../generated src/generated

sed -i 's/\bswagger_client\b/..swagger_client/g' src/generated/swagger_client/__init__.py
sed -i 's/import swagger_client\.models/from swagger_client import models/g' src/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\.models\b/models/g' src/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\b/..swagger_client/g' src/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/generated/swagger_client/api/__init__.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/generated/swagger_client/api/default_api.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/generated/swagger_client/models/__init__.py

# echo "Reinstalling generated client"
# ./installGenerated.sh
