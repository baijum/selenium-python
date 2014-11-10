.. _locating-elements:

Locating Elements
-----------------

There are vaious strategies to locate elements in a page.  You can use
the most appropriate one for your case.  Selenium provides the following
methods to locate elements in a page:

- `find_element_by_id`
- `find_element_by_name`
- `find_element_by_xpath`
- `find_element_by_link_text`
- `find_element_by_partial_link_text`
- `find_element_by_tag_name`
- `find_element_by_class_name`
- `find_element_by_css_selector`


**To find multiple elements (these methods will return a list):**

- `find_elements_by_name`
- `find_elements_by_xpath`
- `find_elements_by_link_text`
- `find_elements_by_partial_link_text`
- `find_elements_by_tag_name`
- `find_elements_by_class_name`
- `find_elements_by_css_selector`


Apart from the public methods given above, there are two private
methods which might be useful with locators in page objects.  These
are the two private methods: `find_element` and `find_elements`.

Example usage::

  from selenium.webdriver.common.by import By

  driver.find_element(By.XPATH, '//button[text()="Some text"]')
  driver.find_elements(By.XPATH, '//button')


These are the attributes available for `By` class::

    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"


Locating by Id
~~~~~~~~~~~~~~

Use this when you know `id` attribute of an element.  With this
strategy, the first element with the `id` attribute value matching the
location will be returned.  If no element has a matching `id`
attribute, a ``NoSuchElementException`` will be raised.

For instance, consider this page source::

  <html>
   <body>
    <form id="loginForm">
     <input name="username" type="text" />
     <input name="password" type="password" />
     <input name="continue" type="submit" value="Login" />
    </form>
   </body>
  <html>

The form element can be located like this::

  login_form = driver.find_element_by_id('loginForm')


Locating by Name
~~~~~~~~~~~~~~~~

Use this when you know `name` attribute of an element.  With this
strategy, the first element with the `name` attribute value matching
the location will be returned.  If no element has a matching `name`
attribute, a ``NoSuchElementException`` will be raised.

For instance, conside this page source::

   <html>
    <body>
     <form id="loginForm">
      <input name="username" type="text" />
      <input name="password" type="password" />
      <input name="continue" type="submit" value="Login" />
      <input name="continue" type="button" value="Clear" />
     </form>
   </body>
   <html>

The username & password elements can be located like this::

  username = driver.find_element_by_name('username')
  password = driver.find_element_by_name('password')

This will give the "Login" button as it occur before the "Clear"
button::

  continue = driver.find_element_by_name('continue')


Locating by XPath
~~~~~~~~~~~~~~~~~

XPath is the language used for locating nodes in an XML document.  As
HTML can be an implementation of XML (XHTML), Selenium users can
leverage this powerful language to target elements in their web
applications.  XPath extends beyond (as well as supporting) the simple
methods of locating by id or name attributes, and opens up all sorts
of new possibilities such as locating the third checkbox on the page.

One of the main reasons for using XPath is when you don't have a
suitable id or name attribute for the element you wish to locate.  You
can use XPath to either locate the element in absolute terms (not
advised), or relative to an element that does have an id or name
attribute.  XPath locators can also be used to specify elements via
attributes other than id and name.

Absolute XPaths contain the location of all elements from the root
(html) and as a result are likely to fail with only the slightest
adjustment to the application.  By finding a nearby element with an id
or name attribute (ideally a parent element) you can locate your
target element based on the relationship.  This is much less likely to
change and can make your tests more robust.

For instance, conside this page source::

   <html>
    <body>
     <form id="loginForm">
      <input name="username" type="text" />
      <input name="password" type="password" />
      <input name="continue" type="submit" value="Login" />
      <input name="continue" type="button" value="Clear" />
     </form>
   </body>
   <html>

