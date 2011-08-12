###############
How to get data
###############

.. sectionauthor:: Tim McNamara <tim.mcnamara@okfn.org>

This guide focuses on how you can extract data from web sites and 
web services. We will go over the various resources at your disposal
to find sources which are useful to you.

************
Finding data
************

Directories
===========

Search Engines
--------------

There are a small number of emerging search engines for raw data:

 * `opendatasearch.org`_ is a search engine which collects linked data from
   various directories.
 * The `Open Data Directory` provides wide coverage of many catalogues.
   At this stage, the directory's metadata is released under a 
   non-commercial licence.
 
Edited directories
------------------

One of the `largest directories of open data repositories`_ is provided 
by the `Open Access Directory`_. Its collection is mostly focused on 
scientific or research data and is curated by topic area. Topics covered 
the directory include archaeology, astronomy, biology, chemistry, 
computer science, energy, environmental sciences, earth sciences,
linguistics, marine sciences, medicine, physics and social sciences.

`CKAN`_ is a directory that largely works through wiki-like edits. Some 
of the benefits of CKAN are that it has well developed client libraries 
that enable you to programmatically access information about each of the 
datasets within its directory. For example, it is easy to ask it to 
tell you which datasets have been released into the public domain.

`Quora`_ has actually become a great source of information about where 
to find data on specific topic areas. It has several questions related 
to this topic which are being continually updated. Some examples include:

* `What are some free, public data sets? <http://www.quora.com/Data/What-are-some-free-public-data-sets>`
*  `Where can I get large datasets open to the public <http://www.quora.com/Data/Where-can-I-get-large-datasets-open-to-the-public>`

.. _opendatasearch.org: http://www.opendatasearch.org/
.. _largest directories of open data repositories: http://oad.simmons.edu/oadwiki/Data_repositories
.. _Open Access Directory: http://oad.simmons.edu/oadwiki/About_OAD
.. _CKAN: http://ckan.net
.. _Quora: http://www.quora.com

***************
Extracting Data
***************

.. 
   TODO
     OData
     REST APIs
      - ideas to get all results when there is no list given
      - paginating through all results as iterators
     Feeds - RSS/Atom

Scraping
========

Remember, the website is the API. If a site provides information full
information on its pages, but only offers you a limited access via its
search page.

Structure of a scraper
----------------------

Scrapers are comprised of three core parts:

1) A queue of pages to scrape
2) An area for structured data to be stored, such as a database
3) A downloader and parser that adds URLs to the queue and/or
   structured information to the database.

Useful clean up steps
---------------------

One advantage of scraping data from the web is that you can actually 
have a better dataset than the original. Because you need to take steps
to understand the dataset's inconsistencies, you can eliminate or at least
minimise them. From another perspective, spending time cleaning up 
messy data can fill the large gaps that your processor will experience
when waiting for it to be downloaded from its host.

This section provides an example of several useful clean-up operations.

* Cleaning HTML
* Strip whitespace
* Converting numbers to number types: 
* Converting Boolean values: `'Yes' -> True`
* Converting dates to machine-readable formats: `"24 June 2004" -> "2004-06-24"`

Clean the HTML
^^^^^^^^^^^^^^

HTML you find on the web can be atrocious. Here's a quick function that 
can help. We make use of the `lxml`_ library. It'svery good at 
understanding broken HTML and will render a perfectly-formed page for 
your extractor functions to

You may be concerned that this is computationally wasteful. This is 
true, but it can reduce lots of the irritation of extracting specific
information from messy HTML::

    def clean_page(html, pretty_print=False):
        """
        >>> junk = "some random HTML<P> for you to try to parse</p>"
        >>> clean_page(junk)
        '<div><p>some random HTML</p><p> for you to try to parse</p></div>'
        >>> print clean_page(junk, pretty_print=True)
        <div>
        <p>some random HTML</p>
        <p> for you to try to parse</p>
        </div>
        """
        from lxml.html import fromstring
        from lxml.html import tostring
        return tostring(fromstring(html), pretty_print=pretty_print)

