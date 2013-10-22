.. _api:

WebDriver API
-------------

.. note::

   This is not an official documentation.  Official API documentation
   is available `here
   <http://selenium.googlecode.com/svn/trunk/docs/api/py/index.html>`_.

This chapter cover all the interfaces of Selenium WebDriver.


**Recommended Import Style**

The API definitions in this chapter shows the absolute location of classes.
However the recommended import style is as given below::

  from selenium import webdriver

Then, you can access the classes like this::

  webdriver.Firefox
  webdriver.FirefoxProfile
  webdriver.Chrome
  webdriver.ChromeOptions
  webdriver.Ie
  webdriver.Opera
  webdriver.PhantomJS
  webdriver.Remote
  webdriver.DesiredCapabilities
  webdriver.ActionChains
  webdriver.TouchActions
  webdriver.Proxy

The special keys class (``Keys``) can be imported like this::

  from selenium.webdriver.common.keys import Keys

The exception classes can be imported like this (Replace the ``TheNameOfTheExceptionClass`` with actual class name given below)::

  from selenium.common.exceptions import [TheNameOfTheExceptionClass]

**Conventions used in the API**

Some attributes are callable (or methods) and others are non-callable
(properties).  All the callable attributes are ending with round
brackets.

Here is an example for property:

  - current_url

    URL of the current loaded page.

    Usage::

      driver.current_url

Here is an example for a method:

  - close()

    Closes the current window.

    Usage::

      driver.close()


Exceptions
~~~~~~~~~~

.. automodule:: selenium.common.exceptions
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:


Action Chains
~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.common.action_chains
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:


Alerts
~~~~~~

.. automodule:: selenium.webdriver.common.alert
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:


Special Keys
~~~~~~~~~~~~

.. automodule:: selenium.webdriver.common.keys
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:


Firefox WebDriver
~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.firefox.webdriver
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:

Chrome WebDriver
~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.chrome.webdriver
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:


Remote WebDriver
~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.remote.webdriver
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:


WebElement
~~~~~~~~~~

.. automodule:: selenium.webdriver.remote.webelement
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:

UI Support
~~~~~~~~~~

.. automodule:: selenium.webdriver.support.select
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:

.. automodule:: selenium.webdriver.support.wait
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:

Color Support
~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.support.color
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:

Expected conditions Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.support.expected_conditions
   :members:
   :undoc-members:
   :member-order: groupwise
   :show-inheritance:
