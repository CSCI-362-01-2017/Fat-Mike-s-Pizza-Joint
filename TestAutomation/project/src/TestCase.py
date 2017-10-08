#!/usr/bin/python3
# TestCase class for containerizing data read from specification files
#
# Written by Chandler DeLoach
class TestCase:
    def __init__(self, testCaseFile):
        # On init, we're going to parse a file to build our test case.
        # If any errors are encountered while parsing, our "self.valid" boolean becomes false,
        # signaling that the object should be not be processed further.
        #
        # INIT METHOD STATUS: Tested by creator, unreviewed by peers:
        # [ ] Jayse White
        # [ ] Ethan Hendrix
        error = None
        keys = [ ["name", "", 0], ["requirement", "", 0], ["component", "", 0], ["method", "", 0], ["input", "", 0], ["output", "", 0] ] # [name, field, incidences]
        for line in testCaseFile:
            full = line.split()
            token = full[0]
            if token.find(":") != -1:
                token = token[:len(token)-1] # "Normalize" token by removing ':'
                fi = 1
            else:
                try:
                    colon = full[1]
                except IndexError:
                    error = "SpecSyntaxError" # No text or ':'
                    break
                if colon.find(":") == -1:
                    error = "SpecSyntaxError" # They forgot the ':' before the text
                    break
                else:
                    fi = 2 # 'fi' = 'field index' = index for specification field
            try:
                field = " ".join(full[fi:])
            except IndexError:
                error = "NullFieldError"
                break
            if field == "":
                error = "NullFieldError"
                break
            validToken = False
            for key in keys:
                if token == key[0]:
                    validToken = True
                    key[1] = field
                    key[2] += 1
            if validToken is False:
                error = "InvalidSpecTypeError"
                break
        errorList = { "SpecSyntaxError": "invalid syntax in one or more specifications",
                      "InvalidSpecTypeError": "invalid specification type for test case",
                      "ConflictingSpecError": "one or more conflicting specifications within test case",
                      "MissingSpecError": "test case is missing a required specification",
                      "NullFieldError": "field for one or more specifications is empty" }
        for key in keys:
            if error is None:
                if key[2] > 1:
                    error = "ConflictingSpecError"
                elif key[2] == 0:
                    error = "MissingSpecError"
        if error is not None:
            print("Error in file: %s" % errorList[error])
            self.valid = False
        else:
            self.valid = True
            self.name        = keys[0][1]
            self.requirement = keys[1][1]
            self.component   = keys[2][1]
            self.method      = keys[3][1]
            self.input       = keys[4][1]
            self.output      = keys[5][1]

    def isValid(self):
        return self.valid
