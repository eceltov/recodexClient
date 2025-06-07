#!/bin/bash

# path to swagger-codegen (https://github.com/swagger-api/swagger-codegen/tree/3.0.0)
swaggerCodegenPath=../swagger-codegen

# path to swagger specification file in the ReCodEx api repository
recodexSwaggerDocsPath=../api/docs/swagger.yaml

# path to the generated code
generatedPath=./src/recodex_cli_lib/generated

echo "Removing old generated code"
rm -r $generatedPath

echo "Generating new client code"
java -jar "$swaggerCodegenPath/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar" generate \
   -i $recodexSwaggerDocsPath \
   -l python \
   -o $generatedPath

# copy the swagger spec
cp $recodexSwaggerDocsPath "$generatedPath/swagger.yaml"

# make import adjustments in the generated code
#TODO: improve this doc string
sed -i 's/\bswagger_client\b/..swagger_client/g' src/recodex_cli_lib/generated/swagger_client/__init__.py
sed -i 's/import swagger_client\.models/from swagger_client import models/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\.models\b/models/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\b/..swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api/__init__.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api/default_api.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/models/__init__.py
