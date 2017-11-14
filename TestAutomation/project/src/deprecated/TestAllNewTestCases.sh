#!/bin/bash
ls testfiles > tmp
while read line; do
    ./TestNewTestCase.py "testfiles/$line"
done < tmp
rm tmp
