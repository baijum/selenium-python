Appendix: Frequently asked questions
------------------------------------


How to use ChromeDriver ?
~~~~~~~~~~~~~~~~~~~~~~~~~

Download the latest `chromdriver from download page
<http://code.google.com/p/chromium/downloads/list>`_.  Unzip the
file::

  unzip chromedriver_linux32_x.x.x.x.zip

You should see a ``chromedriver`` executable.  Now you can instance of
Chrome WebDriver like this::

  driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

The rest of the example should work as given in other other
documentation.

Does Selenium 2 supports XPath 2.0 ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ref: http://seleniumhq.org/docs/03_webdriver.html#how-xpath-works-in-webdriver

Selenium delegate XPath queries down to the browser's own XPath
engine, so Selenium support XPath supports whatever the browser
supports.  In browsers which don't have native XPath engines (IE
6,7,8), Selenium support XPath 1.0 only.


How to scroll down to the bottom of a page ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ref: http://blog.varunin.com/2011/08/scrolling-on-pages-using-selenium.html

You can use the `execute_script` method to execute javascript on the
loaded page.  So, you can call the JavaScript API to scroll to the
bottom or any other position of a page.

Here is an example to scroll to the bottom of a page::

  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

The `window <http://www.w3schools.com/jsref/obj_window.asp>`_ object
in DOM has a `scrollTo
<http://www.w3schools.com/jsref/met_win_scrollto.asp>`_ method to
scroll to any position of an opened window.  The `scrollHeight
<http://www.w3schools.com/jsref/dom_obj_all.asp>`_ is a common
property for all elements.  The `document.body.scrollHeight` will give
the height of the entire body of the page.

