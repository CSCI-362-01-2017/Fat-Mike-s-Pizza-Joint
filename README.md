# Fat Mike's Testing Framework
This testing framework is developed specifically for automated unit tests on components for the Cadasta project, but ought to work with any similar Python-based project. The primary function of this framework is to read in test case specifications in this format:
```name       : Name of test case
requirement: Requirement being tested
component  : Component containing method
method     : Method being tested
input      : Input including arguments
output     : Expected output
```
and use them to run automated unit tests on the codebase of the project specified (by default this is Cadasta of course).
