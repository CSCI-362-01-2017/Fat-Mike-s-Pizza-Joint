#!/usr/bin/python3
# TestCase class for containerizing data read from specification files
#
# Written by Chandler DeLoach
class TestCase:
    def validate(testCaseFile):
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
            return None
        else:
            fields = []
            for key in keys:
                fields.append(key[1])
            return fields

    def __init__(self, validatedFile):
        if validatedFile is not None:
            self.name        = validatedFile[0]
            self.requirement = validatedFile[1]
            self.component   = validatedFile[2]
            self.method      = validatedFile[3]
            self.input       = validatedFile[4]
            self.output      = validatedFile[5]
        else:
            print("Error: attempted to create TestCase from improperly validated file!")
