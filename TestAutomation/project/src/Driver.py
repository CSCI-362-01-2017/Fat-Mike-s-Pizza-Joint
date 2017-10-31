# Actual Driver class for utilized by testing framework
# Written by Chandler DeLoach
import sys

class Driver:
    def __init__(self, testcase):
        self.testcase = testcase

    def execute(self):
        # TODO: add sys.path specification
        t = self.testcase
        try:
           exec("from target.%s import %s" % (t.component_provider, t.component_class))
        except ImportError:
            print("Error in execution: class or component provider target.%s not found" % t.component_provider)
            return None
        try:
            TEST_CLASS_INST = eval("%s(%s)" % (t.component_class, t.input_constructor))
        except NameError:
            print("Error in construction: class not found in file")
            return None
        except TypeError:
            print("Error in construction: invalid number of arguments to constructor")
            return None
        if t.oracle.find("Error"):
            # Expect an error
            sequence='''
            try:
                METHOD_RETURN = TEST_CLASS_INST.%s(%s)
                print(METHOD_RETURN)
            catch %s:
                print("Method %s from class %s raised error: %s")
            '''
            exec(sequence % (t.method, t.input_method, t.oracle, t.method, t.component_class, t.oracle))
        else:
            # 
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
