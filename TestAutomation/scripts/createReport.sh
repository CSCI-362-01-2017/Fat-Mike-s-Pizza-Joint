#!/bin/bash
if [ ! -f ../../reporsts/o ]; then
	input="../../temp/test.txt"
	o="/../../reports"

	echo "<html>" >> o

	echo "<!Doctype html>" >> o
	echo "<title>Report</title>" >> o
	echo "</head>" >> o
	echo "<body>" >> o

	while IFS=: read -r line
	do
		echo "$line" >> o
		echo "<br/>" >> o

	done<"$input"

	echo "</body>" >> o
	echo "</html>" >> o
	mv o "../../reports/"
	mv "../../reports/o" "../../reports/report.html"
else
	rm "../../reports/o"
		input="../../temp/test.txt"
	o="/../../reports"

	echo "<html>" >> o

	echo "<!Doctype html>" >> o
	echo "<title>Report</title>" >> o
	echo "</head>" >> o
	echo "<body>" >> o

	while IFS=: read -r line
	do
		echo "$line" >> o
		echo "<br/>" >> o

	done<"$input"

	echo "</body>" >> o
	echo "</html>" >> o
	mv o "../../reports/"
	mv "../../reports/o" "../../reports/report.html"
fi
