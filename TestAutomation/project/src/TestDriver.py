from Driver import Driver
from NewTestCase import TestCase

def main():
    with open("testfiles/Valid.txt", "r") as testfile:
        blueprint = TestCase.parse_syntax(testfile)
        if blueprint is not None:
            tc = TestCase(blueprint)
            dr = Driver(tc)
            dr.execute()

main()
