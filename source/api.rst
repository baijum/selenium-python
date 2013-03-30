.. _api:

WebDriver API
-------------

.. note::

   This is not an official documentation.  Official API documentation
   is available `here
   <http://selenium.googlecode.com/svn/trunk/docs/api/py/index.html>`_.

This chapter cover all the interfaces of Selenium WebDriver.

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

