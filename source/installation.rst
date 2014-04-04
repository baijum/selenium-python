.. _installation:

Installation
------------

Introduction
~~~~~~~~~~~~

Selenium Python bindings provides a simple API to write
functional/acceptance tests using Selenium WebDriver.  Through
Selenium Python API you can access all functionalities of Selenium
WebDriver in an intuitive way.

Selenium Python bindings provide a convenient API to access Selenium
WebDrivers like Firefox, Ie, Chrome, Remote etc...  The current supported
Python versions are 2.7, 3.2, 3.3 and 3.4.

This documentation explains Selenium 2 WebDriver API.  Selenium
1 / Selenium RC API is not covered here.


Downloading Python bindings for Selenium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can download Python bindings for Selenium from the `PyPI page for
selenium package <http://pypi.python.org/pypi/selenium>`_.  However,
a better approach would be to use
`pip <http://www.pip-installer.org/en/latest/installing.html>`_ to
install the selenium package.  Python 3.4 has pip available in the
`standard library <http://docs.python.org/3.4/installing/index.html>`_.
Using `pip`, you can install selenium like this::

  pip install selenium

You may consider using `virtualenv <http://www.virtualenv.org>`_
to create isolated Python environments.  Python 3.4 has `pyvenv
<http://docs.python.org/3.4/using/scripts.html#scripts-pyvenv>`_
which is almost same as virtualenv.


Detailed instructions for Windows users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Note::

  You should have internet connection to perform this installation.

1. Install Python 3.4 using the `MSI available in python.org download
   page <http://www.python.org/download>`_.

2. Start a command prompt using the ``cmd.exe`` program and run the
   ``pip`` command as given below to install `selenium`.

   ::
   
     C:\Python34\Scripts\pip.exe install selenium

Now you can run your test scripts using Python.  For example,
if you have created a Selenium based script and saved it inside
``C:\my_selenium_script.py``, you can run it like this::

  C:\Python34\python.exe C:\my_selenium_script.py


Downloading Selenium server
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

  The Selenium server is only required, if you want to use the remote
  WebDriver.  See the :ref:`selenium-remote-webdriver` section for
  more details.  If you are a beginner learning Selenium, you can
  skip this section and proceed with next chapter.

Selenium server is a Java program.  Java Runtime Environment (JRE) 1.6
or newer version is recommended to run Selenium server.

You can download Selenium server 2.x from the `download page of
selenium website <http://seleniumhq.org/download/>`_.  The file name
should be something like this:
``selenium-server-standalone-2.x.x.jar``.  You can always download the
latest 2.x version of Selenium server.

If Java Runtime Environment (JRE) is not installed in your system, you
can download the `JRE from the Oracle website
<http://www.oracle.com/technetwork/java/javase/downloads/index.html>`_.
If you are using a GNU/Linux system and have root access in your system,
you can also use your operating system instructions to install JRE.

If `java` command is available in the PATH (environment variable),
you can start the Selenium server using this command::

  java -jar selenium-server-standalone-2.x.x.jar

Replace `2.x.x` with actual version of Selenium server you downloaded
from the site.

If JRE is installed as a non-root user and/or if it is
not available in the PATH (environment variable), you can type the
relative or absolute path to the `java` command.  Similarly, you can
provide relative or absolute path to Selenium server jar file.
Then, the command will look something like this::

  /path/to/java -jar /path/to/selenium-server-standalone-2.x.x.jar
