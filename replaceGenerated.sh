#!/bin/bash

echo "Removing old generated code"
rm -r generated

echo "Generating new swagger document"
cd ../api
./generate-swagger > ../swagger.yaml

echo "Generating new client code"
cd ../recodexClient
./generate.sh

echo "Moving new generated client"
mv ../generated generated

echo "Reinstalling generated client"
./installGenerated.sh
