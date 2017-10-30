# Fat Mike's Testing Framework
This testing framework is developed specifically for automated unit tests on Python project source code files.

This framework reads in test case specifications in this format:
```name: (name of test case)
requirement: (requirement being tested)
component: 
    class: (class containing method being tested)
    provider: (.py file which provides class) 
method: (method being tested)
input:
    constructor: (comma-seperated arguments to constructor)
    method: (comma-seperated arguments to constructor)
oracle: (expected method return)
```
and use them to run automated unit tests on the codebase of the project specified (by default this is Cadasta of course).

Note that certain constructors and methods may take or require no arguments; this specified in a testCase file by the **void** keyword, ex.
```
    constructor: void
    method: void
```
