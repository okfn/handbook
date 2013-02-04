Introduction
------------

Welcome to the source text of the `School of Data Handbook`_. The handbook is 
a project of the `Open Knowledge Foundation`_.  If you are reading this 
it is likely you are looking to contribute in some way, whether that's 
feedback, editing or adding more content. If you just want 
to read the handbook, then please head over to
http://schoolofdata.org/handbook.

.. _School of Data Handbook: http://schoolofdata.org/handbook
.. _Open Knowledge Foundation: http://okfn.org/
.. _Sphinx: http://sphinx.pocoo.org/

Contributing
------------

We have several ways you can help. 

* The simplest way is to `open an issue`_ and point us to outdated content
  or parts that need more editing
* Feel free to fork the repository and work on adding or editing content -
  once you're done: Send us a pull-request so we can add your chagnes.
* If you want to get involved further join our `mailing list`_ and contact
  us there

.. _open an issue: https://github.com/okfn/datawrangling/issues/new
.. _mailing list: http://lists.okfn.org/mailman/listinfo/school-of-data


Resources
---------

:Home Page:     http://schoolofdata.org/handbook
:Mailing List:  http://lists.okfn.org/mailman/listinfo/school-of-data
:Source:        https://github.org/okfn/datawrangling
:Translations:  coming soon
:Sphinx Introduction: http://sphinx-doc.org/rest.html


About our tools
---------------

The handbook is written the `ReStructured Text`_ format. `ReStructured Text`_
allows us to write files in plain text files, which can be nicely rendered 
as a website or a PDF using `Sphinx`_.

.. _ReStructured Text: http://sphinx.pocoo.org/rest.html


Project Layout
--------------

Outline::

  datawrangling/
    text/
    build/

Details:

| ``datawrangling`` is the base directory.
|
|    ``text`` is where we keep the plain text source files.
|
|    ``build`` is where rendered, or "built", HTML files live.  


Rendering the handbook
--------------------

1. Move into the base directory of the project::

    cd datawrangling

2. Install `Sphinx`_, with a minimum version of 1.0. Instructions for 
   Debian and Ubuntu::

    apt-get install python-sphinx

3. Make sure you have installed the theme by initializing the git submodules
   for this repo::

    git submodule init
    git submodule update

4. Render the HTML, using ``make``::

    make html