The form elements can be located like this::

  login_form = driver.find_element_by_xpath("/html/body/form[1]")
  login_form = driver.find_element_by_xpath("//form[1]")
  login_form = driver.find_element_by_xpath("//form[@id='loginForm']")


1. Absolute path (would break if the HTML was changed only slightly)

2. First form element in the HTML

3. The form element with attribute named `id` and the value `loginForm`

The username element can be located like this::

  username = driver.find_element_by_xpath("//form[input/@name='username']")
  username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
  username = driver.find_element_by_xpath("//input[@name='username']")

1. First form element with an input child element with attribute named
   `name` and the value `username`

2. First input child element of the form element with attribute named
   `id` and the value `loginForm`

3. First input element with attribute named 'name' and the value
   `username`

The "Clear" button element can be located like this::

  clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
  clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")


1. Input with attribute named `name` and the value `continue` and
   attribute named `type` and the value `button`

2. Fourth input child element of the form element with attribute named
   `id` and value `loginForm`

These examples cover some basics, but in order to learn more, the
following references are recommended:

* `W3Schools XPath Tutorial <http://www.w3schools.com/Xpath/>`_
* `W3C XPath Recommendation <http://www.w3.org/TR/xpath>`_
* `XPath Tutorial
  <http://www.zvon.org/comp/r/tut-XPath_1.html>`_
  - with interactive examples.

There are also a couple of very useful Add-ons that can assist in
discovering the XPath of an element:

* `XPath Checker
  <https://addons.mozilla.org/en-US/firefox/addon/1095?id=1095>`_ -
  suggests XPath and can be used to test XPath results.
* `Firebug <https://addons.mozilla.org/en-US/firefox/addon/1843>`_ -
  XPath suggestions are just one of the many powerful features of this
  very useful add-on.
* `XPath Helper
  <https://chrome.google.com/webstore/detail/hgimnogjllphhhkhlmebbmlgjoejdpjl>`_ -
  for Google Chrome


Locating Hyperlinks by Link Text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when you know link text used within an anchor tag.  With this
strategy, the first element with the link text value matching the
location will be returned.  If no element has a matching link text
attribute, a ``NoSuchElementException`` will be raised.

For instance, consider this page source::

  <html>
   <body>
    <p>Are you sure you want to do this?</p>
    <a href="continue.html">Continue</a>
    <a href="cancel.html">Cancel</a>
  </body>
  <html>

The continue.html link can be located like this::

  continue_link = driver.find_element_by_link_text('Continue')
  continue_link = driver.find_element_by_partial_link_text('Conti')


Locating Elements by Tag Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when you want to locate an element by tag name. With this
strategy, the first element with the given tag name will be returned.
If no element has a matching tag name, a ``NoSuchElementException``
will be raised.

For instance, conside this page source::

  <html>
   <body>
    <h1>Welcome</h1>
    <p>Site content goes here.</p>
  </body>
  <html>

The heading (h1) element can be located like this::

  heading1 = driver.find_element_by_tag_name('h1')


Locating Elements by Class Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when you want to locate an element by class attribute name.
With this strategy, the first element with the matching class attribute
name will be returned.  If no element has a matching class attribute name,
a ``NoSuchElementException`` will be raised.

For instance, consider this page source::

  <html>
   <body>
    <p class="content">Site content goes here.</p>
  </body>
  <html>

The "p" element can be located like this::

  content = driver.find_element_by_class_name('content')

Locating Elements by CSS Selectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when you want to locate an element by CSS selector syntaxt.
With this strategy, the first element with the matching CSS selector
will be returned.  If no element has a matching CSS selector,
a ``NoSuchElementException`` will be raised.

For instance, consider this page source::

  <html>
   <body>
    <p class="content">Site content goes here.</p>
  </body>
  <html>

The "p" element can be located like this::

  content = driver.find_element_by_css_selector('p.content')

`Sauce Labs has good documentation <http://saucelabs.com/resources/selenium/css-selectors>`_
on CSS selectors.
