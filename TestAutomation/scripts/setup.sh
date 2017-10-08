#!/bin/sh
# This file will make sure the required files are in place, and then create a file to 
# store necessary environment variables

TARGETPATH="$1"
SCRIPTS="`pwd`"
PARENT=..
if [ -z "$TARGETPATH" ]; then
    echo "Do you have the cadasta-platform repo cloned onto your machine somewhere?"
    read -n 1 answer
    if [ "$answer" = "n" ] || [ "$answer" = "N" ]; then
        hasgit="`whereis git` | awk '{ print $2 }'"
        if [ -z "$hasgit" ]; then
            echo "Error: git must be installed for repository to be cloned"
            exit -1
        else
            cd PARENT
            git clone https://github.com/Cadasta/cadasta-platform
            TARGETPATH="PARENT/cadasta-platform"
            cd "$SCRIPTS"
        fi
    elif [ "$answer" = "y" ] || [ "$answer" = "Y" ]; then
        echo "Please pass the path to the cloned repository to this script as the first argument"
        exit -1
    else
        echo "I'm not sure what you mean."
        exit -1
    fi
fi
