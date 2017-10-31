#!/usr/bin/python3
# Honestly, making "Driver" a class was worth it
# just so we have this one called "DriverDriver.py"
from Driver import Driver
from TestCase import TestCase
import sys

with open(sys.argv[1], "r") as testfile:
    blueprint = TestCase.parse_syntax(testfile)
    if blueprint is not None:
        tc = TestCase(blueprint)
        dr = Driver(tc)
        dr.execute()
    elif blueprint is None:
        print("Invalid blueprint")
