=======================================
Welcome to the Data Wrangling Handbook!
=======================================

The Data Wrangling Handbook is a companion text to the `School of Data`_. Its
function is something like a traditional textbook - it will provide the detail
and background theory to support the School of Data courses and challenges.

The Data Wrangling Handbook is currently in an early stage of development. Over
the coming months we intend to write more chapters and flesh out this skeleton
with content and detail. We also hope to expand and improve upon this basic
outline, so if there's a section that you currently feel is missing, please do
let us know!

The Data Wrangling Handbook is a collaborative endeavour, and we welcome all
feedback and contributions. To contribute to the Data Wrangling Handbook you
can:

* Edit directly on the `Data Wrangling Github Repository`_
* Submit an issue to our `issue tracker`_
* Write a new contribution - you can do this in the format and editor of your choice (Google Docs, Open Office, Word, Latex ...) and then email it to schoolofdata [@] okfn.org
* Email us ideas and suggestions at schoolofdata [@] okfn.org 
* Send tweets to `@SchoolOfData`_

The Data Wrangling Handbook should be accessible to all learners. If you
stumble across an unexplained term or a concept that requires more explanation,
please do get in touch.

.. _School of Data: http://schoolofdata.org/
.. _Data Wrangling Github Repository: https://github.com/okfn/datawrangling
.. _@SchoolOfData: http://twitter.com/SchoolOfData
.. _issue tracker: https://github.com/okfn/datawrangling/issues

.. toctree::
   :maxdepth: 4

   part1/index.rst

  
=======================================
Part II: The Data Pipeline
=======================================

(Make sure to discuss keeping a data notebook throughout this process.)

Finding Data
---------------------

.. toctree::
   :maxdepth: 3

* Data Sources
   
  * Online - a curated list of "trustworthy" sources by category - not guaranteed - see Data Quality
      
    * government
    * science
    * social science
    * literature
    * sports
    * art
    * etc
   
  * Online - APIs
      
    * introduce the idea
    * examples

  * Online - Scraping

    * introduce the idea
    * examples

  * Crowdsourcing

    * manual / bulk digitization

  * Offline
      
    * interviews, ethnography, government docs, library collections, more??

* Wrangling

  * Extraction
   
    * selection, download
    * scraping & parsing in detail

  * Cleaning

    * The Table - Rows and Columns
    * Unicode & Special Characters
    * missing values
    * granularity
    * uniqueness
    * duplicates
    * manual correction
    * more.....

  * Transforming

    * Normalization
    * more.....

  * Merging

    * SUPER IMPORTANT

  * Storing & Publishing
  
    * datahub
    * online
    * bulk vs. structured

* Analysis

  * Investigating the Shape of Data - The Basics
  
    * count
    * min, max, range
    * mean, median, mode
    * quartiles
    * outliers
    * variance, standard deviation
    * histogram
    * scatterplots

  * Simple Statistical Techniques

    * filtering
    * pivoting
    * plotting 
    * regression
    * more???

  * Advanced Statistical Techniques

    * Data Mining Techniques
    * more????

* Communicating Data

  * "Story"

  * Visualization

   ref/visualization



  * Mapping

  * Watch Out!!! Common Misinterpretations of Data


=======================================================
Part III: Case Studies
=======================================================

.. toctree::
   :maxdepth: 2

   part3/weather-data


=======================================================
Part IV: The "Secrets" - Tips & Tricks of the Trade
=======================================================

This is always the best part, right??? :-)

Recipes
---------------------

.. toctree::
   :maxdepth: 2

   part4/recipes/liberating-html-tables
   part4/recipes/liberating-access-databases
   part4/recipes/archiving-twitter
  

Tips
---------------------

.. toctree::
   :maxdepth: 1

* tips??


=====================================================
Appendix
=====================================================

.. toctree::
    :maxdepth: 2
    
    glossary








======================================================
OLDER OUTLINE, to be incorporated into above outline:
======================================================

.. toctree::
   :maxdepth: 2

   csv
   workingenv

* SQL, JSON, CSV ...
* Types of Data

  * Web
  * Text
  * Structured Documents
  * Databases
  * Scientific Data

* Programming Basics
* Advanced Programming

How to find stuff! (aka Discovery and Acquisition)
--------------------------------------------------

.. toctree::
   :maxdepth: 2
  
   howtogetdata

* Searching and Finding
* Crowd Sourcing

  * Manual Digitisation
  * Bulk Digitsation

Extraction
----------

.. toctree::
   :maxdepth: 2
  
   scraping
   liberating-html-tables

* Scraping and Parsing
* Automation
* Natural Language Processing
* Data Pipes
* OCR
* Other potential sections? Regexen / PDF / OCR/ocropus / Refine / Refine as a Server / Text Normalization / Calais and Auto-Tagging

Cleaning, Transforming & Integrating
------------------------------------

.. toctree::
   :maxdepth: 2
  
   geocoding
   datahub
   ref/visualization

* Data Formats and Standards
* Data Granularity
* Using Refernce Data
* Merge / Join
* Mapping
* Handling Manual Corrections
* Normalisation
* Entity Uniqueness
* Treating Duplicates
* Indexing and Optimisation
* Handling Changing Dimensions
* Concept Modelling
* Fuzzy Matching

Storing and publishing data
---------------------------

.. toctree::
   :maxdepth: 2
  
   datahub

* Publishing Online
* Bulk storage versus structured storage

Analysis
--------

* Visualisation and Plotting
* Sorting, Filtering and Pivoting
* Regression
* Visualisation Method Selection - list of tools in DWH
* Map Geo-Tagging - short section in DWH
* Other potential sections: NetworkX / graphviz + Gephi / Mapping / Dataviz (invite)

Presentation
------------

.. toctree::
   :maxdepth: 2
  
   ref/visualization

* Viz
* Mapping ...

.. _data quality outline: https://docs.google.com/document/d/13IkiZfd3OR7PxPED58Cw3giB3HMjHprayODoVCseOow/edit
.. _databases outline: https://docs.google.com/document/d/1TrCuVla9cSdaWx8_vzeuS_gGQDYIuewRXJOq9cXFFf4/edit
