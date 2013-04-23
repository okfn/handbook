======================
Cleaning spending data
======================

Often, you will need to clean up the spending data that you receive. Even government data is not perfect. 

In this section, we highlight some common issues experience when working with spending data. 

In the recipe book - you will find a recipe to help you solve these issues. 

Common issues with spending data: 

* **Typos** - E.g. some of your cells contain “Rroceeds from global taxes” rather than “Proceeds from global taxes”
* **Inconsistencies** - You may be looking to try and find out how much money does company X receive from government. However in your data, sometimes the company is entered variously as "Fuzzy Robot Llama Exporters", "Fuzzy Robot Llama Exporters Ltd", "FRLE Ltd" - you need a way to tell that these are all the same. 
* **Blank columns, rows and cells** - When you are summing up values it is very important to know what is a genuine zero and what is a blank due to the absence of data. 
* **Human Friendly Formatting** - such as pseudo rows and things being in horizontal rows when you need them in verticals - your computer probably needs the computer to be laid out somewhat consistently if it is to be able to process it.  
* **Multiple types of information contained in a single column**. For example:  

========================  ============
Revenue, Extractives      300,000,000
Revenue, Taxation         100,000,000
Expenditure, Healthcare   50,000,000
=======================  ============

Actually, it would be more helpful to have a column just to have one column with just whether a transaction was revenue or expenditure and a second to allow you to filter by revenue / expenditure type. 

* **Whitespace** - You don't see it, but it causes big problems in datasets. To many databases, the two transactions below would be treated differently due to the extra space at the end: 
=====================  =============
Fiscal revenue          50,000
Fiscal revenue[space]   50,000
======================  =============

So if you ever filtered or searched for just "Fiscal revenue" [no space at the end] - you would actually be omitting the latter case - possibly leading to incorrect conclusions. You can remove the nasty white space quite easily. 

Normalizing data
----------------

Data that comes from the government is often generated across multiple departments by hand. This can result in inconsistencies in what kinds of values or formats are used to describe the same meaning. Normalizing values to be consistent across a dataset is therefore a common activity.

Step 1: Find all distinct values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, you want to start by finding all of the distinct ranges of values for the different columns in your dataset. You can accomplish this by using a database query language (such as SQL's DISTINCT), or by simply using the 'filter' property on a spreadsheet program.

For example, if you have a spreadsheet with contracting data, and one column is 'Competed?', you would expect the values to be 'yes' or 'no'. But if this spreadsheet is an amalgam of spreadsheet data from multiple users and departments, your values could vary among the following: 'Y', 'YES', 'yes', 1, 'True', 'T', 't', 'N', 'NO', 'no', 0, 'False', 'F', 'f', etc. Limiting all of these potential values to two clear options will make it easier to analyse the data, and also easier for those who follow in your footsteps.

Step 2: Sanity Check
^^^^^^^^^^^^^^^^^^^^^

Especially with financial data, numbers can be formatted several different ways. For example, are your negative values represented with a '-' or placed inside '( )' or possibly even highlighted in red? Not all of these values will be easily read by a computer program (especially the color), so you'll want to pick something clear and consistent to convert all your negative values to (probably the negative sign).

Is all your numerical data measured out in ones or is abbreviated in thousands? Especially with budget data, order of magnitude errors are not uncommon when one department thinks they're reporting in thousands or millions by default but others expand their data all the way to the ones place. Are some values in scientific notation (e.g. 10e3938)? Make sure all your values are consistent, otherwise your analysis could contain serious errors.

A column of data requiring name normalization:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: http://content.openspending.org/resources/handbook/static/Screen%20Shot%202012-11-15%20at%2011.34.49%20AM.png



Challenge: Wrangle the data
---------------------------

.. raw:: html

  <div class="well">

**Task:**  

Read the `recipe`_ from the handbook walking you through cleaning up a spending dataset.

.. _recipe: 

Take the sample dataset and replicate the steps there. 

Remember - once you've cleaned your data, share it and save someone else the job! Why not upload to `the OpenSpending group on the datahub`_ and drop the `OpenSpending Mailing List`_ a line to say you have done so, people are always looking for raw data to visualise and explain. 

**Extra Credit:** 

Take a dataset from your own country and clean it up ready to go into a database. 

  .. _the OpenSpending group on the datahub: http://datahub.io/dataset?groups=openspending&q=openspending 
  .. _OpenSpending Mailing List: http://lists.okfn.org/mailman/listinfo/openspending
.. raw:: html
  
  </div>


