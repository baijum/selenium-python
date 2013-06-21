.. _faq:

Appendix: Frequently asked questions
------------------------------------

Another FAQ: https://code.google.com/p/selenium/wiki/FrequentlyAskedQuestions

How to use ChromeDriver ?
~~~~~~~~~~~~~~~~~~~~~~~~~

Download the latest `chromedriver from download page
<https://code.google.com/p/chromedriver/downloads/list>`_.  Unzip the
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

How to auto save files using custom Firefox profile ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ref: http://stackoverflow.com/questions/1176348/access-to-file-download-dialog-in-firefox
Ref: http://blog.codecentric.de/en/2010/07/file-downloads-with-selenium-mission-impossible/

The first step is to identify the type of file you want to auto save.

To identify the content type you want to download automatically, you
can use `curl <http://curl.haxx.se/>`_::

  curl -I URL | grep "Content-Type"

Another way to find content type is using the `requests
<http://python-requests.org>`_ module, you can use it like this::

  import requests
  print requests.head('http://www.python.org').headers['content-type']

Once the content type is identified, you can use it to set the firefox
profile preference: ``browser.helperApps.neverAsk.saveToDisk``

Here is an example::

  import os

  from selenium import webdriver

  fp = webdriver.FirefoxProfile()

  fp.set_preference("browser.download.folderList",2)
  fp.set_preference("browser.download.manager.showWhenStarting",False)
  fp.set_preference("browser.download.dir", os.getcwd())
  fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

  browser = webdriver.Firefox(firefox_profile=fp)
  browser.get("http://pypi.python.org/pypi/selenium")
  browser.find_element_by_partial_link_text("selenium-2").click()

In the above example, ``application/octet-stream`` is used as the
content type.

The ``browser.download.dir`` option specify the directory where you
want to download the files.

How to use firebug with Firefox ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First download the Firebug XPI file, later you call the
``add_extension`` method available for the firefox profile::

  from selenium import webdriver

  fp = webdriver.FirefoxProfile()

  fp.add_extension(extension='firebug-1.8.4.xpi')
  fp.set_preference("extensions.firebug.currentVersion", "1.8.4") #Avoid startup screen
  browser = webdriver.Firefox(firefox_profile=fp)

