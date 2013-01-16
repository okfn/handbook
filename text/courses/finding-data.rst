Finding Data
============

Introduction
------------

Now we know what data is and the questions we’re interested in we’re ready to go out and hunt for it online.

In this tutorial, you will learn where to start looking for data. We will then look at different ways of getting hold of data, before setting you loose to find data yourselves!

Data Sources 
------------

There are three ways of getting hold of data: 

#. **Finding data** - this involves searching and finding data that has already been released 
#. **Getting hold of more data**  - asking for ‘new’ data from official sources e.g. through Freedom of Information requests. Some data is hidden away in websites that are hard to navigate - but don’t give up! This data can be liberated with what datawranglers call ‘scraping’. 
#. **Collecting data yourself** - This means gathering data and entering it into a database or a spreadsheet - whether you work alone or collaboratively.

In this tutorial we’ll focus on (1) Finding data that already has been released. 


Several sources frequently release data for public use:

#. **Government** In recent years governments have begun to release some of their data to the public. Many governments host special (open) government data platforms for the data they create. For example the UK government started `data.gov.uk`_ to release their datasets. Similar data portals exist in the `US`_, `Brazil`_ and `Kenya`_ - and in many other countries! Does your country have an open data portal (`Datacatalogs.org`_ is a good starting point)?
#. **Organisations** Other sources of data are large organisations. The `WorldBank`_ and the `World Health Organization`_ for example regularly release reports and data sets.
#. **Science** Scientific projects and institutions release data to the scientific community and the general public. Open data is produced by `NASA`_ for example, and many specific disciplines have their own data repositories, some of which are open. More and more initiatives exist trying to provide access to already published data (e.g. `Dryad`_)

.. _data.gov.uk: http://data.gov.uk
.. _US: http://www.data.gov
.. _Brazil: http://dados.gov.br/
.. _Kenya: https://opendata.go.ke/
.. _WorldBank: http://data.worldbank.org
.. _World Health Organization: http://www.who.int/research/en/
.. _NASA: http://data.nasa.gov/
.. _Dryad: http://datadryad.org/

To help people to find data, projects like the Open Access Directory’s
`data repository list`_ or the Open Knowledge Foundation’s `datahub.io`_
have been started. They aim either to collect data sources, or collect
together different data sets from various sources. Also the School of Data
is building a list of `data sources`_ with your help!

.. _data repository list: http://oad.simmons.edu/oadwiki/Data_repositories
.. _datahub.io: http://datahub.io

.. raw:: html
  
  <div class="well">

**Task:** Are there any data sources we missed? What kind of data would be
most interesting to you? Add them to our list of `data sources`_

.. raw:: html
  
  </div>

.. _data sources: http://schoolofdata.org/datasources/

.. raw:: html

  <iframe src="http://p2pu.schoolofdata.org/tip/find-data-with-google.html"
  width="100%" height="330" style="border: none;"></iframe>

Now that you have an overview of some of the key concepts related to data, it’s time to start hunting for your own! To begin with, let’s return to the question that we posed at the beginning of this module

Downloading Data from the Worldbank
-----------------------------------

We started out with the question how healtcare spending affects life expectancy around the world. This is one of the answers we can find looking at data from the worldbank.

**Walkthrough:** Downloading Data from the Worldbank

#. Open the worldbank data portal: it lives in http://data.worldbank.org 
#. Select ``Data Catalog`` from the menu on the top.

   .. image:: http://farm9.staticflickr.com/8180/8051105884_f23e200bae_o_d.jpg 
#. In the long list on the bottom find “World Development Indicators”
#. Click on the blue ``databank`` button next to it.

   .. image:: http://farm9.staticflickr.com/8454/8051105990_7a7467bf79_o_d.png
