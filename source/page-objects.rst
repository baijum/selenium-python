.. _page-objects:

Page Objects
------------

.. note::

   Code in this chapter works and is quite self-descriptive, but a
   little description wouldn't hurt.  If anyone interested, please
   send pull request in `Github
   <https://github.com/baijum/selenium-python>`_.  Here is an example
   implementation of the page objects pattern:
   https://github.com/baijum/pitracker/tree/master/test/acceptance

This chapter is a tutorial introduction to page objects design
pattern.  A page object represents an area in the web application user
interface that your test is interating.  Page objects reduces the
amount of duplicated code and if the user interface changes, the fix
need only changes in one place.

Test case
~~~~~~~~~

Here is a test case which searches for a word in python.org website
and ensure some results are found.

::

  import unittest
  from selenium import webdriver
  import page

  class PythonOrgSearch(unittest.TestCase):

      def setUp(self):
          self.driver = webdriver.Firefox()
          driver.get("http://www.python.org")

      def test_search_in_python_org(self):
          main_page = page.MainPage(self.driver)
          assert main_page.is_title_matches(), "python.org title doesn't match."
	  main_page.search_text_element = "pycon"
	  main_page.click_go_button()
          search_results_page = page.SearchResultsPage(self.driver)
	  assert search_results_page.is_results_found(), "No results found."

      def tearDown(self):
          self.driver.close()

  if __name__ == "__main__":
      unittest.main()

Page object classes
~~~~~~~~~~~~~~~~~~~

The ``page.py`` will look like this::

  from element import BasePageElement
  from locators import MainPageLocators

  class SearchTextElement(BasePageElement):

      locator = 'q'


  class BasePage(object):

      def __init__(self, driver):
          self.driver = driver


  class MainPage(BasePage):

      search_text_element = SearchTextElement()

      def is_title_matches(self):
          return "Python" in self.driver.title

      def click_go_button(self):
          element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
          element.click()


  class SearchResultsPage(BasePage):

      def is_results_found(self):
          #Probably should search for this text in the specific page element, but as for now it works fine
          return "No results found." not in self.driver.page_source

Page elements
~~~~~~~~~~~~~

The ``element.py`` will look like this::

  from selenium.webdriver.support.ui import WebDriverWait


  class BasePageElement(object):

      def __set__(self, obj, value):
          driver = obj.driver
          WebDriverWait(driver, 100).until(
              lambda driver: driver.find_element_by_name(self.locator))
          driver.find_element_by_name(self.locator).send_keys(value)

      def __get__(self, obj, owner):
          driver = obj.driver
          WebDriverWait(driver, 100).until(
              lambda driver: driver.find_element_by_name(self.locator))
          element = driver.find_element_by_name(self.locator)
          return element.get_attribute("value")

Locators
~~~~~~~~

The ``locators.py`` will look like this::

  from selenium.webdriver.common.by import By

  class MainPageLocators(object):
      GO_BUTTON = (By.ID, 'submit')

  class SearchResultsPageLocators(object):
      pass
