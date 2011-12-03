=====================================================
Wrangling a Dataset with the DataHub and its Webstore
=====================================================

Your need: get a dataset together and make it available online.

We're going to show a quick and easy way to do this using the DataHub_ and
either Google Docs or the DataHub Webstore_.

.. note:

  We will assume below that the data can ultimately take a tabular like form but this is by no means required to use the DataHub_

.. _Webstore: http://github.com/okfn/webstore
.. _DataHub: http://thedatahub.org/
.. _CKAN: http://ckan.org/

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
form `todo.getthedata`.

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

*Note: step 2 and 3 will often occur in parallel.*

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

1. Create a :term:`CSV` file (this is much preferred as a format to e.g. a excel file)

2. Either the data to the DataHub.
   
   * Either: (Best) Upload it to the Webstore (see next item) and then add
     Resource entry in the Resources section of your DataHub dataset linking to
     your Webstore file

   * Just upload the file directly to the DataHub - go to Resources in edit
     section and then choose 'Upload a File'

.. note::

    If using google doc the simplest option is just to create a Resource in your
    DataHub dataset linking to the google doc. (NB: if you do this, ensure that you
    have made your google doc publicly accessible and that you have *also*
    published it to the web -- see file menu -> publish to the web).


Upload to the Webstore
----------------------

The easiest way to do this at present is to use the command line tool
:term:`curl`. You will also need your DataHub API key (see your account page).

Peform the following on the command line::

  curl --data-binary @myfile.csv -H "Authorization: {datahub-api-key}" -i -H "Content-type: text/csv" -X PUT http://webstore.thedatahub.org/{user-name}/{db-name}/{table-name}

Values in '{...}' should be replaced with a value your choose.

  * {table-name}: suggest using `data` as a standard default
  * {db-name}: suggest using the same name as your DataHub dataset

If you want to delete the table in order to re upload it do::

  curl -H "Authorization: {datahub-api-key}" -i -X DELETE http://webstore.thedatahub.org/{user-name}/{db-name}/{table-name}

