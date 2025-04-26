#!/bin/bash

. .conf

echo "Removing old generated code"
rm -r src/recodex_cli_lib/generated

echo "Generating new swagger document"
cd ../api
./generate-swagger > ../swagger.yaml

echo "Generating new client code"
cd ../recodexLib
# create output folder
mkdir -p $outPath

# generate code
java -jar "$swaggerCodegenPath/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar" generate \
   -i $swaggerSpecPath \
   -l python \
   -o $outPath

# copy the swagger spec
cp $swaggerSpecPath "$outPath/$outSwaggerSpecName"

echo "Moving new generated client"
mv ../generated src/recodex_cli_lib/generated

# make import adjustments in the generated code
sed -i 's/\bswagger_client\b/..swagger_client/g' src/recodex_cli_lib/generated/swagger_client/__init__.py
sed -i 's/import swagger_client\.models/from swagger_client import models/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\.models\b/models/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\b/..swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api_client.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api/__init__.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/api/default_api.py
sed -i 's/\bswagger_client\b/...swagger_client/g' src/recodex_cli_lib/generated/swagger_client/models/__init__.py
