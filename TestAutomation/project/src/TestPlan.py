#!/usr/bin/python3
# TestPlan class for aggregating a sequence of TestCases for execution
# Definitely a work in progress, structure may not be final.
#
# Written by Chandler DeLoach
class TestPlan:
    def __init__(self):
        self.numCases = 0
        self.testCases = []
    
    def loadTestCase(self, testCaseIn):
        try:
            if testCaseIn.isValid():
                self.testCases.append(testCaseIn)
                self.numCases += 1
            else:
                print("Warning: tried to load an invalid TestCase object!")
        except AttributeError:
            print("Warning: tried to load a non-TestCase object!")

    def displaySequenceBrief(self):
        numSequenceItem = 1
        print("The current sequence is:")
        for tc in self.testCases:
            print("%d) %s" % (numSequenceItem, tc.name))
            numSequenceItem += 1

    def executeSequence(self):
        for tc in self.testCases:
            TestDriver.executeTest(tc)
