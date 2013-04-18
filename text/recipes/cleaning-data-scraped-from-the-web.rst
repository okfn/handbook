=====================================
Cleaning up Data Scraped from the Web
=====================================

.. sectionauthor:: Tim McNamara <tim.mcnamara@okfn.org>

This section deals with how you can clean up data - having extracted it from the web by scraping.  

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
can help. We make use of the `lxml`_ library. It's very good at 
understanding broken HTML and will render a perfectly-formed page for 
your extractor functions. 

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
these values will make any automatic comparisons much richer::

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

If you're extracting numbers from HTML tables, they will each be 
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