#!/bin/bash
ls "../testCases" > tcs
while read line; do
    ./runSingularTest.sh "$line"
done < tcs
rm tcs
