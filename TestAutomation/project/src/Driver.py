# Example Driver class for instructive purposes
# Written by Chandler DeLoach
import sys

class Driver:
    def __init__(self, testcase):
        self.testcase = testcase

    def execute(self):
        # TODO: add sys.path specification
        # TODO: modify parser to accept '.py'
        t = self.testcase
        try:
            exec("from %s import %s" % (t.component_provider, t.component_class))
        except ImportError:
            print("Error in execution: class or component provider not found")
        try:
            TEST_CLASS_INST = eval("%s(%s)" % (t.component_class, t.input_constructor))
        except NameError:
            print("Error in construction: class not found in file")
        except TypeError:
            print("Error in construction: invalid number of arguments to constructor")
        try:
            METHOD_RETURN = eval("TEST_CLASS_INST.%s(%s)" % (t.method, t.input_method))
        except AttributeError:
            print("Error: method %s not found in class" % t.method)
        print("Method %s from class %s returned %s" % (t.method, t.component_class, str(METHOD_RETURN)))
        print("Oracle predicted %s" % str(t.oracle))
        oracle_correct = eval("%s == %s" % (str(METHOD_RETURN), str(t.oracle)))
        if oracle_correct:
            print("...and was correct!")
        else:
            print("...and was not correct.")
