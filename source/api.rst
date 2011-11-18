.. _api:

API
---

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

**module:** selenium.common.exceptions


- class WebDriverException(msg=None, screen=None, stacktrace=None)

  base: Exception


- class ErrorInResponseException(response, msg)

  base: WebDriverException

  An error has occurred on the server side.

  This may happen when communicating with the firefox extension or the
  remote driver server.


- class InvalidSwitchToTargetException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

  The frame or window target to be switched doesn't exist.


- class NoSuchFrameException(msg=None, screen=None, stacktrace=None)

  base: InvalidSwitchToTargetException

  The frame target to be switched doesn't exist.

- class NoSuchWindowException(msg=None, screen=None, stacktrace=None)

  base: InvalidSwitchToTargetException

  The window target to be switched doesn't exist.

- class NoSuchElementException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

  The find_element_by_* methods can't find the element.


- class NoSuchAttributeException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

- class StaleElementReferenceException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

  Indicates that a reference to an element is now "stale" --- the
  element no longer appears on the DOM of the page.

- class InvalidElementStateException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

- class ElementNotVisibleException(msg=None, screen=None, stacktrace=None)

  base: InvalidElementStateException

  Thrown to indicate that although an element is present on the DOM,
  it is not visible, and so is not able to be interacted with.

- class ElementNotSelectableException(msg=None, screen=None, stacktrace=None)

  base: InvalidElementStateException

- class InvalidCookieDomainException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

  Thrown when attempting to add a cookie under a different domain
  than the current URL.

- class UnableToSetCookieException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

  Thrown when a driver fails to set a cookie.

- class RemoteDriverServerException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

- class TimeoutException(msg=None, screen=None, stacktrace=None)

  Thrown when a command does not complete in enough time.

Action Chains
~~~~~~~~~~~~~

**module:** selenium.webdriver.common.action_chains

- class ActionChains(driver)

  *driver:* The WebDriver instance which performs user actions.

  Generate user actions.  All actions are stored in the ActionChains
  object.  Call perform() to fire stored actions.

  - perform()

    Performs all stored actions.

  - click(on_element=None)

    Clicks an element.

    *on_element:* The element to click.  If None, clicks on current
    mouse position.

  - click_and_hold(on_element)

    Holds down the left mouse button on an element.

    *on_element:* The element to mouse down.  If None, clicks on
    current mouse position.

  - context_click(on_element)

    Performs a context-click (right click) on an element.

    *on_element:* The element to context-click.  If None, clicks on
    current mouse position.

  - double_click(on_element)

    Double-clicks an element.

    *on_element:* The element to double-click.  If None, clicks on
    current mouse position.

  - drag_and_drop(source, target)

    Holds down the left mouse button on the source element, then moves
    to the target element and releases the mouse button.

    *source:* The element to mouse down.

    *target:* The element to mouse up.

  - key_down(key, element=None)

    Sends a key press only, without releasing it.  Should only be used
    with modifier keys (Control, Alt and Shift).

    *key:* The modifier key to send. Values are defined in Keys class.

    *element:* The element to send keys.  If None, sends a key to
    current focused element.


  - key_up(key, element=None)

    Releases a modifier key.

    *key:* The modifier key to send. Values are defined in Keys class.

    *element:* The element to send keys.  If None, sends a key to
    current focused element.

  - move_by_offset(xoffset, yoffset)

    Moving the mouse to an offset from current mouse position.

    *xoffset:* X offset to move to.
    *yoffset:* Y offset to move to.

  - move_to_element(to_element)

    Moving the mouse to the middle of an element.

    *to_element:* The element to move to.

  - move_to_element_with_offset(to_element, xoffset, yoffset)

    Move the mouse by an offset of the specificed element.
    Offsets are relative to the top-left corner of the element.

    *to_element:* The element to move to.
    *xoffset:* X offset to move to.
    *yoffset:* Y offset to move to.

  - release(on_element)

    Releasing a held mouse button.

    *on_element:* The element to mouse up.

  - send_keys(`*keys_to_send`)

    Sends keys to current focused element.

    *keys_to_send:* The keys to send.

  - send_keys_to_element(self, element, `*keys_to_send`):

    Sends keys to an element.

    *element:* The element to send keys.
    *keys_to_send:* The keys to send.


