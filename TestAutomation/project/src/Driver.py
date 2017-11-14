# Actual Driver class for utilized by testing framework
# Written by Chandler DeLoach
import sys

class Driver:
    def __init__(self, testcase):
        self.testcase = testcase

    def execute(self):
        t = self.testcase
        error = None
        print(self.testcase)
        try:
           exec("from %s import %s" % (t.component_provider, t.component_class))
        except ImportError:
            print("Error in import: class %s or module %s not found" % (t.component_class, t.component_provider))
            return "ImportError"
        except ModuleNotFoundError:
            print("Error in import: provider module %s not found" % t.component_provider)
            return "ModuleNotFoundError"
        except:
            print("Unexpected error encountered in import, congrats!")
            raw = str(sys.exc_info()[0]).split()[1]
            error = "UnexpectedImport" + raw[1:len(raw)-2]
            print("Error: %s" % error)
            return error
        if error is None:
            try:
                if t.input_constructor != "static":
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
                if t.input_constructor == "static":
                    METHOD_RETURN = str(eval("%s.%s(%s)"
                                            % (t.component_class, t.method, t.input_method)))
                else:
                    METHOD_RETURN = str(eval("TEST_CLASS_INST.%s(%s)" % (t.method, t.input_method)))
            except AttributeError:
                print("Error: method %s not found in class %s from provider %s"
                      % t.method, t.component_class, t.component_provider)
                error = "AttributeError"
            except:
                raw = str(sys.exc_info()[0]).split()[1]
                error = raw[1:len(raw)-2]
                print("Error: %s" % error)
        if error is None:
            print("Method : %s\nClass : %s\nReturn : %s\nOracle : %s"
                  % (t.method, t.component_class, METHOD_RETURN, t.oracle))
            oracle_correct = eval("%s == %s" % (METHOD_RETURN, t.oracle))
        else:
            print("Method : %s\nClass : %s\nError : %s\nOracle : %s"
                  % (t.method, t.component_class, error, t.oracle))
            print("Method %s from class %s raised %s" % (t.method, t.component_class, error))
            print("Oracle predicted %s" % t.oracle)
            oracle_correct = eval("%s == %s" % (error, t.oracle))
        if oracle_correct:
            print("PASS")
        else:
            print("FAIL")
