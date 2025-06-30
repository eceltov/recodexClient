#!/bin/bash

# path to swagger-codegen
swaggerCodegenPath=./swagger-codegen-cli-3.0.9.jar

# path to the new swagger specification file from the ReCodEx api repository
recodexSwaggerDocsPath=./tests/swagger.yaml

# path to the generated code
generatedPath=./src/recodex_cli_lib/generated

# donwload swagger-codegen
wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.9/swagger-codegen-cli-3.0.9.jar

echo "Removing old generated code"
rm -r $generatedPath

echo "Generating new client code"
java -jar "$swaggerCodegenPath" generate \
   -i $recodexSwaggerDocsPath \
   -l python \
   -o $generatedPath

# copy the swagger spec
cp $recodexSwaggerDocsPath "$generatedPath/swagger.yaml"

# make import adjustments in the generated code
# the raw generated code expects to be used as a top-level package using absolute import,
# but that is not the case here, the absolute imports need to be converted to relative ones by
# adding a correct number of dots before them (based on directory depth)
sed -i 's/\bswagger_client\b/..swagger_client/g' src/recodex_cli_lib/generated/swagger_client/__init__.py
sed -i 's/import swagger_client\.models/from swagger_client import models/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\.models\b/models/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\b/..swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api/__init__.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api/default_api.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/models/*.py
