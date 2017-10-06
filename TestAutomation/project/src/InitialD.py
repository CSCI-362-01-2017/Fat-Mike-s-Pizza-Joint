#!/usr/bin/python3
#
# InitialD.py: Initial D(river) python file
# Will contain these classes: TestPlan, TestCase, Driver
#
import sys

class TestPlan:
    def validStructure(testFile):
        # This method determines if test case specification file meets structural syntax standards
        # STATUS:
        # basic token parsing: works
        # everything else: untested
        testTokens = specTokens = 0
        error = keys = None
        for line in testFile:
            full = line.split()
            token = full[0]
            if token.find(":") != -1:
                token = token[:len(token)-1] # "Normalize" token by removing ':'
            if token == "test":
                testTokens += 1
                if keys is not None:
                    for key in keys:
                        if key[1] != 1: # Must have one of every token
                            error = "ConflictingSpec"
                            break
                        else:
                            key[1] = 0 # Reset incidences
                    if error is not None:
                        break # Drop out to singular handling point for errors outside loop
            elif token.isalpha():
                specTokens += 1
            keys = [ ["test", 0], ["name", 0], ["requirement", 0], # Reset incidences
                     ["component", 0], ["method", 0], ["input", 0], ["output", 0] ]
            validToken = False
            for key in keys:
                if token == key[0]:
                    validToken = True
                    key[1] += 1
            if validToken is False:
                error = "InvalidSpec"
                break
        errorList = { "InvalidNumSpec": "invalid number of specifications for test case",
                      "InvalidSpec": "invalid specification for test case",
                      "ConflictingSpec": "one or more conflicting specifications within test case" }
        for key in keys:
            if key[1] != 1:
                error = "ConflictingSpec"
        if specTokens != testTokens * 6:
            error = "InvalidNumSpec"
        if error is not None:
            print("Error in file: %s" % errorList[error])
            return False
        else:
            return True

def main():
    try:
        testfile = open(sys.argv[1])
    except FileNotFoundError:
        print("Error: invalid file specified for test case")
        print("Exiting...")
        exit(-1)
    except IndexError:
        print("USAGE: ./InitialD.py [path to test case specification file]")
        print("Exiting...")
        exit(-1)
    TestPlan.validStructure(testfile)

main()
