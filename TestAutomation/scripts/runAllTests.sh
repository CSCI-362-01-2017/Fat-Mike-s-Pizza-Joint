#!/bin/bash
ls "testCases" | grep testCase | grep yml > tcs
while read line; do
    ./runSingularTest.sh "testCases/$line"
done < tcs
rm tcs
cd ../reports
cat * > final.html
xdg-open final.html
rm *.yml.html 2>/dev/null
