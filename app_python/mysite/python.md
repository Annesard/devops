## Python best practices

There are some best practices to use before, during, and after writing code in Python language in order to make the code readable and create a standard across the industry

Here will be listed several of such practices:
* Create a Code Repository and Implement Version Control
* Create Readable Documentation

  In my project I use readmee and Docstrings

* Follow Style Guidelines

  For example: PEP8(https://www.python.org/dev/peps/pep-0008/)

*  Correct Broken Code Immediately
*  Use the PyPI Instead of Doing it Yourself
*  The Zen of Python (https://www.python.org/dev/peps/pep-0020/)
*  Use the Right Data Structures
*  Write Readable Code
  
  You should use line breaks and indent your code.
  
  Use naming conventions for identifiers- this makes it easier to understand the code.
  
  Use comments, and whitespaces around operators and assignments.
  
  Keep the maximum line length 79 characters.

*   Use Virtual Environments
*   Write Object-Oriented Code
*   Avoid importing everything from a package- this pollutes the global namespace and can cause clashes.
*   Don’t implement best practices from other languages.
*   Do not turn off error reporting during development- turn it off after it.
*   Don’t alter sys.path, use distutils for that.


Reference:https://data-flair.training/blogs/python-best-practices/


## Unit test best practices 

Below several unit test practices are listed:
* Adopt well organaised test structure: like mutation testing, test-driven development, or behavior-driven programming
* Name the test well: save your test with the strategy being tested, save your test given the name of the environment under which it’s being tested, save your test with the proposed behavior when the scenario is requested
* Write relaible and trustworthy unit tests
* Make automated unit tests
* Focus on single use case at a time
* Minimal assertation per test
* Unit test should be isolated
* Trust unit, not integration: a unit test and the system under test must abstain from external factors.
* Aim for 100% test case coverage
* Start using headless testing in the cloud: headless testing takes advantage of lightweight container instances in the cloud that allows you to write tests quickly and avail rapid feedback almost in real-time

Reference: https://www.partech.nl/nl/publicaties/2020/03/10-unit-testing-best-practices