Converting yes/no to Boolean values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Computers are far better at interpreting Boolean values when they are 
consistently provided. Irrespective of the programming language, normalising
these values will make any automatic comparisions much richer::

    def to_bool(yes_no, none_to_false=True):
        """
        >>> to_bool('')
        False
        >>> to_bool(None):
        False
        >>> to_bool('y')
        True
        >>> to_bool('yip')
        True
        >>> to_bool('Yes')
        True
        >>> to_bool('nuh')
        False
        """
        yes_no = yes_no.strip().lower()
        if not yes_no.strip() and none_to_false:
            return False
        if yes_no.startswith('y'):
            return True
        elif yes_no.startswith('n'):
            return False

Converting numbers to the correct type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you're extracting number from HTML tables, they will each be 
represented as a `string` or Unicode, even though it would be 
more sensible to treat as integers or floating point numbers:: 

    def to_int(number, european=False):
        """ 
        >>> to_int('32')
        32
        >>> to_int('3,998')
        3998
        >>> to_int('3.998', european=True)
        3998
        """
        if european:
            number = number.replace('.', '')
        else:
            number = number.replace(',', '')
        return int(number)

    def to_float(number, european=False)
        """
        >>> to_float(u'42.1')
        42.1
        >>> to_float(u'32,1', european=True)
        32.1
        >>> to_float('3,132.87')
        3132.87
        >>> to_float('3.132,87')
        3132.87
        >>> to_float('(54.12)')
        -54.12

        Warning
        -------

        Incorrectly declaring `european` leads to troublesome results:

        >>> to_float('54.2', european=True)
        542
        """
        import string
        if european:
            table = string.maketrans(',.','.,')
            number = string.translate(number, table)
        number = number.replace(',', '')
        if number.startswith('(') and number.endswith(')'):
            number = '-' + number[1:-1] 
        return float(number)

If you are dealing with numbers from another region consistently, it may be
appropriate to call upon the `locale` module. You will then have the advantage
of code written in C, rather than Python::

    >>> import locale
    >>> locale.setlocale(locale.LC_ALL, '')
    >>> locale.atoi('1,000,000')
    1000000

Stripping whitespace
^^^^^^^^^^^^^^^^^^^^

Removing whitespace from a string is built into many languages
`string`. Removing left and right whitespace is highly 
recommended. Your database will be unable to sort data properly
which have inconsistent treatment of whitespace:: 

    >>> u'\n\tTitle'.strip()
    u'Title'

Converting dates to a machine-readable format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python is well blessed with a `mature date parser`_, `dateutil`. 
We can take advantage of this to make light work an otherwise
error-prone task.

`dateutil` can be reluctant to raise exceptions to dates that 
it doesn't understand. Therefore, it can be wise to store the 
original along with the parsed ISO formatted string. This can 
be used for manual checking if required later.

Example code::

    def date_to_iso(datestring):
        """
        Takes a string of a human-readable date and
        returns a machine-readable date string.


        >>> date_to_iso('20 July 2002')
        '2002-07-20 00:00:00'
        >>> date_to_iso('June 3 2009 at 4am')
        '2009-06-03 04:00:00'
        """
        from dateutil import parser
        from datetime import datetime
        default = datetime(year=1, month=1, day=1)
        return str(parser.parse(datestring, default=default))
  
.. _mature date parser: http://www.labix.org/python-dateutil

General tips
------------

* Minimise the pages to scrape. This will save everybody time and 
  resources.

  * Inspect any AJAX fields. AJAX is generally performed by sending 
    JavaScript objects between the server and the web browser. They
    are easy to parse and are generally very rich.
  * Try looking for a `sitemap.xml`.
  * Any pages in the `robots.txt` which disallow access are generally 
    where the bulk of the value lies.

* Run an evented or multi-threaded system. Once you have gained the 
  confidence of building a few scrapers, learn how to optimise 
  performance. Given that you are using lots of external resources,
  there will be lots of latency involved. This means that your scraper's
  performance by using asynchronous programming.


Types of scrapers
-----------------

