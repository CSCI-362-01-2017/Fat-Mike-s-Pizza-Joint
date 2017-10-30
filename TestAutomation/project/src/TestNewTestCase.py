#!/usr/bin/python3
from NewTestCase import TestCase
import sys

def main():
    with open(sys.argv[1]) as testfile:
        fieldmap = TestCase.parse_syntax(testfile)
        if type(fieldmap) is not None:
            print(fieldmap)
        print("from %s" % sys.argv[1])
main()
