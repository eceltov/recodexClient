#!/bin/bash

# path to swagger-codegen (https://github.com/swagger-api/swagger-codegen/tree/3.0.0)
swaggerCodegenPath=../

# path to the new swagger specification file in the ReCodEx api repository
recodexSwaggerDocsPath=../api/docs/swagger.yaml

# path to the generated code
generatedPath=./src/recodex_cli_lib/generated

# path to the old swagger
oldSwaggerDocsPath=./src/recodex_cli_lib/generated/swagger.yaml

if ! test -d ./venv; then
   echo "Initializing Python venv"
   ./initVenv.sh
fi

echo "Updating README"
./venv/bin/activate
python3 src/readmeChangesCleaner.py
python3 src/swaggerDiffchecker.py $oldSwaggerDocsPath $recodexSwaggerDocsPath >> README.md

echo "Removing old generated code"
rm -r $generatedPath

echo "Generating new client code"
java -jar "$swaggerCodegenPath/openapi-generator-cli.jar" generate \
   -i $recodexSwaggerDocsPath \
   -g python \
   -o $generatedPath

# copy the swagger spec
cp $recodexSwaggerDocsPath "$generatedPath/swagger.yaml"

# make import adjustments in the generated code
# the raw generated code expects to be used as a top-level package using absolute import,
# but that is not the case here, the absolute imports need to be converted to relative ones by
# adding a correct number of dots before them (based on directory depth)
sed -i 's/import openapi_client\.models/from openapi_client import models/g' src/recodex_cli_lib/generated/openapi_client/*.py
sed -i 's/\bopenapi_client\b/..openapi_client/g' src/recodex_cli_lib/generated/openapi_client/*.py
sed -i 's/\bopenapi_client\b/...openapi_client/g' src/recodex_cli_lib/generated/openapi_client/api/*.py
sed -i 's/\bopenapi_client\b/...openapi_client/g' src/recodex_cli_lib/generated/openapi_client/models/*.py
# special case where the conversion replaced something that is not an import
sed -i 's/getattr(..openapi_client.models, klass)/getattr(models, klass)/g' src/recodex_cli_lib/generated/openapi_client/api_client.py

