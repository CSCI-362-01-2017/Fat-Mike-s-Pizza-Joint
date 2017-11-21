#!/usr/bin/python3
import sys
try:
    f = open(sys.argv[1], "r")
except IndexError, FileNotFoundError:
    exit()

gettoken = lambda s : s[0]

def getfield(s):
    ss = s.split()
    for i in range(len(ss)):
        if s[i].find(":") != -1:
            return " ".join(ss[i+1:len(ss)])

fl = f.readlines()
for ln in fl:
    token = gettoken(ln)
    if token == "Name:":
    elif token == "Requirement":
    elif token == "Method":
    elif token == "Class":
    elif token == "Provider":
    elif token == "Method Input":
    elif token == "Requirement":


contents = '''<html>
    <head>
        <title>Tables test</title>
    </head>

    <body>
        <div align="center">
            <table width="60%" border="1" cellpadding="0" cellspacing="2" bgcolor="white">
                <tr>
                    <td colspan="2" width="50%" align="center">testCaseTitle</td>
                    <td width="50%" align="center">Detail view</td>
                </tr>
                <tr>
                    <td>Name:</td><td width="30%" align="center">field</td>
                    <td rowspan="13" width="50%">Raw program output goes here</td>
                </tr>
                <tr>
                    <td>Requirement:</td><td align="center">field</td>
                </tr>
                <tr>
                    <td>Provider:</td><td align="center">field</td>
                </tr>
                <tr>
                    <td>Class:</td><td align="center">field</td>
                </tr>
                <tr>
                    <td>Method:</td><td align="center">field</td>
                </tr>
                <tr>
                    <td colspan="2" align="center">Input</td>
                </tr>
                <tr>
                    <td>Constructor:</td><td align="center">field</td>
                </tr>
                <tr>
                    <td>Method:</td><td align="center">field</td>
                </tr>
                <tr>
                    <td colspan="2" align="center">Output</td>
                </tr>
                <tr>
                    <td>Expected:</td><td align="center">field</td>
                </tr>
                <tr>
                    <td>Actual:</td><td align="center">field</td>
                </tr>
                <tr>
                    <td colspan="2" align="center">Result</td>
                </tr>
                <tr>
                    <td colspan="2" align="center">the result</td>
                </tr>
            </table>
    </body>
</html>'''
