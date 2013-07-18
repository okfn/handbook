Making data on the web useful: scraping
=======================================

Introduction
------------
Many times data is not easily accessible - although it does exist. As much as we wish everything was available in CSV or the format of our choice - most data is published in different forms on the web. What if you want to use the data to combine it with other datasets and explore it independently? 

Scraping to the rescue!

Scraping describes the method to extract data hidden in documents - such as Web Pages and PDFs and make it useable for further processing. It is among the most useful skills if you set out to investigate data - and most of the time it’s not especially challenging. For the most simple ways of scraping you don’t even need to know how to write code.

This example relies heavily on Google Chrome for the first part. Some things work well with other browsers, however we will be using one specific browser extension only available on Chrome. If you can’t install Chrome, don’t worry the principles remain similar.

Code-free Scraping in 5 minutes using Google Spreadsheets & Google Chrome
-------------------------------------------------------------------------

Knowing the structure of a website is the first step towards extracting and using the data. Let’s get our data into a spreadsheet - so we can use it further. An easy way to do this is provided by a special formula in Google Spreadsheets.

Save yourselves hours of time in copy-paste agony with the ImportHTML command in Google Spreadsheets. It really is magic! 

Recipes
^^^^^^^

In order to complete the next challenge, take a look in the Handbook at one of the following recipes:  

#. `Extracting data from HTML tables`_.
#. Scraping using the `Scraper Extension for Chrome`_

.. _Extracting data from HTML tables: http://schoolofdata.org/handbook/recipes/liberating-html-tables/
.. _Scraper Extension for Chrome: http://schoolofdata.org/handbook/recipes/scraper-extension-for-chrome

.. image:: http://farm9.staticflickr.com/8303/7850933084_b188c02992_o_d.jpg

Both methods are useful for: 

* Extracting individual lists or tables from single webpages

The latter can do slightly more complex tasks, such as extracting nested information. Take a look at the recipe for more details. 

Neither will work for: 

* Extracting data spread across multiple webpages

Challenge
^^^^^^^^^

.. raw:: html
  
  <div class="well">

**Task:** Find a website with a table and scrape the information from it. Share your result on `datahub.io`_ (make sure to tag your dataset with schoolofdata.org)

.. _datahub.io: http://datahub.io/

.. raw:: html
  
  </div>

Tip
^^^^

Once you've got your table into the spreadsheet, you may want to move it around, or put it in another sheet. Right click the top left cell and select “paste special” - “paste values only”.

Scraping more than one webpage: Scraperwiki
-------------------------------------------

Note: Before proceeding into full scraping mode, it's helpful to understand the flesh and bones of what makes up a webpage. Read the `Introduction to HTML recipe`_ in the handbook. 

.. _Introduction to HTML recipe: http://schoolofdata.org/handbook/recipes/introduction-to-html/

Until now we’ve only scraped data from a single webpage. What if there are
more? Or you want to scrape complex databases? You’ll need to learn how to
program - at least a bit. 

It's beyond the scope of this course to teach how to scrape, our aim here is to help you understand whether it is worth investing your time to learn, and to point you at some useful resources to help you on your way!

Structure of a scraper
^^^^^^^^^^^^^^^^^^^^^^

Scrapers are comprised of three core parts:

#. A queue of pages to scrape
#. An area for structured data to be stored, such as a database
#. A downloader and parser that adds URLs to the queue and/or
   structured information to the database.

Fortunately for you there is a good website for
programming scrapers: `ScraperWiki.com`_

.. _ScraperWiki.com: http://scraperwiki.com

.. image:: http://farm9.staticflickr.com/8112/8660176200_2dd5aa8d0b_z.jpg

ScraperWiki has two main functions: You can write scrapers - which are
optionally run regularly and the data is available to everyone visiting -
or you can request them to write scrapers for you. The latter costs some
money - however it helps to contact the Scraperwiki community (`Google
Group`_) someone might get excited about your project and help you!.

.. _Google Group: https://groups.google.com/forum/?fromgroups=#!forum/scraperwiki

If you are interested in writing scrapers with Scraperwiki, check out this `sample scraper`_ - scraping some data about `Parliament`_.
Click View source to see the details. Also check out the Scraperwiki documentation: https://scraperwiki.com/docs/python/

.. _sample scraper: https://scraperwiki.com/scrapers/members_of_the_uk_parliament/
.. _Parliament: http://www.parliament.uk/mps-lords-and-offices/mps/

When should I make the investment to learn how to scrape? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A few reasons (non-exhaustive list!): 

#. If you regularly have to extract data where there are numerous tables in one page. 
#. If your information is spread across numerous pages. 
#. If you want to run the scraper regularly (e.g. if information is released every week or month).
#. If you want things like email alerts if information on a particular webpage changes. 

...And you don't want to pay someone else to do it for you!

Summary:
--------
In this course we’ve covered Web scraping and how to extract data from websites. The main function of scraping is to convert data that is semi-structured into structured data and make it easily useable for further processing. While this is a relatively simple task with a bit of programming - for single webpages it is also feasible without any programming at all. We’ve introduced =importHTML and the Scraper extension for your scraping needs.

Further Reading
---------------

* `Scraping for Journalism`_: A Guide for Collecting Data: ProPublica Guides
* `Scraping for Journalists`_ (ebook): Paul Bradshaw
* `Scrape the Web`_: Strategies for programming websites that don't expect it : Talk from PyCon
* `An Introduction to Compassionate Screen Scraping`_: Will Larson 

.. _Scraping for Journalism: http://www.propublica.org/nerds/item/doc-dollars-guides-collecting-the-data
.. _Scraping for Journalists: https://leanpub.com/scrapingforjournalists
.. _Scrape the Web: http://pyvideo.org/video/256/pycon-2010--scrape-the-web--strategies-for-progra
.. _An Introduction to Compassionate Screen Scraping: http://lethain.com/an-introduction-to-compassionate-screenscraping/
.. raw:: html

  <div class="alert alert-info">Any questions? Got stuck? <a class="btn
  btn-large btn-info" href="http://ask.schoolofdata.org">Ask School of Data!
  </a></div>
