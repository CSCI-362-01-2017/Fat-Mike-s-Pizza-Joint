TEST DESCRIPTION

TEST CASES BY ORDER
parsing test cases: testCase00.yml - testCase07.yml
single line parsing test cases: testCase08.yml - testCase12.yml
store_value test cases: testCase13.yml - testCase14.yml
driver test cases: testCase15.yml - testCase22.yml

name: (name of the test case)
requirement: (requirement being tested)
component: 
    class: (class containing method being tested)
    provider: (.py file which provides class) 
method: (method being tested)
input:
    constructor: (comma-seperated arguments to constructor)
    method: (comma-seperated arguments to constructor)
oracle: (expected method return)

Test Case:
 -  8 for parsing files which should raise various errors 
 - ~5 for extract_contents(singular line parsing)
 -  2 for store_value(valid,invalid type)
 
Driver: 
 -  nonexistent class
 -  nonexistent provider
 -  Class does not have method
 -  Invalid arguments to constructor
 -  invalid arguments to method
 -  invalid "Error" type specified for Oracle
 -  expecting return: 
     -  int,double,string,etc...
     -  user specified class
     -  library (imported)
 -  expecting error: 
     -  built in error
     -  user specified 
     -  library import error 
REVISIT: testCase20.yml-testCase26.yml

KNOWN GOOD
testCase01.yml-testCase14.yml

KNOWN ISSUES
testCase24.yml
testCase23.yml
testCase22.yml
testCase21.yml
testCase20.yml
testCase17.yml
testCase15.yml
testCase13.yml
testCase12.yml
testCase11.yml
testCase10.yml
testCase09.yml
testCase05.yml
testCase04.yml

