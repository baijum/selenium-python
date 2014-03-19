from setuptools import setup, find_packages

setup(name="selenium-python-docs",
      version="0.0.0",
      description="",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      author='Baiju Muthukadan',
      install_requires=['setuptools',
                        'selenium',
                        'Sphinx',
                        ],
      )
