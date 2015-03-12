.. _waits:

Waits
-----

These days most of the web apps are using AJAX techniques.  When a
page is loaded to browser, the elements within that page may load at
different time intervals.  This makes locating elements difficult, if
the element is not present in the DOM, it will raise
`ElementNotVisibleException` exception.  Using waits, we can solve
this issue.  Waiting provides some time interval between actions
performed - mostly locating element or any other operation with the
element.

Selenium Webdriver provides two types of waits - implicit & explicit.
An explicit wait makes WebDriver to wait for a certain condition to
occur before proceeding further with executions.  An implicit wait
makes WebDriver to poll the DOM for a certain amount of time when
trying to locate an element.


Explicit Waits
~~~~~~~~~~~~~~

An explicit waits is code you define to wait for a certain condition
to occur before proceeding further in the code.  The worst case of
this is time.sleep(), which sets the condition to an exact time period
to wait.  There are some convenience methods provided that help you
write code that will wait only as long as required.  WebDriverWait in
combination with ExpectedCondition is one way this can be
accomplished.

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


This waits up to 10 seconds before throwing a TimeoutException or if
it finds the element will return it in 0 - 10 seconds.  WebDriverWait
by default calls the ExpectedCondition every 500 milliseconds until it
returns successfully.  A successful return is for ExpectedCondition
type is Boolean return true or not null return value for all other
ExpectedCondition types.

**Expected Conditions**

There are some common conditions that are frequent when
automating web browsers.  Listed below are Implementations of
each. Selenium Python binding provides some convienence methods so you
don't have to code an expected_condition class yourself or create your
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
- element_to_be_clickable - it is Displayed and Enabled.
- staleness_of
- element_to_be_selected
- element_located_to_be_selected
- element_selection_state_to_be
- element_located_selection_state_to_be
- alert_is_present

::

  from selenium.webdriver.support import expected_conditions as EC

  wait = WebDriverWait(driver, 10)
  element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))

The expected_conditions module contains a set of predefined conditions
to use with WebDriverWait.


Implicit Waits
~~~~~~~~~~~~~~

An implicit wait is to tell WebDriver to poll the DOM for a certain
amount of time when trying to find an element or elements if they are
not immediately available.  The default setting is 0.  Once set, the
implicit wait is set for the life of the WebDriver object instance.

::

  from selenium import webdriver

  driver = webdriver.Firefox()
  driver.implicitly_wait(10) # seconds
  driver.get("http://somedomain/url_that_delays_loading")
  myDynamicElement = driver.find_element_by_id("myDynamicElement")
