#!/usr/bin/python3
from Driver import Driver
from TestCase import TestCase
import sys

filename = sys.argv[1]
blueprint = TestCase.parse_syntax(testfile)
if blueprint is not None:
    tc = TestCase(blueprint)
    dr = Driver(tc)
    dr.execute()
elif blueprint is None:
    print("Invalid blueprint")
else:
    print("How the hell did you end up here?")
