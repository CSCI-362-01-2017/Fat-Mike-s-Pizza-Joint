#!/bin/bash
if [ -z "`pwd | grep scripts`" ]; then
    cd scripts
    if [ -z "`pwd | grep scripts`" ]; then
        printf "Error: cannot navigate to scripts directory. Please execute this script from either TestAutomation/ or TestAutomation/scripts/\n"
        exit -1
    fi
fi
rm ../reports/*
ls "testCases" | grep testCase | grep yml > tcs
while read line; do
    printf "Generating report for $line\n"
    ./runSingularTest.sh "testCases/infectedTestCases/$line"
done < tcs
rm tcs
cd ../reports
cat * > final.html
xdg-open final.html
cd ../scripts
