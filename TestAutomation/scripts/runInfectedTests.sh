#!/bin/bash
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
