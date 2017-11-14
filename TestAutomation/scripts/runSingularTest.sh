#!/bin/bash
# Run a singular test from test case specification file
source printlast
TESTFILE="$1"
SHORTNAME="`printlast $1`" 1>/dev/null # Get name from within testCases directory 
../project/bin/Loader.py "$TESTFILE" > "../temp/$SHORTNAME"
./createReportRevised.sh "../temp/$SHORTNAME"
rm "../temp/$SHORTNAME"
