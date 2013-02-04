Introduction
------------

Welcome to the source text of the `Data Wrangling Handbook`_. The handbook is 
a project of the `Open Knowledge Foundation`_.  If you are reading this 
it is likely you are looking to contribute in some way, whether that's 
translation, feedback, editing or adding more content. If you just want 
to read the handbook, then please head over to the 
http://handbook.schoolofdata.org/.

.. _Data Wrangling Handbook: http://handbook.schoolofdata.org/
.. _Open Knowledge Foundation: http://okfn.org/
.. _Sphinx: http://sphinx.pocoo.org/

Contributing
------------

We have several ways you can help. The project is split into a few 
roles. Our **authors** write content, **editors** merge those 
submissions into the handbook, **designers** help beautify it and 
**translators** bring the handbook to all countries of the world.

If you are interested in contributing please either `open an issue`_ or get in
contact on the `mailing list`_.

.. _open an issue: https://github.com/okfn/datawrangling/issues/new
.. _mailing list: http://lists.okfn.org/mailman/listinfo/school-of-data


Resources
---------

:Home Page:     http://handbook.schoolofdata.org/
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
    examples
    bin/
    build/

Details:

| ``datawrangling`` is the base directory.
|
|    ``text`` is where we keep the plain text source files.
|
|    ``examples`` is where we put example code and utilities
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


Deploying the Handbook
----------------------

We use ReadTheDocs to host the handbook. ReadTheDocs will automatically rebuild
the site each time you push a change to the master branch.

