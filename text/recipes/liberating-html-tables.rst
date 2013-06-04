===========================
Liberating HTML Data Tables
===========================

.. sectionauthor:: Tony Hirst (psychemedia on Twitter)

It's not uncommon to see small data sets published on the web using an HTML table element. If you have a quick click around Wikipedia, you're likely to find a wide variety of examples. Some sites will use Javascript libraries to enhance the presentation or usability of a table, for example, by making columns sortable; but most of the time, we are faced with a flat HTML table, and the data locked in it.

In this section, we look at some quick tricks for liberating data from HTML tables on public webpages and turning them into something more useful.

Screenscraping HTML Tables Using Google Spreadsheets
----------------------------------------------------

The Google spreadsheet formula:: 

  =importHTML("","table",N)

will scrape a table from an HTML web page into a Google spreadsheet. The URL of the target web page, and the target table element both need to be in double quotes. The number N identifies the N'th table in the page (counting starts at 1) as the target table for data scraping.

So for example, have a look at the following Wikipedia page – `List of largest United Kingdom settlements by population 
<http://en.wikipedia.org/wiki/List_of_largest_United_Kingdom_settlements_by_population>`_ (found using a search on Wikipedia for UK city population):

.. image:: http://farm9.staticflickr.com/8303/7850933084_b188c02992_o_d.jpg

Grab the URL, fire up a new Google spreadsheet, and start to enter the formula *=importHTML* into one of the cells:

.. image:: http://farm9.staticflickr.com/8284/7850932578_b5db80ed9d_o_d.jpg

Autocompletion works a treat, so finish off the expression and add in the URL and table number::

  =importHTML("http://en.wikipedia.org/wiki/List_of_largest_United_Kingdom_settlements_by_population","table",2)

The table numbers are not always obvious - start with 1 and increment the
table number until you get the correct one.

.. image:: http://farm9.staticflickr.com/8438/7850932674_ef1514b761_o_d.jpg

As if by magic, a data table appears in the spreadsheet, pulled in directly from the Wikipedia page:

.. image:: http://farm9.staticflickr.com/8425/7850932816_b5598830e0_o_d.jpg

If the data in the HTML table is updated, the data in the spreadsheet will also be updated when you refresh or call the spreadsheet page.
