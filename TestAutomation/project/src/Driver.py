# Actual Driver class for utilized by testing framework
# Written by Chandler DeLoach
import sys

class Driver:
    def __init__(self, testcase):
        self.testcase = testcase

    def execute(self):
        t = self.testcase
        error = None
        try:
           exec("from %s import %s" % (t.component_provider, t.component_class))
        except ImportError:
            print("Error in import: class %s not found" % t.component_class)
            error = "ImportError"
        except ModuleNotFoundError:
            print("Error in import: provider module %s not found" % t.component_provider)
            error = "ModuleNotFoundError"
        except:
            print("Unexpected error encountered in import, congrats!")
            raw = str(sys.exc_info()[0]).split()[1]
            error = "UnexpectedImport" + raw[1:len(raw)-2]
            print("Error: %s" % error)
        if error is None:
            try:
                TEST_CLASS_INST = eval("%s(%s)" % (t.component_class, t.input_constructor))
            except NameError:
                print("Error in construction: constructor for class %s not found" % t.component_provider)
                error = "NameError"
            except TypeError:
                print("Error in construction: invalid number of arguments to constructor")
                error = "TypeError"
            except:
                print("Unexpected error encountered in construction, congrats!")
                raw = str(sys.exc_info()[0]).split()[1]
                error = "UnexpectedConstruction" + raw[1:len(raw)-2]
                print("Error: %s" % error)
        if error is None:
            try:
                METHOD_RETURN = eval("TEST_CLASS_INST.%s(%s)" % (t.method, t.input_method))
            except AttributeError:
                print("Error: method %s not found in class %s from provider %s" % t.method, t.component_class, t.component_provider)
                error = "AttributeError"
            except:
                raw = str(sys.exc_info()[0]).split()[1]
                error = raw[1:len(raw)-2]
                print("Error: %s" % error)
        if error is not None:
            print("Method %s from class %s returned %s" % (t.method, t.component_class, str(METHOD_RETURN)))
            print("Oracle predicted %s" % str(t.oracle))
            oracle_correct = eval("%s == %s" % (str(METHOD_RETURN), str(t.oracle)))
        else:
            print("Method %s from class %s raised %s" % (t.method, t.component_class, error))
            print("Oracle predicted %s" % str(t.oracle))
            oracle_correct = eval("%s == %s" % (error, str(t.oracle)))
        if oracle_correct:
            print("...and was correct!")
        else:
            print("...and was not correct.")