Alerts
~~~~~~

**module:** selenium.webdriver.common.alert

- class Alert(driver)

  - text()

    Gets the text of the Alert

  - dismiss()

    Dismisses the alert available

  - accept()

    Accepts the alert available

  - send_keys(keysToSend)

    Send Keys to the Alert

    *keysToSend:* Any character.


Special Keys
~~~~~~~~~~~~

**module:** selenium.webdriver.common.keys

- class Keys()

  - NULL         = u'\ue000'
  - CANCEL       = u'\ue001' #  ^break
  - HELP         = u'\ue002'
  - BACK_SPACE   = u'\ue003'
  - TAB          = u'\ue004'
  - CLEAR        = u'\ue005'
  - RETURN       = u'\ue006'
  - ENTER        = u'\ue007'
  - SHIFT        = u'\ue008'
  - LEFT_SHIFT   = u'\ue008' #  alias
  - CONTROL      = u'\ue009'
  - LEFT_CONTROL = u'\ue009' #  alias
  - ALT          = u'\ue00a'
  - LEFT_ALT     = u'\ue00a' #  alias
  - PAUSE        = u'\ue00b'
  - ESCAPE       = u'\ue00c'
  - SPACE        = u'\ue00d'
  - PAGE_UP      = u'\ue00e'
  - PAGE_DOWN    = u'\ue00f'
  - END          = u'\ue010'
  - HOME         = u'\ue011'
  - LEFT         = u'\ue012'
  - ARROW_LEFT   = u'\ue012' # alias
  - UP           = u'\ue013'
  - ARROW_UP     = u'\ue013' # alias
  - RIGHT        = u'\ue014'
  - ARROW_RIGHT  = u'\ue014' #  alias
  - DOWN         = u'\ue015'
  - ARROW_DOWN   = u'\ue015' #  alias
  - INSERT       = u'\ue016'
  - DELETE       = u'\ue017'
  - SEMICOLON    = u'\ue018'
  - EQUALS       = u'\ue019'

  - NUMPAD0      = u'\ue01a' #  numbe pad  keys
  - NUMPAD1      = u'\ue01b'
  - NUMPAD2      = u'\ue01c'
  - NUMPAD3      = u'\ue01d'
  - NUMPAD4      = u'\ue01e'
  - NUMPAD5      = u'\ue01f'
  - NUMPAD6      = u'\ue020'
  - NUMPAD7      = u'\ue021'
  - NUMPAD8      = u'\ue022'
  - NUMPAD9      = u'\ue023'
  - MULTIPLY     = u'\ue024'
  - ADD          = u'\ue025'
  - SEPARATOR    = u'\ue026'
  - SUBTRACT     = u'\ue027'
  - DECIMAL      = u'\ue028'
  - DIVIDE       = u'\ue029'

  - F1           = u'\ue031' #  function  keys
  - F2           = u'\ue032'
  - F3           = u'\ue033'
  - F4           = u'\ue034'
  - F5           = u'\ue035'
  - F6           = u'\ue036'
  - F7           = u'\ue037'
  - F8           = u'\ue038'
  - F9           = u'\ue039'
  - F10          = u'\ue03a'
  - F11          = u'\ue03b'
  - F12          = u'\ue03c'

  - META         = u'\ue03d'
  - COMMAND      = u'\ue03d'


Firefox WebDriver
~~~~~~~~~~~~~~~~~

**module:** selenium.webdriver.firefox.webdriver

- class WebDriver(firefox_profile=None, firefox_binary=None, timeout=30)

  base: selenium.webdriver.remote.webdriver.WebDriver

  - save_screenshot(filename)

    Gets the screenshot of the current window. Returns False if there
    is any IOError, else returns True. Use full paths in your
    filename.


Chrome WebDriver
~~~~~~~~~~~~~~~~