:DOM-based approaches:
  :advantages:
     * familiar
     * relatively computationally efficient

  :disadvantages:
     * requires parsing the entire document, which can be difficult
       with messy content
     * prone to breaking when encountering unexpected content
     * can be tricky to handle errors
     * may require learning a new language, `XPath`_

  This is the most common form of scraper. All the data that you are
  looking to extract is identified by selecting portions from the DOM.

  Most modern libraries, such as `lxml`_ accept CSS selectors. So, in
  Python to extract content from the  `<title>` tag, you do something
  similiar to `page.cssselect('title')[0].text`.

  `XPath`_, the XML Path Language, is a fuller way to select elements 
   from XML and XML-like documents, such as HTML. As with CSS, it uses 
   the structure of the page and tag attributes to be able to select 
   specific elements or groups of elements. XPath expressions can look 
   fairly complex and take some some time to learn. 

:Template:
  Regular expressions to look for common patterns in the text. One of 
  the easiest template extraction systems is `scrapemark`_. While it
  is not the most computationally efficient, using template systems
  requires far less manual work to get going with. This can le

:Machine-learning:
  Machine-learning packages work by training a model of example pages,
  then asking for matching material.

  One tool that is very good at removing boilerplate, such as headings
  from web pages and only leaving the content is called `boilerpipe`_. 
  It is bundled together with the `Data Science Toolkit`_ and there is
  an `demo of boilerpipe's capabilities is available`_.

.. _boilerpipe: http://code.google.com/p/boilerpipe/
.. _demo of boilerpipe's capabilities is available: http://boilerpipe-web.appspot.com/
.. _lxml : http://lxml.de/
.. _XPath : http://en.wikipedia.org/wiki/XPath 

A scraping framework
--------------------

Let's demonstrate some of the principles that we have been talking about. 

We'll be creating a scraping framework, called `tbd`::

    """
    {{somthing}}.py : a webscraping framework..
    """
    import bsddb
    import pickle
    import urllib2
    from asynchat import fifo
    
    from dateutil import parser as date_parser
    import lxml
    import lxml.html
    
    START_URL = 'http://blog.okfn.org/'
    db = bsddb.hashopen('okfnblog.db')
    
    #
    # UTILITY FUNCTIONS
    #
    
    def get_clean_page(url):
        page = get_page(url)
        page = lxml.html.tostring(page)
        page = lxml.html.fromstring(page)
        return page
    
    def get_page(url):
        res = urllib2.urlopen(url)
        page = lxml.html.parse(res)
        page.make_links_absolute()
        return page
    
    def save_post(post):
        save(post['post_id'], post)
    
    def save_tag(tag):
        save('tag-%s' % tag['tag'], tag)
    
    def save_author(author):
        save('author-%s' % author['name'], author)
    
    def save(key, data):
        db[key] = pickle.dumps(data)
    
    def extract_created_at_datetime(post):
        date = post.cssselect('span.entry-date')[0].text
        time = post.cssselect('div.entry-meta a')[0].attrib['title']
        return str(date_parser.parse(date + ' ' + time))
     
    def process_post(url):
        source = get_page(url)
        post = {}
        post['title'] = source.cssselect('h1.entry-title')[0].text
        post['author'] = source.csselect('span.author a')[0].text
        post['content'] = source.cssselect('div.entry-content')[0].text_content()
        post['as_html'] = lxml.html.tostring(source.cssselect('div.entry-content')[0])
        post['created_at'] = extract_created_at_datetime(source)
        post['post_id'] = source.cssselect('div.post')[0].attrib['id']
        post['tags'] = [tag.text for tag in source.cssselect('a[rel~=tag]')]
        post['url'] = url
        yield save_post, post
        yield save_author, dict(name=post['author'])
        for tag in post['tags']
            yield save_tag, dict(tag=tag, post_id=post_id, author_name=post['author'])
    
    def process_archive(url):
        archive = get_page(url)
        for post in archive.cssselect('.post .entry-meta a'):
            yield process_post, post.attrib['href']
        previous = archive.cssselect('.nav-previous a')
        if previous: #is found
            yield process_archive, previous[0].attrib['href']
    
    def process_start(url):
        index = get_page(url)
        for anchor in index.cssselect('li#archives-2 a'):
            yield process_archive, anchor.attrib['href']
    
    def main():
        queue = fifo((process_start, START_URL))
        while 1:
            status, data = queue.pop()
            if status != 1:
                break
            func, args = data
            for newjob in func(args):
                queue.push(newjob[0], newjob[1])
            db.sync()
           

