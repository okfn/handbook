=================================================
Introducing SQL for Lightweight Data Manipulation
=================================================

*Author: Tim McNamara*

This article introduces the SQL language as a tool for people interested in
using data to create visualisations and other forms of data analysis.

About the data
--------------

This article uses some housing price data from New Zealand. Here, you use
[Trademe](http://www.trademe.co.nz). So I've used Trademe's
[API](http://developer.trademe.co.nz) to pull out data from a few thousand
properties on the market. Unfortunately, the terms of the API restrict
redistribution.

Getting the workable data out of the database
---------------------------------------------

Now that we have all of the data at our disposal, we need a way to extract it.
We can use the SQL language to easily manipulate the data we need. My data is
stored in the [SQLite3](http://www.sqlite.org) database.
.
[SQLite3 has its own command line shell](http://www.sqlite.org/sqlite.html)
that that's very easy to install on Ubuntu:

    $ sudo apt-get install sqlite3

Invoking it is trivial:

    $ sqlite housing-data.db


First touch of SQL
===================

Now, let's count up how many houses we were able to extract data from::

  sqlite> <b>SELECT count(*) FROM residentialproperty;</b>
  4151

Great. Now, how many of those houses are actually useful for us? Unfortunately,
far fewer. Take a look at this query::

  sqlite> SELECT count(*) 
     ...> FROM residentialproperty 
     ...> <b>WHERE rateable_value > 0;</b>
  2357

The addition of WHERE clauses allows us to filter the result. While the fact
that we've lost half of our data wont affect the training exercise, it does
demonstrate some of the issues of using real-world data. The effect is
magnified as we ask for even cleaner data::

  sqlite> SELECT count(*)
     ...> FROM residentialproperty 
     ...> WHERE rateable_value > 0 <b>AND area > 0</b>;
  1290

We're only doing univariate logistic regression in this example, so a single
variable is fine. It's about the extent of the calculus that I can take for the
moment. 

Let's take a look at the data itself, just so you can get a feel for what's
happening::

  sqlite> <abbr title="We choose which columns we want..."><b>SELECT rateable_value, area, land_area</b></abbr>
     ...> FROM residentialproperty
     ...> WHERE rateable_value > 0 AND area > 0
     ...> <abbr title="...and limit the number of rows to return">LIMIT 10</abbr>;
  360000|183|993
  235000|100|738
  435000|140|725
  510000|180|759
  142000|100|675
  370000|210|1346
  325000|46|0
  385000|100|371
  205000|100|991
  465000|181|1130  

It's hard to make out, but there seems to be a correlation between these
variables. On the left is the government's valuation (known here as the
rateable value, as land taxes are known as rates here in New Zealand). The
middle column is the reported surface area of the dwelling. The right-hand
column displays the size of the land.

Sidebar: Syntax
-------------------

SQL uses a semicolon as a full stop.

The language is quite relaxed when it comes to whitespace. You will see a few
variations of indentation in this article. Feel free to experiment with what
suits you best.

I tend to use capital letters for SQL keywords, but that is not required. Some
people may look down on it as formal and stuffy. But, I tend to find the
formality is a feature, not a bug.


Tidying up output
-----------------

We can improve how this looks, by the way. The sqlite3 utility is somewhat
intimidating, but it's simple once you spend a few moments getting used to it.
Here are a few useful commands::

    sqlite> .help
    ...
    sqlite> .prompt "> " ". "
    > .mode column
    > .headings on
    > .width 14 10 10 8 9

Now, if we call up another query, we'll see a much more readable output::

    > SELECT rateable_value AS `rateable value`, 
    .        area AS `floor area`,
    .        land_area AS `land area`, 
    .        bedrooms, 
    .        bathrooms
    . FROM residentialproperty
    . WHERE rateable_value > 0 AND area > 0
    . LIMIT 10;
    rateable value  floor area  land area   bedrooms  bathrooms
    --------------  ----------  ----------  --------  ---------
    360000          183         993         4         1        
    235000          100         738         3         1        
    435000          140         725         4         1        
    510000          180         759         3         2        
    142000          100         675         3         1        
    370000          210         1346        4         1        
    325000          46          0           2         1        
    385000          100         371         2         1        
    205000          100         991         3         1        
    465000          181         1130        4         2  

Aggregates
----------

As well as displaying data in raw form, databases also include power to provide
you summaries of the data::

  > SELECT <abbr title="Functions look like functions from other languages">max(area), avg(area), min(area)</abbr>
  . FROM residentialproperty WHERE area > 0;
  2100            156.927513015619  20        

As always with numeric data manipulation, be careful of values like 0 or 99999.
Either of those can be a placeholder for an unknown quantity. They will really
ruin your values. Consider the difference between these two queries::

  > SELECT avg(rateable_value) FROM residentialproperty;
  <b>234629.451698386</b>

  > SELECT avg(rateable_value) FROM residentialproperty
  . WHERE rateable_value > 0;

  413214.617734408

Databases support a wide range of functions out of the box. Check your
[database's documentation](http://www.sqlite.org/lang_corefunc.html) for
details.


Categorical Data
----------------

If we are looking at categorical data, there are a few handy operations worth
knowing about. Let's try to find the number of suburbs that are represented in
our sample::

  > SELECT <b>count(DISTINCT suburb)</b> FROM residentialproperty;
  142

Functions that take a single argument are allowed to include a DISTINCT keyword. Very cunning.

Now, what if we would like to see which regions are selling the most houses. We
can introduce the GROUP BY clause::

  > SELECT suburb, count(*)
  . FROM residentialproperty
  . GROUP BY suburb;
  suburb              count(*)
  ------------------  ------------------
  Akatarawa           9
  Alicetown           11
  Aotea               30
  Aro Valley          7
  ...    
  Waterloo            20
  Wellington Central  130
  Whitby              77
  Whitemans Valley    4
  Wilton              4
  Woburn              20
  Woodridge           3
  York Bay            1

We can combine this with what we have already learned to create useful reports::

  > .width 20 3 8 10 10
  > SELECT suburb, 
  .        count(*) AS `n`,
  .        min(rateable_value) AS `min ($)`, 
  .        avg(rateable_value) AS `avg ($)`, 
  .        max(rateable_value) AS `max ($)`, 
  .        max(rateable_value) - min(rateable_value) AS `range ($)`
  . FROM residentialproperty
  . WHERE rateable_value > 0
  . GROUP BY suburb;
  suburb              n     min ($)   avg ($)     max ($)     range ($) 
  Akatarawa           8    180000    470625.0    850000      670000
  Alicetown           4    360000    421250.0    475000      115000
  Aotea               9    180000    443888.888  595000      415000
  Aro Valley          4    390000    577500.0    670000      280000
  ...
  Wallaceville        6    120000    217500.0    330000      210000
  Waterloo            7    295000    427142.857  590000      295000
  Wellington Central  69   106000    520188.405  4135000     4029000
  Whitby              45   76000     419155.555  900000      824000
  Whitemans Valley    1    550000    550000.0    550000      0
  Wilton              3    440000    500000.0    565000      125000
  Woburn              10   390000    582000.0    760000      370000
  Woodridge           2    500000    565000.0    630000      130000
  York Bay            1    510000    510000.0    510000      0
  </code></pre>

Dates
-----

Databases also generally know quite a bit about dates. For example, the following function tries to see how current the listing date is::

    > SELECT (
    .           strftime('%s', datetime('now')) - 
    .            strftime('%s', start_date)
    .        ) / 60 / 60 / 24
    . FROM residentialproperty
    . WHERE start_date > datetime(1, 'unixepoch')
    .   AND end_date > datetime(1, 'unixepoch'); 

This example is a little bit messier than the others. That's probably because
of the <code>strftime</code> function that's inserted there.
<code>strftime</code> is a function that take a <b>str</b>ing and
<b>f</b>ormats it to time. We are using <code>'%s'</code> as the format,
telling the function to convert things to seconds.

The SELECT clause is converting the current time and the auction's listing date
into seconds. It then divides this into days. I've left this as multiple divide
operations for readability. The WHERE clause is similar to asking for greater
than zero. A quirk of my processing was that empty dates were sent to the
database as 1 Jan 1970, which is second 0 of the [UNIX
epoch](http://en.wikipedia.org/wiki/Unix_time). Omitting this would really skew
the results.

Knowing about dates could be handy if we wanted to model data that is no more
than 90 days old. To do that, move our "dates from today" function to the WHERE
clause and add a comparison::

    > SELECT suburb, rateable_value, bedrooms, bathrooms
    . FROM residentialproperty
    . WHERE start_date > datetime(1, 'unixepoch')
    .   AND end_date > datetime(1, 'unixepoch')
    .   AND (
    .         strftime('%s', datetime('now')) - 
    .         strftime('%s', start_date)) / 
    .         60 / 60 / 24 
    .       ) <= 90
    . LIMIT 5; 
    suburb              rateable_value      bedrooms   bathrooms
    ------------------  ------------------  ---------  ---------
    Paekakariki         360000              4          1        
    Porirua East        235000              3          1        
    Waikanae Beach      0                   3          1        
    Raumati South       0                   3          2        
    Berhampore          0                   4          2        
    Waiwhetu            435000              4          1        
    Kaiwharawhara       0                   0          0        
    Thorndon            0                   6          2        
    Ngaio               0                   3          2        
    Maoribank           0                   2          1        

Now, I guess your first reaction is "Wow, Wellington has some strange place
names." I'll let you look into Wikipedia for the appropriate pronunciation.
Hopefully your next thought is, "Wow, that's a pretty complex set of operations
without for loops or nested if statements." I know that programming can be
intimidating. However, for ad-hoc data analysis, SQL can provide a lot of
benefit.

I have put the computationally intensive operation at the end of the WHERE
clause. This is so that this processing only needs to occur on those rows which
have passed the suitability test.

Exporting Data
==============

Sending data to your application is probably one of the easiest things that you
can do. Once you have your query in the way that you want it, you just set the
mode to CSV output to a file:

    > .mode csv
    > .output results.csv
    > SELECT ... ;
    > .output stdout

Why use this approach
=====================

**Programming is reproducible.** While it's convenient to work away at data in
a spreadsheet program, sometimes it can be hard to retrace your steps. It's
sometimes even harder to describe to other people how you've come to a result.

**No loops!** Once you get the hang of it, programming in SQL can be a lot
easier than preforming similar operations in languages. You no longer need to
spend a great deal of time worrying about complex control structures.  

**Databases are everywhere.** While NoSQL databases are increasingly being
used, relational data are all around us. SQL is the interface to all of that
data. For example, the tens of millions of records extracted by the ScraperWiki
community is stored in SQLite. 

**Emailability.** A SQLite file can be shared with anyone or stored anywhere.
It doesn't need software to be installed for it to work perfectly well.


When not to use this approach
=============================

SQL does not tolerate messy data. When data are irregular, use something like
Google Refine to clean it up.

Take some time to understand the behaviour of NULL. It is the placeholder for
missing values. We have ignored talking about the complexities of NULL in this
article.

Further Reading
===============

I have left out a fews things which are really important. Most importantly, how
to deal with multiple relations/tables. I've also omitted string functions.
These two resources go over these points really well:

* [A Gentle Introduction to SQL using SQLite](https://github.com/tthibo/SQL-Tutorial) by Toby Thibodeaux. This is one of the most readable tutorials I've encountered. It will really whet your appetite.
* [Command Line Shell For SQLite](http://www.sqlite.org/sqlite.html) by D. Richard Hipp et al. 

