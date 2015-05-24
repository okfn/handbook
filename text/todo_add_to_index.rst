=======================================
Welcome to the School of Data Handbook
=======================================

The School of Data Handbook is a companion text to the `School of Data`_. Its
function is something like a traditional textbook - it will provide the detail
and background theory to support the School of Data courses and challenges.

The Handbook should be accessible to all learners. It comes
with a :doc:`appendix/glossary` explaining the important terms and concepts. If you
stumble across an unexplained term or a concept that requires more explanation,
please do get in touch.

.. _School of Data: http://schoolofdata.org/

========================
Data Processing Pipeline
========================

The Handbook will guide you through the key stages of a data project. These stages can be thought of as a pipeline, or a process. 

Processing stages for data projects
-----------------------------------
While there are many different types of data, almost all processing can be expressed as a set of incremental stages. The most common stages include data acquisition, extraction, cleaning, transformation, integration, analysis and presentation. Of course, with many smaller projects, not each of these stages may be necessary.

An introduction to the data pipeline
------------------------------------

* **Acquisition** describes gaining access to data, either through any of the methods mentioned above or by generating fresh data, e.g through a survey or observations.
* In the **extraction** stage, data is converted from whatever input format has been acquired (e.g. XLS files, PDFs or even plain text documents) into a form that can be used for further processing and analysis. This often involves loading data into a database system, such as MySQL or PostgreSQL.
* **Cleaning and transforming** the data often involves removing invalid records and translating all the columns to use a sane set of values. You may also combine two different datasets into a single table, remove duplicate entries or apply any number of other normalizations. As you acquire data, you will notice that such data often has many inconsistencies: names are used inconsistently, amounts will be stated in badly formatted numbers, while some data may not be usable at all due to file corruptions. In short: data always needs to be cleaned and processed. In fact, processing, augmenting and cleaning the data is very likely to be the most time- and labour-intensive aspect of your project.
* **Analysis of data** to answer particular questions we will not describe in detail in the following chapters of this book. We presume that you are already the experts in working with your data and using e.g. economic models to answer your questions. The aspects of analysis which we do hope to cover here are automated and large-scale analysis, showing tips and tricks for getting and using data, and having a machine do a lot of the work, for example: network analysis or natural language processing.
* **Presentation of data** only has impact when it is packaged in an appropriate way for the audiences it needs to aim at.

As you model a data pipeline, it is important to take care that each step is well documented, granular and - if at all possible - automated. 

We will also cover best practice guidelines for data projects - which may not fit into any particular categories, but are very important parts of any data work! 


#################
Table of Contents
#################
.. toctree::
   :maxdepth: 2

   courses/index.rst
   recipes/index.rst
   appendix/index.rst

