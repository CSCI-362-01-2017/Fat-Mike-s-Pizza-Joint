#!/usr/bin/python3
#
# InitialD.py: Initial D(river) python file
# Will contain these classes: TestPlan, TestCase, Driver
#
class TestPlan:
    def validSyntax(testFile):
        # This method determines if file meets syntax standards
        # STATUS: completely untested
        testTokens = subTokens = 0
        error = None
        for line in testFile:
            full = line.split()
            token = full[0]
            if token.find(":") != -1:
                token = token[:len(token)-1] # "Normalize" token by removing ':'
            if token == "test":
                testTokens += 1
            elif token.isalpha():
                specTokens += 1
            keys = [ "test", "name", "requirement", "component", "method", "input", "output" ]
            validToken = False
            for key in keys:
                if token == key:
                    validToken = True
            if validToken is False:
                error = "InvalidSpec"
        errorList = { "InvalidNumSpec": "invalid number of specifications for test case",
                      "InvalidSpec": "invalid specification for test case" }
        if specTokens != testTokens * 6:
            error = "InvalidNumSpec"
        if error is not None:
            print("Error in file: %s" % errorList[error])
            return False
        else:
            return True
