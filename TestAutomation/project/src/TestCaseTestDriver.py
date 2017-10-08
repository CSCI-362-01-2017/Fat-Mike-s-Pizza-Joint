#!/usr/bin/python3
# Driver for testing TestCase.py, feel free to modify if you can think of any other relevant testing procedures
# Written by Chandler DeLoach
def main():
    try:
        with open(sys.argv[1]) as testfile:
            vfile = validate(testfile)
            if vfile is not None:
                tc = TestCase(vfile)
                print("Test case looks good!")
                print("Name is %s" % tc.name)
                print("Requirement being tested is %s" % tc.requirement)
                print("Component is %s" % tc.component)
                print("Method is %s" % tc.method)
                print("Input is %s" % tc.input)
                print("Expected output is %s" % tc.output)
            else:
                print("Invalid data in test case specification file.")
                exit(-1)
    except FileNotFoundError:
        print("Error: invalid file specified for test case")
        exit(-1)
    except IndexError:
        print("USAGE: ./TestCaseTestDriver.py [path to test case specification file]")
        exit(-1)

main()
