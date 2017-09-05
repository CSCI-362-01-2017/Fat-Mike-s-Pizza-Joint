#!/bin/sh
ls ~ | cat > out
cat > src.html << EOF
<html>
<head>
<title>`pwd`</title>
</head>
<body>
EOF
while read line; do
    echo "$line<br>" >> src.html
done < out
rm out
printf "</body>\n</html>\n" >> src.html
xdg-open src.html && sleep 1 || exit -1
rm src.html