Dealing with JavaScript
-----------------------

JavaScript can be a pain for scrapers. JavaScript is often used to alter the
DOM when pages after the page has been created. This means that the page you
see in an internet browser is different that the page your scrapers see.

There are a few different approaches to dealing with this process. We will
briefly outline them, then go through the easiest option.

Options
^^^^^^^

There are three broad options when considering how to deal with JavaScript:

 - **Don't** Much of the AJAX content could be downloaded directly by your
   scraper. AJAX is generally sent as JSON, which means it is very easy to
   parse. You could save yourself a lot of time if you spent some time 
   evaluating the target more closely.
 - **Do it offline**  Under this approach, you download the content, send it
   to a JavaScript interpreter such as `SpiderMonkey`_, then process the
   results. If this sounds like a lot of manual work, it is. Fortunately for
   us, other people have struggled with this problem before and have 
   released software to take care of most of the detail. Take a look at
   `crowbar`_ and `webkitcrawler`.
 - **Automate a browser**  This third approach involves relying on a web
   browser's handling JavaScript itself. Until recently, this has involved 
   quite a bit of complicated effort. Now, a library called `splinter` has
   come along to make life much easier.

One of the biggest differences between the second and third options is that 
the second option does not require a monitor. That means, it can be much 
easier to deploy on a server. However, in general the tasks we'll be doing 
are fairly small and can happily run in the background while you're doing 
other work.

.. _SpiderMonkey: https://developer.mozilla.org/en/SpiderMonkey
.. _crowbar: http://simile.mit.edu/wiki/Crowbar
.. _how to write a program that processes JavaScript for you: http://blog.motane.lu/2009/07/07/downloading-a-pages-content-with-python-and-webkit/
.. _webkitcrawler: https://github.com/emyller/webkitcrawler

Path of least resistance - splinter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Splinter is Python library that takes all of the trouble out of this process::

    >>> from splinter.browser import Browser
    >>> br = Browser('webdriver.chrome')

As a trivial example, let's find Auckland's current weather from `the New 
Zealand Herald`_. If you visit their homepage without JavaScript enabled on
your internet browser, you'll see nothing. However, with JavaScript, an
icon appears ::

    >>> br.visit('http://www.nzherald.co.nz/')
    >>> high = br.find_by_css('span.high').first.value
    >>> low  = br.find_by_css('span.low').first.value
    >>> high, low
    '19\xb0', '11\xb0' # \xb0 is the degree sign
     

.. _the New Zealand Herald: http://www.nzherald.co.nz 

Dealing with PDF content
------------------------

PDF documents are a pain. Some PDF generators don't actually have the concept
of a word-- every letter is individually placed. This makes it very hard to 
create a software tool that can combine letters to make words, and combine words
to make sentences. However, depending on the source documents, there
are possibilities for extracting information from them.

The `Data Science Toolkit`_ is now the best way to get up and running with
these kinds of tasks. Its `"File to Text" tool` takes an image, PDF or MS Word 
document and returns text to you.

If you only have a few documents to process, the website actually allows you 
to do the processing on their servers.

Extracting plain text
^^^^^^^^^^^^^^^^^^^^^

A quick way to extract text from a PDF programmatically is with the Python
library, `slate`_. Disclaimer: I maintain `slate`. Its philosophy is to have
a very low barrier to entry, but only extracts plain text out of the document::


    >>> import slate
    >>> with open('salesreport.pdf') as f:
    ...    report = slate.PDF(f)
    ...
    >>> report[0]
    "2011 ..."

Digging deeper
^^^^^^^^^^^^^^

One of the better free tools is called `pdftohtml`_. It generates an HTML 
version of the document, which can then be processed by tools that you 
are used to. It does a good job of understanding the layout 

It is possible to circumvent in PDF documents. The PDF viewer `xpdf`_ 
provides this be default. This allows you to print or extract content 
that may be otherwise prevented through securirty measures.