#. You’ll find a very different site: The Databank - The databank is an interface to the worldbank database. You can select what data you want to see from which countries for what period of time.
#. First select the countries. We’re interested in all the countries click on ``select all`` in the country view and then on ``next``

   .. image:: http://farm9.staticflickr.com/8181/8051106310_86ffe90bdc_b_d.jpg 
#. Now you’ll see a long list of data series you can export. We’ll need a few of them.
#. First we are interested in healthcare expenditure so type “Health” in
   the little search box on the top of the list and click ``Go``
#. Select “Health expenditure, private (% GDP)”, “Health expenditure,
   public (% GDP)” and “Health expenditure, total (% GDP)”. And click on
   ``Select``

   .. image:: http://farm9.staticflickr.com/8033/8051099651_aeec6d8ec3_b_d.jpg      
#. Since the expenditure is in % of GDP we’ll need to get the GDP as well. Since we want to compare countries directly we’ll need GDP in US$. To do this type GDP into the search box and find the entry “GDP (current US$)”
#. If we want to see how healthcare expenditure affects the life expectancy we need to add life expectancy to the data.
#. Now let’s add one more thing: Population - like this we can calculate how much is spent by and on an average person. Search for “Population” and select “Population, total”.
#. Bring GDP and Population to the top with the arrows on the side of the list, your selection should now look like this:

   .. image:: http://farm9.staticflickr.com/8451/8051099565_9274f466e7_b_d.jpg
#. Click on ``Next`` to select the years we are interested in. 
#. To keep things simle, select the years 2000-2012 (you can do multiple
   selections by either pressing ``ctrl`` or ``shift``). And click ``next``,
#. You’ll see an overview screen now on the top left there is a rough layout of how your downloaded file will look like. You’ll see “time” in the columns bit and “series” in the rows bit - this influences how the spreadsheet will look like.
   
   .. image:: http://farm9.staticflickr.com/8462/8051106168_62d3a4032a_o_d.png
#. While this might be great for some people: The data is a lot easier to handle if all of our “series” are in columns and the years are different rows. So let’s change this.
#. Simply drag the “time” from columns to “rows” and the “series” from rows to columns
#. Your arranged organization diagram should look like this:
   
   .. image:: http://farm9.staticflickr.com/8317/8051099813_f707789d17_o_d.png
#. Now let’s go and ``Export``
#. If you click on the ``Export`` button a pop up will appear asking you
   for the format. Select ``CSV``.
#. You will then be able to download a file - store and name it in a folder so you remember where it comes from and what it is for.

.. raw:: html

  <div class="well">

**Task:** If you found your own alternative data to answer this question, congratulations! Take a moment to upload it to the datahub.io - and have a browse to see what other School of Data learners have found.


**Extension Task:** Explore the web, and see what open data you can find. If you find something really interesting and think of an exciting question it could help to address, tweet it to @SchoolofData - or write a short post for the School of Data blog. 

.. raw:: html
  
  </div>

Summary
-------
In this tutorial we discussed how we get the data to answer our question. We explored different ways of accessing data sources and introduced several resources listing different data portals and search engines.


We posed ourselves a question: ‘How does healthcare spending influence life expectancy?’, and have found a dataset from the WorldBank that will help us to answer that question.


Extra Reading
-------------

1. How to upload data to datahub.io http://vimeo.com/45913395 
2. `scraperwiki.com`_ a plattform for scraping documents to get more data

.. _Datacatalogs.org: http://datacatalogs.org
.. _scraperwiki.com: http://scraperwiki.com

Quiz
----

Take the following quiz to check whether you understood where to find data.

.. raw:: html
   
      <iframe 
         src="http://okfnlabs.org/scodaquiz/index.html#data/finding-data.json"
            width="100%" height="850" frameborder="0" marginheight="0"
               marginwidth="0">Loading...</iframe><br/><br/>

.. raw:: html 
 
   <a href="../sort-and-filter/" class="btn btn-primary btn-large">Next 
     Course<span class="icon-arrow-right"></span></a> 

