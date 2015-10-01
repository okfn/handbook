---
title: Scraping web sites
---

Screen-scraping web sites is the process of extracting structured information from ordinary web sites or on-line databases using custom scripts or scripted procedures. Scraping can be used to extract large archives of online content into a form more suitable for further processing. This is particularly fruitful when the web site you are scraping is based on a structured database and all you have to do is to reverse the rendering of content.

In general, the following problems are common when scraping data:

 * Badly formatted HTML code with little or no structural information.
 * Authentication systems that are supposed to prevent automatic access.
 * Session-based systems that use browser cookies to maintain state.
 * Lack of complete listings and possibilities for wildcard search.
 * Blocking of bulk access.
 * Use of outdated server technologies and inappropriate data formats.

Parse HTML
----------

One of the fantastic aspects of the web is that most web pages are little trees of data that wait to be harvested. If you are not familiar with the basics of [`HTML`](http://en.selfhtml.org/), [`XML`](http://www.xml.com/pub/a/98/10/guide0.html) and the [`XPath`](http://lxml.de/xpathxslt.html#xpath) query language, invest a few moments to learn about each.

To learn about HTML in practice, use the [`debugging toolbar`](http://getfirebug.com/) in your browser. With the increasing use of dynamic page content (Ajax and JavaScript frameworks), looking at a web page's HTML source is becoming less helpful: you need to be able to inspect the rendered document object. Firefox's Firebug used to be the tool of choice for this, but nowadays the toolbars in Safari and Chrome are equally useful. Make a habit of peeking under the hood whenever you discover something technically weird or interesting on the web.

To parse HTML or XML in Python, use [`lxml`](http://lxml.de). The libary offers simple ways to parse and traverse documents, both via generic XPath queries and through a custom interface. Extended HTML5 support is available via [`html5lib`](http://code.google.com/p/html5lib/) which can be used as a plugin to lxml. In the past, [`BeautifulSoup`](http://www.crummy.com/software/BeautifulSoup/) was very popular amongst scrapers for HTML handling, but lxml has since caught up regarding support for broken markup and is an order of magnitude faster, so BeautifulSoup has been discontinued as a project.

The basic steps for reading an HTML page are trivial::

```bash
>>> from lxml import html
>>> doc = html.parse('http://www.google.com/')
>>> elem = doc.find('//div[@id="searchform"]//center/input[1]')
>>> print elem.get('value')
I'm Feeling Lucky
```

Note that we import the html parser rather than the XML one (lxml.etree). Both offer the ``parse()`` convenience function that accepts either a file object or an URL. The ``find()`` method uses lxml-style XPath and has two siblings, ``findall()`` and ``findtext()`` which together are the main tools of lxml tree
traversal.

=={.note}
**Note**: While some people [`prefer to use regular expressions`](http://stackoverflow.com/questions/4231382/regular-expression-pattern-not-matching-anywhere-in-string/4234491#4234491) to parse HTML, this is generally a bad idea unless you know exactly what you are doing. Most of the time using a proper HTML parser will result in much more readable and 
stable code.
==

Index and Item
--------------

A very common pattern in scraping is to make a distinction between an index of items and the items detail page. For example, lets have a look at the [`CORDIS`](http://cordis.europa.eu/fp7/projects_en.html) database, a listing of research projects funded by the European Commission. When you run an empty search on the database, you will recieve a list of projects with very few details on each item. Clicking on a project name will give you a details page with a description, contact details etc.

This split between index and item pages is useful in many ways: it allows you to modularize your scraper, introduce a task queue and possibly multiple threads. Imagine the following program::

```python
def get_index():
	...
	for page in count():
	  items = ...
	  for item in items:
		yield item

def get_items(items):
	for item in items:
	  ...

get_items(get_index())
```

The benefit of using a generator here is that it can later be replaced with a more advanced call, such as a thread manager picking items from a queue.

As a more comprehensive example, here is an index collecting function for the CORDIS database mentioned above:

```
../examples/cordis.py
```

Note that this is not beautiful code by any means, but it is sufficiently functional and solves the problem.


Choosing your elements
----------------------

**TODO**: add this section

Caching HTTP requests
---------------------

**TODO**: link to httplib2

Threading your scraper
----------------------

One particularly useful tool for speeding up your scraper is spreading the retrieval over various threads that operate in parallel. While this is useful, it also means you must take care not to overload the server and to cause a denial-of-service attack. Running a scraper with more than 15-20 threads should only be tried against large, well-cached systems.

The easiest way to thread your scraper is using the index and item pattern described above: your index scraper function will generate a task queue and a set of worker threads will handle each item on that queue.

```
../examples/threads.py
```

