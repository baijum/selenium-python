.. _api:

WebDriver API
-------------

.. note::

   This is not an official documentation.  Official API documentation
   is available `here
   <https://seleniumhq.github.io/selenium/docs/api/py/api.html>`_.

This chapter covers all the interfaces of Selenium WebDriver.


**Recommended Import Style**

The API definitions in this chapter show the absolute location of classes.
However, the recommended import style is as given below::

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

The exception classes can be imported like this (Replace the ``TheNameOfTheExceptionClass``
with the actual class name given below)::

  from selenium.common.exceptions import [TheNameOfTheExceptionClass]

**Conventions used in the API**

Some attributes are callable (or methods) and others are non-callable
(properties).  All the callable attributes are ending with round
brackets.

Here is an example for property:

  - current_url

    URL of the currently loaded page.

    Usage::

      driver.current_url

Here is an example of a method:

  - close()

    Closes the current window.

    Usage::

      driver.close()


Exceptions
~~~~~~~~~~

.. automodule:: selenium.common.exceptions
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:


Action Chains
~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.common.action_chains
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:


Alerts
~~~~~~

.. automodule:: selenium.webdriver.common.alert
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:


Special Keys
~~~~~~~~~~~~

.. automodule:: selenium.webdriver.common.keys
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:


Locate elements By
~~~~~~~~~~~~~~~~~~

These are the attributes which can be used to locate elements.  See
the :ref:`locating-elements` chapter for example usages.

.. automodule:: selenium.webdriver.common.by
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:


Desired Capabilities
~~~~~~~~~~~~~~~~~~~~

See the :ref:`selenium-remote-webdriver` section for example usages of desired capabilities.

.. automodule:: selenium.webdriver.common.desired_capabilities
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Touch Actions
~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.common.touch_actions
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Proxy
~~~~~

.. automodule:: selenium.webdriver.common.proxy
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:


Utilities
~~~~~~~~~

.. automodule:: selenium.webdriver.common.utils
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Service
~~~~~~~

.. automodule:: selenium.webdriver.common.service
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Application Cache
~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.common.html5.application_cache
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:


Firefox WebDriver
~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.firefox.webdriver
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Firefox WebDriver Options
~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.firefox.options
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Firefox WebDriver Profile
~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.firefox.firefox_profile
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Firefox WebDriver Binary
~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.firefox.firefox_binary
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Firefox WebDriver Extension Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.firefox.extension_connection
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Chrome WebDriver
~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.chrome.webdriver
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Chrome WebDriver Options
~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.chrome.options
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:


Chrome WebDriver Service
~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.chrome.service
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Remote WebDriver
~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.remote.webdriver
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Remote WebDriver WebElement
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.remote.webelement
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Remote WebDriver Command
~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.remote.command
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Remote WebDriver Error Handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.remote.errorhandler
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Remote WebDriver Mobile
~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.remote.mobile
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Remote WebDriver Remote Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.remote.remote_connection
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Remote WebDriver Utils
~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.remote.utils
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:


Internet Explorer WebDriver
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.ie.webdriver
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Android WebDriver
~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.android.webdriver
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Opera WebDriver
~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.opera.webdriver
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

PhantomJS WebDriver
~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.phantomjs.webdriver
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

PhantomJS WebDriver Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.phantomjs.service
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Safari WebDriver
~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.safari.webdriver
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Safari WebDriver Service
~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.safari.service
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Select Support
~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.support.select
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Wait Support
~~~~~~~~~~~~

.. automodule:: selenium.webdriver.support.wait
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Color Support
~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.support.color
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Event Firing WebDriver Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.support.event_firing_webdriver
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Abstract Event Listener Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.support.abstract_event_listener
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:

Expected conditions Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: selenium.webdriver.support.expected_conditions
   :members:
   :undoc-members:
   :special-members: __init__
   :member-order: groupwise
   :show-inheritance:
