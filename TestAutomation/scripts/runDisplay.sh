#!/bin/bash
# Run a singular test from test case specification file
source printlast
TESTFILE="$1"
SHORTNAME="`printlast $1 | awk '{print substr($1, 1, length($1)-4)}'`" 
../project/bin/Loader.py "$TESTFILE" > "../temp/$SHORTNAME"
./tablegen.sh "../temp/$SHORTNAME" > "../reports/$SHORTNAME.html"
rm "../temp/$SHORTNAME"
xdg-open "../reports/$SHORTNAME.html"
