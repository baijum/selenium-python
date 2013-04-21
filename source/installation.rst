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
WebDrivers like Firefox, Ie and Chrome.  The current supported Python
versions are 2.6, 2.7, 3.2 and 3.3.

This documentation explains using Selenium 2 WebDriver API.
Selenium 1 / Selenium RC API is not covered here.


Downloading Python bindings for Selenium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can download Python bindings for Selenium from the `PyPI page for
selenium package <http://pypi.python.org/pypi/selenium>`_.  You can
also use `easy_install <http://python-distribute.org/distribute_setup.py>`_
or `pip <http://pypi.python.org/pypi/pip>`_ to install the bindings::

  easy_install selenium

or::

  pip install selenium

You may consider using `virtualenv <http://www.virtualenv.org>`_
to create isolated Python environments.


Detailed instructions for Windows users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Note::

  You should have internet connection to perform this installation.

1. Install Python 2.7 using the `MSI available in python.org download page <http://www.python.org/download>`_.

2. Create a folder named ``C:\seltests`` and download `virtualenv.py <https://raw.github.com/pypa/virtualenv/master/virtualenv.py>`_ script into that folder.

   If you have downloaded and saved the program properly, please make sure ``virtualenv.py`` file exists at this location in your system:  ``C:\seltests\virtualenv.py``

3. Start a command prompt (using the ``cmd.exe`` program), then change to the ``C:\seltests`` folder and run the ``virtualenv.py`` script as given below.

   ::

     C:
     cd C:\seltests
     C:\Python27\python.exe virtualenv.py selenv


   This step will create a folder named ``C:\seltests\selenv`` which contains a virtual Python.

4. Use the ``pip`` command as given below to install `selenium`

   ::

     C:\seltests\selenv\Scripts\pip.exe install selenium

   Now installation has been completed!  You can proceed to test your Selenium scripts.

Now you can run your test scripts using the virtual Python.  For example, if you have a created
script and saved it inside ``C:\seltests\my_selenium_script.py``, you can run it like this.

::

  C:\seltests\selenv\Scripts\python.exe C:\seltests\my_selenium_script.py


Downloading Selenium server
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

  The Selenium server is only required, if you want to use the remote
  WebDriver.  See the :ref:`selenium-remote-webdriver` section
  for more details.

Selenium server is a Java program.  Java Runtime Environment (JRE)
1.6 or newer version is recommended to run Selenium server.

You can download Selenium server 2.x from the `download page of
selenium website <http://seleniumhq.org/download/>`_.  The file name
should be something like this:
``selenium-server-standalone-2.x.x.jar``.  You can always download the
latest 2.x version of Selenium server.

If Java Runtime Environment (JRE) is not installed in your system, you
can download the `JRE from the Oracle website
<http://www.oracle.com/technetwork/java/javase/downloads/index.html>`_.
If you have root access in your system, you can also use your
operating system instructions to install JRE.


Running Selenium server
~~~~~~~~~~~~~~~~~~~~~~~

You should have Java Runtime Environment (JRE) in the system.  If
`java` command is available in the PATH (environment variable), you
can start the Selenium server using the command command given below.
Replace `2.x.x` with actual version of Selenium server you downloaded
from the site.  If JRE is installed as a non-root user and/or if it is
not available in the PATH (environment variable), you can type the
relative/absolute path to the `java` command, for eg:-
``./jre1.6.0_26/bin/java``::

  java -jar selenium-server-standalone-2.x.x.jar

