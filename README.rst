.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/ad_m/ckanext-example_theme.svg?branch=master
    :target: https://travis-ci.org/ad_m/ckanext-example_theme

.. image:: https://coveralls.io/repos/ad_m/ckanext-example_theme/badge.svg
  :target: https://coveralls.io/r/ad_m/ckanext-example_theme

.. image:: https://pypip.in/download/ckanext-example_theme/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-example_theme/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-example_theme/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-example_theme/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-example_theme/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-example_theme/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-example_theme/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-example_theme/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-example_theme/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-example_theme/
    :alt: License

=============
ckanext-example_theme
=============

An exemplary plugin, the purpose of which is to demonstrate the overwriting of selected JS files of the embedded CKAN
module without copying / forcing it entirely.

------------
Requirements
------------

The plugin requires following plugins:

* recline_view (CKAN core plugin)

------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-example_theme:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-example_theme Python package into your virtual environment::

     pip install ckanext-example_theme

3. Add ``example_theme`` to the ``ckan.plugins`` setting in your CKAN
   config file before ``recline_view`` (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


------------------------
Development Installation
------------------------

To install ckanext-example_theme for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/ad_m/ckanext-example_theme.git
    cd ckanext-example_theme
    python setup.py develop
    pip install -r dev-requirements.txt
