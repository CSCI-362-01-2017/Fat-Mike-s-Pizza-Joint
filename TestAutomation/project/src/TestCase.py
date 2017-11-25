# TestCase class for containerizing data read from specification files
#
# Written by Chandler DeLoach
class TestCase:
    @staticmethod
    def extract_contents(line):
        full = line.split()
        token = full[0]
        error = None
        if token.find(":") != -1:
            token = token[:len(token)-1] # "Normalize" token by removing ':'
            fi = 1 # 'field index' = index for start of field
        else:
            try:
                colon = full[1]
            except IndexError:
                error = "SpecSyntaxError" # No text or ':'
                return error
            if colon.find(":") == -1:
                error = "SpecSyntaxError" # They forgot the ':' before the text
                return error
            else:
                fi = 2
        if token != "component" and token != "input":
            try:
                field = " ".join(full[fi:])
            except IndexError:
                error = "NullFieldError"
            if field == "":
                error = "NullFieldError"
        else:
            field = ""
        if error is not None:
            return error
        else:
            return [ token, field ]
    
    @staticmethod
    def store_value(token, field, fieldmap):
        for bucket in fieldmap:
            if token == bucket[0]:
                bucket[1] = field
                bucket[2] += 1
                return None
        return "InvalidSpecTypeError" # If they got here, the spec type was invalid

    @staticmethod
    def parse_syntax(testCaseFileName):
        fieldmap = [ ["name", "", 0],
                     ["requirement", "", 0],
                     ["method", "", 0],
                     ["component_class", "", 0],
                     ["component_provider", "", 0],
                     ["input_constructor", "", 0],
                     ["input_method", "", 0],
                     ["oracle", "", 0]] # [name, field, incidences]
        token_dict = { "constructor": "input_constructor",
                       "method": "input_method",
                       "class": "component_class",
                       "provider": "component_provider" }
        error = None
        state_counter = 0 # number of upcoming lines to expect sub-specifications
        with open(testCaseFileName, "r") as testCaseFile:
            for line in testCaseFile:
                line_content = TestCase.extract_contents(line)
                if type(line_content) is str: # we know it's an error string and not a list
                    error = line_content
                    break
                else:
                    token = line_content[0]
                    field = line_content[1]
                if state_counter > 0:
                    try:
                        token = token_dict[token]
                    except KeyError:
                        error = "InvalidSubSpecTypeError"
                        break
                    state_counter -= 1
                if token == "component" or token == "input":
                    state_counter = 2
                else:
                    if token == "method" and field.find("()") != -1:
                        field = field[:len(field)-2] # "Normalize" method_name by removing '()'
                    elif token == "component_provider" and field.find(".py") != -1:
                        field = field[:len(field)-3] # "Normalize" method_name by removing '()'
                    error = TestCase.store_value(token, field, fieldmap) # will remain None if no error
                    if error is not None:
                        break
        errorList = { "SpecSyntaxError": "invalid syntax in one or more specifications",
                      "InvalidSpecTypeError": "invalid specification type for test case",
                      "ConflictingSpecError": "one or more conflicting specifications within test case",
                      "MissingSpecError": "test case is missing a required specification",
                      "InvalidSubSpecTypeError": "invalid sub specification type",
                      "NullFieldError": "field for one or more specifications is empty" }
        if error is None:
            for bucket in fieldmap:
                if bucket[2] > 1:
                    error = "ConflictingSpecError"
                elif bucket[2] == 0:
                    error = "MissingSpecError"
                    print("Missing spec: %s" % bucket[0])
        if error is not None:
            print("Error in file: %s" % errorList[error])
            return None
        else:
            for i in range(5,7):
                if fieldmap[i][1] == "void":
                    fieldmap[i][1] = ""
            blueprint = []
            for field in fieldmap:
                blueprint.append(field[1]) # structure is implicit in ordering
            return blueprint
    
    def __str__(self):
        return "name: " + self.name + "\n" + "requirement: " + self.requirement + "\n" + "method: " + self.method + "\n" + "class: " + self.component_class + "\n" + "provider: " + self.component_provider + "\n" + "constructor_input: " + self.input_constructor + "\n" + "method_input: " + self.input_method + "\n" + "oracle: " + self.oracle

    def __init__(self, blueprint):
        if blueprint is not None:
            self.name               = blueprint[0]
            self.requirement        = blueprint[1]
            self.method             = blueprint[2]
            self.component_class    = blueprint[3]
            self.component_provider = blueprint[4].replace("/", ".")
            self.input_constructor  = blueprint[5]
            self.input_method       = blueprint[6]
            self.oracle             = blueprint[7]
        else:
            print("Error: attempted to create TestCase from improperly validated file!")
