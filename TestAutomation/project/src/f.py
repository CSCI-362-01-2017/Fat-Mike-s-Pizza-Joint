from TestCase import TestCase
from Driver import Driver
blueprint = TestCase.parse_syntax("brokenParseFiles/Valid.txt")
if blueprint is not None:
    tc = TestCase(blueprint)
    dr = Driver(tc)
    dr.execute()
