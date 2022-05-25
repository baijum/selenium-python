.. _locating-elements:

Locating Elements
-----------------

::

   Note: If you are using Selenium 4.0.0 or higher, there is a deprecation notice for find_element_by_* methods. 
   Please use find_element(By.*) instead.

There are various strategies to locate elements in a page.  You can use the most
appropriate one for your case.  Selenium provides the following methods to
locate elements in a page. :ref:`1<Deprecation of locator methods>`

.. list-table:: Available Locator Methods
   :header-rows: 1

   * - HTML locator
     - Description
     - Legacy method (single element)
     - Legacy method (multiples/list)
     - Selenium 4.0.0+
   * - class name
     - css selector
     - id
     - link text
     - partial link text
     - name
     - tag name
     - xpath
   * - Locate element whose class name contains the search value. Compound class names are not permitted.
     - Locate element matching a CSS selector
     - Locate element whose ID attribute matches the search value
     - Locate anchor element whose visible text matches the search value
     - Locate anchor element whose visible text contains the search value
     - Locate element whose NAME attribute matches the search value
     - Locate element whose tag name matches the search value
     - Locate element matching an XPath expression
   * - find_element_by_class_name
     - find_element_by_css_selector
     - find_element_by_id
     - find_element_by_link_text
     - find_element_by_partial_link_text
     - find_element_by_name
     - find_element_by_tag_name
     - find_element_by_xpath
   * - find_elements_by_class_name
     - find_elements_by_css_selector
     - find_elements_by_id
     - find_elements_by_link_text
     - find_elements_by_partial_link_text
     - find_elements_by_name
     - find_elements_by_tag_name
     - find_elements_by_xpath
   * - By.CLASS_NAME
     - By.CSS_SELECTOR
     - By.ID
     - By.LINK_TEXT
     - By.PARTIAL_TEXT
     - By.NAME
     - By.TAG_NAME
     - By.XPATH

Example usage::

  from selenium.webdriver.common.by import By
  
  myButton = driver.find_element(By.XPATH, '//button[text()="Some text"]')
  # find single button (only or first instance)
  
  foobarRows = driver.find_elements(By.XPATH, '//table[@id="foobar"]/tbody/tr')
  # list all rows in `table` element with attribute `id` set to 'foobar'


Locating by Id
~~~~~~~~~~~~~~

Use this when you know the `id` attribute of an element.  With this strategy,
the first element with a matching `id` attribute will be returned.  If no
element has a matching `id` attribute, a ``NoSuchElementException`` will be
raised.

For instance, consider this page source::

  <html>
   <body>
    <form id="loginForm">
     <input name="username" type="text" />
     <input name="password" type="password" />
     <input name="continue" type="submit" value="Login" />
    </form>
   </body>
  </html>

The form element can be located like this::

  login_form = driver.find_element_by_id('loginForm')
  
  login_form = driver.find_element(By.ID, 'loginForm')
  # (v4.0.0+) Alternate method


Locating by Name
~~~~~~~~~~~~~~~~

Use this when you know the `name` attribute of an element.  With this strategy,
the first element with a matching `name` attribute will be returned.  If no
element has a matching `name` attribute, a ``NoSuchElementException`` will be
raised.

For instance, consider this page source::

   <html>
    <body>
     <form id="loginForm">
      <input name="username" type="text" />
      <input name="password" type="password" />
      <input name="continue" type="submit" value="Login" />
      <input name="continue" type="button" value="Clear" />
     </form>
   </body>
   </html>

The username & password elements can be located like this::

  username = driver.find_element_by_name('username')
  password = driver.find_element_by_name('password')

This will give the "Login" button as it occurs before the "Clear" button::

  continue = driver.find_element_by_name('continue')
  
  continue = driver.find_element(By.NAME, 'continue')
  # (v4.0.0+) Alternate method


Locating by XPath
~~~~~~~~~~~~~~~~~

XPath is the language used for locating nodes in an XML document.  As HTML can
be an implementation of XML (XHTML), Selenium users can leverage this powerful
language to target elements in their web applications.  XPath supports the
simple methods of locating by id or name attributes and extends them by opening
up all sorts of new possibilities such as locating the third checkbox on the
page.

One of the main reasons for using XPath is when you don't have a suitable id or
name attribute for the element you wish to locate.  You can use XPath to either
locate the element in absolute terms (not advised), or relative to an element
that does have an id or name attribute.  XPath locators can also be used to
specify elements via attributes other than id and name.

Absolute XPaths contain the location of all elements from the root (html) and as
a result are likely to fail with only the slightest adjustment to the
application.  By finding a nearby element with an id or name attribute (ideally
a parent element) you can locate your target element based on the relationship.
This is much less likely to change and can make your tests more robust.

For instance, consider this page source::

   <html>
    <body>
     <form id="loginForm">
      <input name="username" type="text" />
      <input name="password" type="password" />
      <input name="continue" type="submit" value="Login" />
      <input name="continue" type="button" value="Clear" />
     </form>
   </body>
   </html>

