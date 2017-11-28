#!/bin/bash

infected="`cat infected`"
cd testCases
if [ ! -d infectedTestCases ]; then
    mkdir infectedTestCases
else
    rm infectedTestCases/*.yml
fi
cp *.yml infectedTestCases/
cd ..
./append_directory.sh "$infected" testCases/infectedTestCases/