**module:** selenium.webdriver.chrome.webdriver

Controls the ChromeDriver and allows you to drive the browser.  You
will need to download the ChromeDriver executable from:
http://code.google.com/p/selenium/downloads/list

- class WebDriver(executable_path="chromedriver", port=0)

  base: selenium.webdriver.remote.webdriver.WebDriver

  *executable_path:* path to the executable. If the default is used it
  assumes the executable is in the $PATH

  *port:* port you would like the service to run, if left as 0, a free
  port will be found

  - save_screenshot(filename)

    Gets the screenshot of the current window. Returns False if there
    is any IOError, else returns True. Use full paths in your
    filename.


Remote WebDriver
~~~~~~~~~~~~~~~~

**module:** selenium.webdriver.remote.webdriver

Controls a browser by sending commands to a remote server.  This
server is expected to be running the WebDriver wire protocol as
defined here: http://code.google.com/p/selenium/wiki/JsonWireProtocol

- class WebDriver(command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=None, browser_profile=None)



  Create a new driver that will issue commands using the wire protocol.


  *command_executor:* Either a command.CommandExecutor object or a
  string that specifies the URL of a remote server to send commands
  to.

  *desired_capabilities:* Dictionary holding predefined values for
  starting a browser

  *browser_profile:* A
  selenium.webdriver.firefox.firefox_profile.FirefoxProfile object.
  Only used if Firefox is requested.

  Other Attributes:

  *error_handler:* errorhandler.ErrorHandler object used to verify
  that the server did not return an error.

  *session_id:* The session ID to send with every command.

  *capabilities:* A dictionary of capabilities of the underlying
  browser for this instance's session (This is set by passing
  `desired_capabilities` argument)


  - name

    Returns the name of the underlying browser for this instance.


  - start_client():

    Called before starting a new session. This method may be
    overridden to define custom startup behavior.


  - stop_client()

    Called after executing a quit command. This method may be
    overridden to define custom shutdown behavior.


  - start_session(desired_capabilities, browser_profile=None)

    Creates a new session with the desired capabilities.

    *desired_capabilities:* A dictionry with following keys:

      - *browser_name:* The name of the browser to request.

      - *version:* Which browser version to request.

      - *platform:* Which platform to request the browser on.

      - *javascript_enabled:* Whether the new session should support JavaScript.

      - *browser_profile:* A
        selenium.webdriver.firefox.firefox_profile.FirefoxProfile
        object.  Only used if Firefox is requested.


  - create_web_element(element_id)

    Creates a web element with the specified element_id.

  - execute(driver_command, params=None)

    Sends a command to be executed by a command.CommandExecutor.

    *driver_command:* The name of the command to execute as a string.

    *params:* A dictionary of named parameters to send with the command.

    **Returns:** The command's JSON response loaded into a dictionary
    object.

  - get(url)

    Loads a web page in the current browser session.

  - title

    Returns the title of the current page.

  - find_element_by_id(`id_`)

    Finds an element by id.

    *id\_:* The id of the element to be found.

    Usage::

      driver.find_element_by_id('foo')


  - find_elements_by_id(`id_`)

    Finds multiple elements by id.

    *id\_:* The id of the elements to be found.

    Usage::

      driver.find_element_by_id('foo')


  - find_element_by_xpath(xpath)

    Finds an element by xpath.

    *xpath:* The xpath locator of the element to find.

    Usage::

      driver.find_element_by_xpath('//div/td[1]')


  - find_elements_by_xpath(xpath)

    Finds multiple elements by xpath.

    *xpath:* The xpath locator of the elements to be found.

    Usage::

      driver.find_elements_by_xpath("//div[contains(@class, 'foo')]")


  - find_element_by_link_text(link_text)

    Finds an element by link text.

    *link_text:* The text of the element to be found.

    Usage::

      driver.find_element_by_link_text('Sign In')


  - find_elements_by_link_text(text)

    Finds elements by link text.

    *link_text:* The text of the elements to be found.

    Usage::

      driver.find_elements_by_link_text('Sign In')


  - find_element_by_partial_link_text(link_text)

    Finds an element by a partial match of its link text.

    *link_text:* The text of the element to partially match on.

    Usage::

      driver.find_element_by_partial_link_text('Sign')


  - find_elements_by_partial_link_text(link_text)

    Finds elements by a partial match of their link text.

    *link_text:* The text of the element to partial match on.

    Usage::

      driver.find_element_by_partial_link_text('Sign')


  - find_element_by_name(name)

    Finds an element by name.

    *name:* The name of the element to find.

    Usage::

      driver.find_element_by_name('foo')


  - find_elements_by_name(name)

    Finds elements by name.

    *name:* The name of the elements to find.

    Usage::

      driver.find_elements_by_name('foo')


  - find_element_by_tag_name(name)

    Finds an element by tag name.

    *name:* The tag name of the element to find.

    Usage::

      driver.find_element_by_tag_name('foo')


  - find_elements_by_tag_name(name)

    Finds elements by tag name.

    *name:* The tag name the use when finding elements.

    Usage::

      driver.find_elements_by_tag_name('foo')


  - find_element_by_class_name(name)

    Finds an element by class name.

    *name:* The class name of the element to find.

    Usage::

      driver.find_element_by_class_name('foo')


  - find_elements_by_class_name(name)

    Finds elements by class name.

    *name:* The class name of the elements to find.

    Usage::

      driver.find_elements_by_class_name('foo')


  - find_element_by_css_selector(css_selector)

    Finds an element by css selector.

    *css_selector:* The css selector to use when finding elements.

    Usage::

      driver.find_element_by_css_selector('#foo')


  - find_elements_by_css_selector(css_selector)

    Finds elements by css selector.

    *css_selector:* The css selector to use when finding elements.

    Usage::

      driver.find_element_by_css_selector('#foo')

  - execute_script(script, \*args)

    Synchronously Executes JavaScript in the current window/frame.

    *script:* The JavaScript to execute.

    *\*args:* Any applicable arguments for your JavaScript.

    Usage::

      driver.execute_script('document.title')

  - execute_async_script(script, \*args)

    Asynchronously Executes JavaScript in the current window/frame.

    *script:* The JavaScript to execute.

    *\*args:* Any applicable arguments for your JavaScript.

    Usage::

      driver.execute_async_script('document.title')

  - current_url

    URL of the current loaded page.

    Usage::

      driver.current_url

  - page_source

    Source code (HTML,CSS,JS etc.) of the current loaded page.

    Usage::

      driver.page_source

  - close()

    Closes the current window.

    Usage::

      driver.close()

  - quit()

    Quits the driver and closes every associated window.

    Usage::

      driver.quit()

  - current_window_handle

    Usage::

      driver.current_window_handle

  - window_handles

    Returns the handles of all windows within the current session.

    Usage::

      driver.window_handles

  - switch_to_active_element()

    Returns the element with focus, or BODY if nothing has focus.

    Usage::

      driver.switch_to_active_element()

  - switch_to_window(window_name)

    Switches focus to the specified window.

    *window_name:* The name of the window to switch to.

    Usage::

      driver.switch_to_window('main')

  - switch_to_frame(index_or_name)

    Switches focus to the specified frame, by index or name.

    *index_or_name:* The name of the window to switch to, or an
    integer representing the index to switch to.

    Usage::

      driver.switch_to_frame('frame_name')
      driver.switch_to_frame(1)

  - switch_to_default_content()

    Switch focus to the default frame.

    Usage::

      driver.switch_to_default_content()

  - switch_to_alert()

    Switches focus to an alert on the page.

    Usage::

      driver.switch_to_alert()


  - back()

    Goes one step backward in the browser history.

    Usage::

      driver.back()


  - forward()

    Goes one step forward in the browser history.

    Usage::

      driver.forward()


  - refresh()

    Refreshes the current page.

    Usage::

      driver.refresh()


  - get_cookies()

    Returns a set of dictionaries, corresponding to cookies visible in
    the current session.

    Usage::

      driver.get_cookies()

  - get_cookie(name)

    Get a single cookie by name. Returns the cookie if found, None if not.

    *name:* namd of the cookie

    Usage::

      driver.get_cookie('my_cookie')

  - delete_cookie(name)

    Delete a particular cookie.

    *name:* namd of the cookie

    Usage::

      driver.delete_cookie('my_cookie')

  - delete_all_cookies()

    Delete all cookies in the scope of the session.

    Usage::

      driver.delete_all_cookies()

  - add_cookie(cookie_dict)

    Adds a cookie to your current session.

    *cookie_dict:* A dictionary object, with the desired cookie name
    as the key, and the value being the desired contents.

    Usage::

      driver.add_cookie({'foo': 'bar',})

  - implicitly_wait(time_to_wait)

    Sets a sticky timeout to implicitly wait for an element to be
    found, or a command to complete. This method only needs to be
    called one time per session.

    *time_to_wait:* Amount of time to wait

    Usage::

      driver.implicitly_wait(30)


  - set_script_timeout(time_to_wait)

    Set the amount of time that the script should wait before throwing
    an error.

    *time_to_wait:* The amount of time to wait

    Usage::

      driver.set_script_timeout(30)

  - desired_capabilities

    returns the drivers current desired capabilities being used

  - get_screenshot_as_file(filename)

    Gets the screenshot of the current window. Returns False if there
    is any IOError, else returns True. Use full paths in your
    filename.

    *filename:* The full path you wish to save your screenshot to.

    Usage::

      driver.get_screenshot_as_file('/Screenshots/foo.png')

  - get_screenshot_as_base64()

    Gets the screenshot of the current window as a base64 encoded
    string which is useful in embedded images in HTML.

    Usage::

      driver.get_screenshot_as_base64()

