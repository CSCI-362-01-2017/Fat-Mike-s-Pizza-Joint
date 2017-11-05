#!/bin/bash
# TODO: write this output as a table
source printlast
INFILE="$1"
SHORTNAME="`printlast $INFILE`"

if [ -e "$SHORTNAME.html" ]; then
    rm "$SHORTNAME.html"
fi
cat > "../reports/$SHORTNAME.html" << EOF
<html>
<head>
<title>$SHORTNAME results</title>
</head>
<body>
EOF
while read line; do
    echo "$line<br>" >> "../reports/$SHORTNAME.html"
done < "$INFILE"
printf "</body>\n</html>\n" >> "$SHORTNAME.html"
