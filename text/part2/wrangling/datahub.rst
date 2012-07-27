===================================
Publishing a Dataset on the DataHub
===================================

This tutorial will show you how to publish a dataset online using the DataHub.

Along the way you may get to do a bit of data wrangling (finding, cleaning and
fixing up data).

.. note:

  We will assume below that the data can ultimately take a tabular like form
  but this is by no means required to use the DataHub_

.. _DataHub: http://datahub.io/

Step 0 - Identify a Dataset to Use
==================================

For this purposes of this tutorial you will want to have some raw data which
you want to put up on the DataHub. If you don't have one to hand we suggest you
just use some of the raw data from this `Gold Prices Dataset`_ on the DataHub
(just pretend you dug it up somewhere on the Internet!).

.. _Gold Prices Dataset: http://datahub.io/dataset/gold-prices


Step 1 - Boot a DataHub Dataset
===============================

Create a Dataset on the DataHub_. Do not worry if you have not, yet, got the
raw data -- it is still a good idea to create the dataset entry now. Creating a
dataset at this point is doing 2 things:

* Creating a nice permanent online address (the dataset URL) which you and
  others can come back to.
* Creating a project workspace for your data wrangling endeavours where you can
  record notes and links as you go along.

In addition to a title, add a short description to your dataset, and any other
relevant links, tags etca. If you don't have the data yet, add a tag of the
form `todo.getdata`.

You may also want to boot a document (such as :term:`etherpad`, or text file)
which will serve as your scratchpad and :term:`README` where you can record
notes, links etc as you go along -- a bit like your data wrangler lab notebook.
You will then periodically dump this -- or a cleaned up version -- into the
your dataset notes on the datahub.

NB: you can just use the notes section of your DataHub dataset all along and
forget having a separate local document -- however a) you may be working
offline b) many people like using their favourite text editor!

Step 2 - Get the Data
=====================

.. note:

   Step 2 and 3 will often occur in parallel.*

Start digging for the data. This isn't our subject here so we leave the details
to you. What we do suggest is you upload or links to data you find in your
DataHub dataset (even if it's just PDF!).

Step 3 - Wrangle the Data
=========================

Now you've found raw data it's time to get it in stanard machine readable form.
We're going to focus on a tabular, spreadsheet style setup here though this may
not always be appropriate for your data (for example, it may be good for
geodata).

We suggest two approaches:

* Use google docs spreadsheets
* Use your favourite spreadsheet application
* Use command line tools

The result of this process should be a spreadsheet representing our 'refined' data.

Step 4 - Add refined data to your dataset
=========================================

1. Create a :term:`CSV` or Excel file (CSV is much preferred as a format to e.g. a excel file)

2. Add the data to the DataHub. Just upload the file directly to the DataHub -
   go to Resources in edit section and then choose 'Upload a File'.
   
   * If you are using Google Docs you can get a CSV link directly from Google
     Docs. Go to File -> Publish to the Web. Hit Start Publishing and select
     CSV. Choose the relevant sheet and then copy the url. Then use that URL
     when creating your Data Resource on the DataHub.

.. note::

    If using google doc the simplest option is just to create a Resource in your
    DataHub dataset linking to the google doc. (NB: if you do this, ensure that you
    have made your google doc publicly accessible and that you have *also*
    published it to the web -- see file menu -> publish to the web).