The form element can be located like this: :ref:`2<Absolute path warning>`)::

   login_form = driver.find_element_by_xpath("/html/body/form[1]")
   # Find form element by absolute path
   
   login_form = driver.find_element_by_xpath("//form[1]")
   # Find the first form element in the html
   
   login_form = driver.find_element_by_xpath("//form[@id='loginForm']")
   # Find the form element with attribute `id` set to `loginForm`
   
   login_form = driver.find_element(By.XPATH, "//form[@id='loginForm']")
   # (v4.0.0+) Find first `input` element with attribute `name` set to `username`

The username element can be located like this::

    username = driver.find_element_by_xpath("//form[input/@name='username']")
    # Find first `form` element with an `input` child element with `name` set to `username`
    
    username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
    # Find first `input` child element of the `form` element with attribute `id` set to `loginForm`
    
    username = driver.find_element_by_xpath("//input[@name='username']")
    # Find first `input` element with attribute `name` set to `username`
    
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    # (v4.0.0+) Find first `input` element with attribute `name` set to `username`

The "Clear" button element can be located like this::

  clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
  # Find `input` with attribute `name` set to `continue` and attribute `type` set to `button`
  
  clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")
  # Find fourth `input` child of the `form` element with attribute `id` set to `loginForm`
  
  clear_button = driver.find_element(By.XPATH, "//input[@name='continue'][@type='button']")
  # (v4.0.0+) Find `input` element with attribute `type` set to `button` and `name` set to `continue`

These examples cover a few basics only. To learn more, the following references are recommended:

* `W3Schools XPath Tutorial <https://www.w3schools.com/xml/xpath_intro.asp>`_
* `W3C XPath Recommendation <http://www.w3.org/TR/xpath>`_
* `XPath Tutorial
  <http://www.zvon.org/comp/r/tut-XPath_1.html>`_
  - with interactive examples.

Additionally, there are useful browser extensions to assist in discovering XPaths:

* `xPath Finder
  <https://addons.mozilla.org/en-US/firefox/addon/xpath_finder>`_ -
  for Firefox
* `XPath Helper
  <https://chrome.google.com/webstore/detail/hgimnogjllphhhkhlmebbmlgjoejdpjl>`_ -
  for Google Chrome
* `Ruto XPath Finder
  <https://chrome.google.com/webstore/detail/ruto-xpath-finder/ilcoelkkcokgeeijnopjnolmmighnppp>`_ -
  for Google Chrome, specifically engineered for use with Selenium
* `SelectorsHub
  <https://selectorshub.com/selectorshub/>`_ -
  for most major browsers (Chrome, Safari, Firefox, Edge)


Locating Hyperlinks by Link Text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when you know the link text used within an anchor tag.  With this
strategy, the first element with the link text matching the provided value will
be returned.  If no element has a matching link text attribute, a
``NoSuchElementException`` will be raised.

For instance, consider this page source::

  <html>
   <body>
    <p>Are you sure you want to do this?</p>
    <a href="continue.html">Continue</a>
    <a href="cancel.html">Cancel</a>
  </body>
  </html>

The continue.html link can be located like this::

  continue_link = driver.find_element_by_link_text('Continue')
  continue_link = driver.find_element_by_partial_link_text('Conti')
  
  continue_link = driver.find_element(By.LINK_TEXT, 'Continue')
  continue_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
  # (v4.0.0+) Alternate methods


Locating Elements by Tag Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when you want to locate an element by tag name.  With this strategy,
the first element with the given tag name will be returned.  If no element has a
matching tag name, a ``NoSuchElementException`` will be raised.

For instance, consider this page source::

  <html>
   <body>
    <h1>Welcome</h1>
    <p>Site content goes here.</p>
  </body>
  </html>

The heading (h1) element can be located like this::

  heading1 = driver.find_element_by_tag_name('h1')
  
  heading1 = driver.find_element(By.TAG_NAME, 'h1')
  # (v4.0.0+) Alternate method


Locating Elements by Class Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when you want to locate an element by class name.  With this strategy,
the first element with the matching class name attribute will be returned.  If
no element has a matching class name attribute, a ``NoSuchElementException``
will be raised.

For instance, consider this page source::

  <html>
   <body>
    <p class="content">Site content goes here.</p>
  </body>
  </html>

The "p" element can be located like this::

  content = driver.find_element_by_class_name('content')
  
  content = driver.find_element(By.CLASS_NAME, 'content')
  # (v4.0.0+) Alternate method

Locating Elements by CSS Selectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when you want to locate an element using `CSS selector
<https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors>`_
syntax.  With this strategy, the first element matching the given CSS selector
will be returned.  If no element matches the provided CSS selector, a
``NoSuchElementException`` will be raised.

For instance, consider this page source::

  <html>
   <body>
    <p class="content">Site content goes here.</p>
  </body>
  </html>

The "p" element can be located like this::

   content = driver.find_element_by_css_selector('p.content')
   
   content = driver.find_element(By.CSS_SELECTOR, 'p.content')
   # (v4.0.0+) Alternate method

`Sauce Labs has good documentation
<https://saucelabs.com/resources/articles/selenium-tips-css-selectors>`_ on CSS
selectors.

Footnotes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _Deprecation of locator methods
[1] If you are using Selenium 4.0.0 or higher, there is a deprecation notice for find_element_by\_* methods. 
Please use find_element(By.*) instead.

.. _Absolute path warning
[2] Use absolute paths only if necessary. Methods will break if the HTML is changed even slightly.
