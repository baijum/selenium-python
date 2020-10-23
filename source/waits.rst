.. _waits:

Waits
-----

These days, most of the web apps are using AJAX techniques.  When a page is
loaded by the browser, the elements within that page may load at different time
intervals.  This makes locating elements difficult: if an element is not yet
present in the DOM, a locate function will raise an `ElementNotVisibleException`
exception.  Using waits, we can solve this issue.  Waiting provides some slack
between actions performed - mostly locating an element or any other operation
with the element.

Selenium Webdriver provides two types of waits - implicit & explicit.  An
explicit wait makes WebDriver wait for a certain condition to occur before
proceeding further with execution.  An implicit wait makes WebDriver poll the
DOM for a certain amount of time when trying to locate an element.


Explicit Waits
~~~~~~~~~~~~~~

An explicit wait is a code you define to wait for a certain condition to occur
before proceeding further in the code.  The extreme case of this is
time.sleep(), which sets the condition to an exact time period to wait.  There
are some convenience methods provided that help you write code that will wait
only as long as required.  WebDriverWait in combination with ExpectedCondition
is one way this can be accomplished.

::

  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  driver = webdriver.Firefox()
  driver.get("http://somedomain/url_that_delays_loading")
  try:
      element = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, "myDynamicElement"))
      )
  finally:
      driver.quit()


In the code above, Selenium will wait for a maximum of 10 seconds for an element
matching the given criteria to be found.  If no element is found in that time, a
TimeoutException is thrown.  By default, WebDriverWait calls the
ExpectedCondition every 500 milliseconds until it returns success.
ExpectedCondition will return `true` (Boolean) in case of success or `not null`
if it fails to locate an element.

**Expected Conditions**

There are some common conditions that are frequently of use when automating web
browsers.  Listed below are the names of each. Selenium Python binding provides
some `convenience methods
<http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions>`_
so you don't have to code an expected_condition class yourself or create your
own utility package for them.

- title_is
- title_contains
- presence_of_element_located
- visibility_of_element_located
- visibility_of
- presence_of_all_elements_located
- text_to_be_present_in_element
- text_to_be_present_in_element_value
- frame_to_be_available_and_switch_to_it
- invisibility_of_element_located
- element_to_be_clickable
- staleness_of
- element_to_be_selected
- element_located_to_be_selected
- element_selection_state_to_be
- element_located_selection_state_to_be
- alert_is_present

::

  from selenium.webdriver.support import expected_conditions as EC

  wait = WebDriverWait(driver, 10)
  element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

The expected_conditions module contains a set of predefined conditions to use
with WebDriverWait.

**Custom Wait Conditions**

You can also create custom wait conditions when none of the previous convenience
methods fit your requirements.  A custom wait condition can be created using a
class with `__call__` method which returns `False` when the condition doesn't
match.


::

  class element_has_css_class(object):
    """An expectation for checking that an element has a particular css class.

    locator - used to find the element
    returns the WebElement once it has the particular css class
    """
    def __init__(self, locator, css_class):
      self.locator = locator
      self.css_class = css_class

    def __call__(self, driver):
      element = driver.find_element(*self.locator)   # Finding the referenced element
      if self.css_class in element.get_attribute("class"):
          return element
      else:
          return False
          
  # Wait until an element with id='myNewInput' has class 'myCSSClass'
  wait = WebDriverWait(driver, 10)
  element = wait.until(element_has_css_class((By.ID, 'myNewInput'), "myCSSClass"))


.. note:: **polling2 Library**

   You may also consider using `polling2
   <https://polling2.readthedocs.io/en/latest/examples.html#polling-for-selenium-webdriver-elements>`_
   lirbary which you need to install separately.

Implicit Waits
~~~~~~~~~~~~~~

An implicit wait tells WebDriver to poll the DOM for a certain amount of time
when trying to find any element (or elements) not immediately available.  The
default setting is 0 (zero).  Once set, the implicit wait is set for the life of
the WebDriver object.

::

  from selenium import webdriver

  driver = webdriver.Firefox()
  driver.implicitly_wait(10) # seconds
  driver.get("http://somedomain/url_that_delays_loading")
  myDynamicElement = driver.find_element_by_id("myDynamicElement")