Optical Character Recognition
-----------------------------

Creating a system for Optical Character Recognition (OCR) can be challenging.
In most circumstances, the `Data Science Toolkit` will be able to extract
text from files that you are looking for.

An excellent free tool is called `OCRFeeder`_. It is available in Ubuntu as 
the `ocrfeeder` package. To get a feel for how to use it, there is a 
`5 minute video tutorial`_ on its usage.

.. _5 minute video tutorial: http://vimeo.com/3760126
.. _OCRFeeder: http://code.google.com/p/ocrfeeder/ 


Building an OCR pipeline
^^^^^^^^^^^^^^^^^^^^^^^^

OCR involves create a programming conveyor belt of tools. The whole process
can include several steps:

  * Cleaning the content
  * Understanding the layout
  * Extracting text fragments from pieces of each page, according to the 
    layout of each page
  * Reassembling text fragments into a usable form


Cleaning the pages
^^^^^^^^^^^^^^^^^^

This generally involves removing dark splotches left by scanners,
straightening pages and adding contrast between the background 
and the printed text. One of the best free tools for this is `unpaper`_. 

File type conversion
^^^^^^^^^^^^^^^^^^^^

One thing to note is that many OCR engines only support a small number of 
input file types. Typically, you will need to convert your images to
.ppm files.

Using an OCR engine
^^^^^^^^^^^^^^^^^^^

The three main contenders in the free and open source world are:

* Tesseract OCR
* Ocropus
* GNU Ocrad

Each of those tools has a long history and is in continuous development.
With my Python bias, Ocropus is probably the easiest to get started with.

.. _unpaper: http://unpaper.berlios.de/
.. _pdftohtml: http://pdftohtml.sourceforge.net/ 
.. _"File to Text" tool: http://www.datasciencetoolkit.org/developerdocs#file2text
.. _Data Science Toolkit: http://www.datasciencetoolkit.org/
.. _slate: http://pypi.python.org/pypi/slate
.. _xpdf: http://www.foolabs.com/xpdf

Crowdsourcing
-------------

The open source project, `TaskMeUp`_ is designed to allow you to distribute jobs
between hundreds of of participants. If you have a project that could benefit 
from being reviewed by human eyes, this may be an option for you.

Alternatively, there are a small number of commercial firms providing this 
service. The most well known is Amazon's Mechanical Turk. They providing 
something of a wholesale service. You may be better off using a service such
as Cloudflower or Microtask. Microtask also has the ethical advantage of not
providing service below the minimum wage. Instead, they team up with video 
game sellers to provide in-game rewards. 


.. _TaskMeUp: https://bitbucket.org/waj/taskmeup

General Tips
--------------

Avoiding being blocked
^^^^^^^^^^^^^^^^^^^^^^

It's possible to use sophisticated techniques to circumvent rate limitations
and IP address blocking. However, the best technique for avoiding being blocked
is by being a good netizen and adding pauses between your requests.

Scrape during the night of the site's local time. This is very likely to have 
very few users, meaning the site will have more capacity to serve your scraper.


Be part of the open data community
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When scraping open data, you should use `ScraperWiki`. ScraperWiki
allows people to cooperatively build scrapers. They will also take care of 
rerunning your scraper periodicly so that new data are added.

By being part of the community, you increase your profile, learn much more 
and benefit from people fixing your scraper when it breaks.

Learn async programming
^^^^^^^^^^^^^^^^^^^^^^^

Network programming is inherently wasteful in many ways. Your processor is
consistently waiting for things to arrive from other parts of the world.
Therefore, you can speed up the processing steps of your scrapers significantly
if you take the time to learn asyncronous programming.


.. _ScraperWiki: http://www.scraperwiki.com/
.. _scrapemark: https://github.com/arshaw/scrapemark

========================================================
Case study: How to build your city's open data catalogue
========================================================

Max Ogden has a great post about the practical steps needed to build 
an open data API for a city.


=======================
How to clean your data
=======================

Whether you have gathered your data from an open data catalogue or have
scraped it yourself, it's likely that it will be in an inconsistent 
state.

Tools to use
------------

- Google Refine
- 

