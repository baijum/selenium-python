.. _locating-elements:

Locating Elements
-----------------

There are various strategies to locate elements in a page.  You can use the most
appropriate one for your case.  Selenium provides the following method to
locate elements in a page:

- `find_element`

**To find multiple elements (these methods will return a list):**

- `find_elements`


Example usage::

  from selenium.webdriver.common.by import By

  driver.find_element(By.XPATH, '//button[text()="Some text"]')
  driver.find_elements(By.XPATH, '//button')

The attributes available for the `By` class are used to locate elements on a page.
These are the attributes available for `By` class::

    ID = "id"
    NAME = "name"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"

The 'By' class is used to specify which attribute is used to locate elements on a page.
These are the various ways the attributes are used to locate elements on a page::

  find_element(By.ID, "id")
  find_element(By.NAME, "name")
  find_element(By.XPATH, "xpath")
  find_element(By.LINK_TEXT, "link text")
  find_element(By.PARTIAL_LINK_TEXT, "partial link text")
  find_element(By.TAG_NAME, "tag name")
  find_element(By.CLASS_NAME, "class name")
  find_element(By.CSS_SELECTOR, "css selector")

If you want to locate several elements with the same attribute replace find_element with find_elements.


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

  login_form = driver.find_element(By.ID, 'loginForm')


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

  username = driver.find_element(By.NAME, 'username')
  password = driver.find_element(By.NAME, 'password')

This will give the "Login" button as it occurs before the "Clear" button::

  continue = driver.find_element(By.NAME, 'continue')


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

The form elements can be located like this::

  login_form = driver.find_element(By.XPATH, "/html/body/form[1]")
  login_form = driver.find_element(By.XPATH, "//form[1]")
  login_form = driver.find_element(By.XPATH, "//form[@id='loginForm']")


1. Absolute path (would break if the HTML was changed only slightly)

2. First form element in the HTML

3. The form element with attribute `id` set to `loginForm`

The username element can be located like this::

  username = driver.find_element(By.XPATH, "//form[input/@name='username']")
  username = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[1]")
  username = driver.find_element(By.XPATH, "//input[@name='username']")

1. First form element with an input child element with `name` set to `username`

2. First input child element of the form element with attribute `id` set to
   `loginForm`

3. First input element with attribute `name` set to `username`

The "Clear" button element can be located like this::

  clear_button = driver.find_element(By.XPATH, "//input[@name='continue'][@type='button']")
  clear_button = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[4]")


1. Input with attribute `name` set to `continue` and attribute `type` set to
   `button`

2. Fourth input child element of the form element with attribute `id` set to
   `loginForm`

These examples cover some basics, but in order to learn more, the following
references are recommended:

* `W3Schools XPath Tutorial <https://www.w3schools.com/xml/xpath_intro.asp>`_
* `W3C XPath Recommendation <http://www.w3.org/TR/xpath>`_
* `XPath Tutorial
  <http://www.zvon.org/comp/r/tut-XPath_1.html>`_
  - with interactive examples.

Here is a couple of very useful Add-ons that can assist in discovering the XPath
of an element:

* `xPath Finder
  <https://addons.mozilla.org/en-US/firefox/addon/xpath_finder>`_ -
  Plugin to get the elements xPath.
* `XPath Helper
  <https://chrome.google.com/webstore/detail/hgimnogjllphhhkhlmebbmlgjoejdpjl>`_ -
  for Google Chrome


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

  continue_link = driver.find_element(By.LINK_TEXT, 'Continue')
  continue_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')


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

  heading1 = driver.find_element(By.TAG_NAME, 'h1')


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

  content = driver.find_element(By.CLASS_NAME, 'content')

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

  content = driver.find_element(By.CSS_SELECTOR, 'p.content')

`Sauce Labs has good documentation
<https://saucelabs.com/resources/articles/selenium-tips-css-selectors>`_ on CSS
selectors.
