Scraping web sites
==================

Screen-scraping web sites is the process of extracting structured information
from ordinary web sites or on-line databases using custom scripts or scripted 
procedures. Scraping can be used to extract large archives of online content 
into a form more suitable for further processing. This is particularly 
fruitful when the web site you are scraping is based on a structured database
and all you have to do is to reverse the rendering of content.

In general, the following problems are common when scraping data:

 * Badly formatted HTML code with little or no structural information.
 * Authentication systems that are supposed to prevent automatic access.
 * Session-based systems that use browser cookies to maintain state.
 * Lack of complete listings and possibilities for wildcard search.
 * Blocking of bulk access.
 * Use of outdated server technologies and inappropriate data formats.

##: Parse HTML
--------------



##: Index and Item
------------------

A very common pattern in scraping is to make a distinction between an index of
items and the items detail page. For example, lets have a look at the `CORDIS`_ 
database, a listing of research projects funded by the European Commission. 
When you run an empty search on the database, you will recieve a list of 
projects with very few details on each item. Clicking on a project name will
give you a details page with a description, contact details etc.

.. _`CORDIS`: http://cordis.europa.eu/fp7/projects_en.html

This split between index and item pages is useful in many ways: it allows you
to modularize your scraper, introduce a task queue and possibly multiple 
threads. Imagine the following program::

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

The benefit of using a generator here is that it can later be replaced with a 
more advanced call, such as a thread manager picking items from a queue.




