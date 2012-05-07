.. _test-design:

Test Design Considerations
--------------------------

Page Objects
~~~~~~~~~~~~

Page objects is a design pattern used for web automated testing.

..
    Typical structure recommended.

    tests/pageobject/page.py
    tests/pageobject/element.py
    tests/package1/locators.py
    tests/pakage1/page/somepage.py
    tests/pakage1/test_something.py
    tests/package2/locators.py
    tests/pakage2/page/somepage.py
    tests/pakage2/test_something.py

Few links:

1. http://code.google.com/p/selenium/wiki/PageObjects
2. http://www.theautomatedtester.co.uk/tutorials/selenium/page-object-pattern.htm
3. http://pragprog.com/magazines/2010-08/page-objects-in-python