WebElement
~~~~~~~~~~

**module:** webdriver.remote.webelement

Represents an HTML element.

Generally, all interesting operations to do with interacting with a page
will be performed through this interface.

- class WebElement(parent, id_)

  This class represents a web element.

  *parent:* The parent element of the current element

  *id_:* The Id of the current element

  - tag_name

    Gets this element's tagName property.

  - text

    Gets the text of the element.

  - click()

    Clicks the element.

  - submit()
    
    Submits a form.

  - clear()

    Clears the text if it's a text entry element.

  - get_attribute(name)

    Gets the attribute value.

  - s_selected(self)
    
    Whether the element is selected.

  - is_enabled()
    
    Whether the element is enabled.

  - find_element_by_id(id_)

    Finds element by id.

  - find_elements_by_id(id_)

  - find_element_by_name(name)

    Find element by name.

  - find_elements_by_name(name)

  - find_element_by_link_text(link_text)

    Finds element by link text.

  - find_elements_by_link_text(link_text)

  - find_element_by_partial_link_text(link_text)

  - find_elements_by_partial_link_text(link_text):

  - find_element_by_tag_name(name)

  - find_elements_by_tag_name(name)

  - find_element_by_xpath(xpath)
    
    Finds element by xpath.

  - find_elements_by_xpath(xpath)

    Finds elements within the elements by xpath.

  - find_element_by_class_name(name)
    
    Finds an element by their class name.

  - find_elements_by_class_name(name)
    
    Finds elements by their class name.

  - find_element_by_css_selector(css_selector)

    Find and return an element by CSS selector.

  - find_elements_by_css_selector(css_selector)
    
    Find and return list of multiple elements by CSS selector.

  - send_keys(*value)
    
    Simulates typing into the element.

**RenderedWebElement Items**

  - is_displayed()

    Whether the element would be visible to a user

  - size

    Returns the size of the element

  - value_of_css_property(property_name)

    Returns the value of a CSS property

  - location
    
    Returns the location of the element in the renderable canvas

  - parent

  - id

  - find_element(by=By.ID, value=None)

    It is reccommened to use ``find_element_by_*`` methods instead of this.

  - find_elements(By.ID, value=None)

    It is reccommened to use ``find_elements_by_*`` methods instead of this.
