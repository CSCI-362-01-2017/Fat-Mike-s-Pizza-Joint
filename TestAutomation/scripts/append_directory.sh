#!/bin/bash
# This script appends a specified "project" directory path to the "provider" path within a set of
# testCase files contained within a "testCase" directory.
#
# This is for purposes of allowing nicely contained fault injection
source getfield

if [ ! "$#" -eq 2 ]; then
    printf "USAGE: ./append_directory.sh <append_directory> <testCase_directory>\n"
fi

APPEND="$1"
DIRECTORY="$2"
cd "$DIRECTORY"
BUFFER="ylenwikylowk251903"
ls | grep ".yml" > tcs
while read line; do
    FILE="$line"
    printf "" > "$BUFFER"
    printf "Appending $APPEND to provider for $line...\n"
    while read line; do
        if [ ! -z "`printf $line | grep provider`" ]; then
            CURRENT="`getfield "$line"`"
            printf "    provider: $APPEND/$CURRENT\n"
        elif [ ! -z "`printf "$line" | grep 'class\|method\|constructor'`" ]; then
            printf "    $line\n"
        else
            printf "$line\n"
        fi
    done < "$line" >> "$BUFFER"
    mv "$BUFFER" "$FILE"
done < tcs
rm tcs
