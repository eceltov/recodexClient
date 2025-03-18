#!/bin/bash

. .conf

# create output folder
mkdir -p $outPath

# generate code
java -jar "$swaggerCodegenPath/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar" generate \
   -i $swaggerSpecPath \
   -l python \
   -o $outPath

# copy the swagger spec
cp $swaggerSpecPath "$outPath/$outSwaggerSpecName"
