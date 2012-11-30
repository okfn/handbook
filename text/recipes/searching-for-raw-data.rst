Searching for raw data
======================
.. sectionauthor: Tim McNamara

So you want data. But, you would like to use tools that you are already
familiar with. That way, you can focus on areas of most interest to you:
analysis.

Let’s consider the example of someone who is looking for air pollution
information in Sydney, Australia. Australia has an data catalogue at
data.gov.au. But it’s likely that the catalogue will be hard to search
through, may be incomplete, and may only give us the phone number or email
address of someone to talk to. Google spends hundreds of millions of
dollars a year indexing the web. Let’s make use of that.

To start with, let’s see how close we get just with::

  sydney air pollution

Actually, we get pretty close. The first link takes us to the relevant
`government department’s web visualisation tool of Sydney’s “Air Quality Index” (AQI)`_. Within one click, I could get to a web table with live data
in it. But, it seems impossible to get to the raw data. By inspecting the
HTML source, it turns out that the table is living within an ``iframe`` to 
`airquality.environment.nsw.gov.au`_. This seems to be a bespoke web
application that doesn’t provide access to its raw data.

Maybe someone has created a dump of the AQI?

The first change we could make to our query is by adding a filetype
operator. To look for Excel spreadsheets, we simply add::
  filetype:xls

If we would like to include .xlsx files, we can use brackets and a pipe
character. To Google, this says, “either is fine”::

 (filetype:xls | filetype:xlsx)

The first link is a World Bank source, which provides information about
countries’ air pollution. While we may not have the source that we wanted,
we have some raw data to play with as a fallback.

The problem with Excel spreadsheets is that they tend to have lots of
formatting issues. Columns are inconsistent. There may be images or
explanatory text. These characteristics occur because spreadsheets are
created by people for people. They’re made easier for people to read, which
tends to make it harder for machines to read. But, there is something
better, CSV.

CSV is a great format. It’s plain text. It’s easy. It’s readable by
everything. Most importantly though, it’s almost always written by & for
machines. This makes it very easy for you to do analysis with. So how do we
find CSV files? Same as before::

  filetype:csv

Another format that’s worth mentioning here is TSV. Exactly the same as
CSV, but tend to be slightly easier for people to read. You may as well
look for both::

  (filetype:csv | filetype:tsv)

This will return many results that look like they do on your hard drive:
``http://www.example.com/results.csv``. Unfortunately, many dynamic websites
do not use file extensions. Instead, they will do something like this:
``http://www.example.com/results?format=csv``. The ``filetype:`` operator will miss
these ones, because the search engine doesn’t think they look like files.
To improve our coverage, let’s introduce ``inurl:``::
  (filetype:csv | filetype:tsv | inurl:csv | inurl:tsv)

Magic. Our search queries are now able to find those files. Beware though,
that ``inurl:`` will result in several false positives. However, it will also
result in much more data. Including data from several countries that we’re
not really interested in. How do we change that?

Use the ``site:`` operator. The interesting thing about ``site:`` is that it’s
useful for more than sites. We can use it to restrict results to particular
level domains. If we were only interested in Australian results, then we
could ask Google to filter them for us::
  site:.au

We can actually get far more specific. We we’re interested in government
sources, just ask for them::
  site:.gov.au

One final operator that is useful to mention is ``ext:``. One of the problems
with ``filetype:`` is that it tends to perform poorly with more specialised
file formats. These include XML files, Atom feeds, ESRI Shapefiles and
other industry-specific formats.

Let’s return to the problem at hand. We would like to receive a
machine-readable dump of the API from Sydney, Australia. Ideally, we will
get our data from a government source. That means we need to construct a
query that combine many of the approaches::

  sydney air pollution (filetype:csv | filetype:tsv | ext:xml) site:.gov.au


The first result is something from stored at New South Wales Ministry of
Health. It’s labelled “env_airaqi.csv”. Further inspection reveals that it
provides samples from the original data source that we could only access
via a web page. Bingo!

A reminder about copyright
--------------------------
Remember, you probably shouldn’t be distributing the files that you find.
There’s the possibility that you will be infringing copyright. Stick to
publishing the analysis or visualisations of the data. Those are your creative
works. They don’t count as derived works. Copyright protects the expression
of facts, not the facts themselves.

Summary
-------

* ``filetype:csv`` is the most likely way to get raw data quickly
* ``inurl:csv`` will reveal even more sources, but will return false positives
* ``site:.gov.uk`` restricts the results to websites from the British government
* ``ext:xml`` returns formats that are not indexed by filetype operator

.. _government department’s web visualisation tool of Sydney’s “Air Quality Index” (AQI): http://www.environment.nsw.gov.au/aqms/aqi.htm
.. _airquality.environment.nsw.gov.au: http://airquality.environment.nsw.gov.au/aquisnetnswphp/getPage.php?reportid=2
