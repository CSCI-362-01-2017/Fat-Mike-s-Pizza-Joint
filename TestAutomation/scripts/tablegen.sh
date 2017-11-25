#!/bin/bash
OUTPUT=""
while read line; do
    if [ "$line" = "EOF" ]; then
        break
    elif [ ! "$line" = "Output:" ]; then
        if [ -z "$OUTPUT" ]; then
            OUTPUT="$line"
        else
            OUTPUT="$OUTPUT\n$line"
        fi
    fi
done < $1 
OUTPUT="$OUTPUT"

getfield() {
    printf "$1\n" | awk '{for (i=2; i<=NF; i++) printf $i " "}'
}

SUMMARY="`tail -n 10 \"$1\"`"

setvar() {
VAR="`printf \"$SUMMARY\" | sed -n $1p`"
VAR="`getfield \"$VAR\"`"
printf "$VAR"
}

NAME="`setvar 1`"
REQUIREMENT="`setvar 2`"
METHOD="`setvar 3`"
CLASS="`setvar 4`"
PROVIDER="`setvar 5`"
CONSTRUCTOR_INPUT="`setvar 6`"
METHOD_INPUT="`setvar 7`"
ORACLE="`setvar 8`"
RETURN="`setvar 9`"
RESULT="`setvar 10 | awk '{print $1}'`"

PASS_GREEN="#99eb84"
FAIL_RED="#f59884"
if [ "$RESULT" = "PASS" ]; then
    RESULT_BG="$PASS_GREEN"
else
    RESULT_BG="$FAIL_RED"
fi
printf "$NAME\n$REQUIREMENT\n$METHOD\n$CLASS\n$PROVIDER\n$CONSTRUCTOR_INPUT\n$METHOD_INPUT\n$ORACLE\n$RETURN\n$RESULT\n$RESULT_BG\n"

cat << EOF
<html>
    <head>
        <title>Tables test</title>
    </head>

    <body>
        <div align="center">
            <table width="60%" border="1" cellpadding="0" cellspacing="2" bgcolor="white">
                <tr>
                    <td colspan="2" width="50%" align="center" bgcolor="#c3e7ed">testCaseTitle</td>
                    <td width="50%" align="center" bgcolor="#c3e7ed">Detail view</td>
                </tr>
                <tr>
                    <td bgcolor="f2e4b9">Name:</td><td width="30%" align="center">$NAME</td>
                    <td rowspan="13" width="50%">$OUTPUT</td>
                </tr>
                <tr>
                    <td bgcolor="f2e4b9">Requirement:</td><td align="center">$REQUIREMENT</td>
                </tr>
                <tr>
                    <td bgcolor="f2e4b9">Provider:</td><td align="center">$PROVIDER</td>
                </tr>
                <tr>
                    <td bgcolor="f2e4b9">Class:</td><td align="center">$CLASS</td>
                </tr>
                <tr>
                    <td bgcolor="f2e4b9">Method:</td><td align="center">$METHOD</td>
                </tr>
                <tr>
                    <td colspan="2" align="center" bgcolor="#c3e7ed">Input</td>
                </tr>
                <tr>
                    <td bgcolor="f2e4b9">Constructor:</td><td align="center">$CONSTRUCTOR_INPUT</td>
                </tr>
                <tr>
                    <td bgcolor="f2e4b9">Method:</td><td align="center">$METHOD_INPUT</td>
                </tr>
                <tr>
                    <td colspan="2" align="center" bgcolor="#c3e7ed">Output</td> </tr>
                <tr>
                    <td bgcolor="f2e4b9">Oracle:</td><td align="center">$ORACLE</td>
                </tr>
                <tr>
                    <td bgcolor="f2e4b9">Actual:</td><td align="center">$RETURN</td>
                </tr>
                <tr>
                    <td colspan="2" align="center" bgcolor="#c3e7ed">Result</td>
                </tr>
                <tr>
                    <td colspan="2" align="center" bgcolor="$RESULT_BG">$RESULT</td>
                </tr>
            </table>
    </body>
</html>
EOF
