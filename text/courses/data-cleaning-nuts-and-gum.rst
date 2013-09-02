Section 1: Nuts and chewing gum
================================
Introduction
------------

Some things just don't go together. These things include a stuffed toy puppy and an electric light, or nuts and chewing gum:

.. figure:: http://farm9.staticflickr.com/8516/8401143241_924a729397_n_d.jpg

  Novelty lamp, Albania, 2011. Photo: Tom Longley. Yes, the lampshade is
  mounted on the puppy’s head. Image License: some rights reserved
  CC-BY-SA.

.. figure:: http://farm9.staticflickr.com/8237/8402232902_ec862773eb_n_d.jpg

  'Nuts and Gum'. From The Simpsons Series 5, Episode 14: Lisa vs. Malibu Stacy, 1994. View clip: http://vimeo.com/9372862 Copyright: FOX. Reproduced under Fair Use.


In spreadsheets, formatting and data don't go together.  Behold the consequences of spreadsheet formatting:

.. image:: http://farm9.staticflickr.com/8503/8401143543_a8a9b1bb41_c_d.jpg    

You’ve probably received something as aesthetically abhorrent as the above. Creators of spreadsheets spend a lot of time formatting data in ways that they find useful to them. They change the text size, colour in the cells, introduce borders and lines to give emphasis to the things they are interested in. However, these may not be useful to you as a receiver of that data, and may get in the way of your ability to use the data. 


By the end of this section, you’ll have gained the following: 

* practical knowledge of common formatting and layout features of spreadsheets.
* the skills to transform data other people give from a stuffed toy puppy lamp to something less distracting.
* some ideas about how to present your raw data to others so they will love you!

Some work
---------

To do both the quick and longer tasks below you’ll need:

* a spreadsheet tool, such as Excel or Libre Office.
* a copy of the course dataset, which is GRAIN’s data on “land grabbing”  (available `here`_).

.. _here: http://datahub.io/dataset/grain-landgrab-data/resource/af57b7b2-f4e7-4942-88d3-83912865d116

A quick task (15-30 minutes)
____________________________

Ready to make a mess? Let’s try and get into the minds of people who make spreadsheets as ugly as a stuffed toy puppy lamp. 


In his excellent essay “The Art of Spreadsheets” John Raffensperger lists
`37 ways that you can hide data in a spreadsheet`_. Here are 10 of them:

.. _37 ways that you can hide data in a spreadsheet: http://john.raffensperger.org/ArtOfTheSpreadsheet/Chapter09_ShowAllTheInformation.html


* Do not share the file. This is the most common way of hiding information, and the most effective.
* Hide the sheet. You need at least two sheets first, then: Format, Sheet, Hide.
* Hide the row: Format, Row, Hide.
* Hide the column: Format, Column, Hide.
* Hide the cell and protect the sheet: Format, Cells, Protection, Hidden, then Tools, Protection. This shows a display, but hides the formula: =if(1, “Peace!”, “Attack at dawn.”).
* Make the column too narrow: Format, Column, Width, 0.
* For formulas that are likely to be zero, use Tools, Options, View, and clear the Zero values box. For example: =IF(1, 0, “Attack at dawn.”).
* Use a formula that returns a blank: =IF(1, “ ”, “Attack at dawn.”).
* Create a complicated formula that displays the information, but format it as text (with Format, Cells, Number, Text, or just start the cell with a single quotation mark), so the formula is displayed rather than the output.
* Format the font with Wingdings: Format, Cells, Font, Wingdings. This displays unintelligible characters.


Using John Raffensperger's list as inspiration, your task is to mess up the GRAIN data as much as  possible.  Marks will be awarded for:

* making the presentation just bad enough that someone using the data might be tempted to think they can still use it!
* the use of colour and font effects in ways that really offend the eye
* ingenuity in hiding bits of data in plain sight.


When you’re finished making a mess, consider how you would undo it and persuade others not to treat their data in this way.


A longer task (30-60 minutes)
_____________________________

* From the Data Wrangling Handbook Recipe on Data Cleaning, run through Problem 1: `Showing the data plainly using the GRAIN data`_. This shows you how to remove formatting quickly. It is the first part of a longer ‘recipe’ on data cleaning.        

.. _Showing the data plainly using the GRAIN data: http://schoolofdata.org/handbook/recipes/cleaning-data-with-spreadsheets/#problem-1-showing-the-data-plainly

Reading list
------------

#. The help documentation for the most common spreadsheet tools outlines the different ways that you can change the way that a spreadsheet displays data. Depending on which spreadsheet you're using, visit these sites to refresh your memory: `Libre Office - Formatting`_, `Excel - Apply Cell Style`_, `Google Docs - Cell Style`_
#. “The Art of Spreadsheets” by John Raffensperger has a list of `37 ways to hide information in spreadsheets`_.
#. Spreadsheet legend Chandoo looks at how to `Boss proof your spreadsheets`_.
#. The nuclear option: how to remove all formatting from a spreadsheet (`LibreOffice`_)

.. _Libre Office - Formatting: https://help.libreoffice.org/Calc/Format
.. _Excel - Apply Cell Style: http://office.microsoft.com/en-us/excel-help/apply-create-or-remove-a-cell-style-HP001216732.aspx

.. _Google Docs - Cell Style: http://support.google.com/drive/bin/answer.py?hl=en&answer=46973
.. _37 ways to hide information in spreadsheets: http://john.raffensperger.org/ArtOfTheSpreadsheet/Chapter09_ShowAllTheInformation.html

.. _Boss proof your spreadsheets: http://chandoo.org/wp/2009/11/03/make-better-excel-sheets/
.. _LibreOffice: https://help.libreoffice.org/Common/Undoing_Direct_Formatting_for_a_Document#Removing_all_Direct_Formatting_in_a_LibreOffice_Calc_Spreadsheet

Rest and reflect
----------------
Well, you must now be exhausted, so let’s pause a little and consider what we’ve been doing. Here are a few questions to get you started:

#. Are there times when formatting is useful? 
#. What are the downsides of removing formatting from a spreadsheet?
#. How should we visually display data in the tools that we work with every day?


Talk about it in the comments threads if you like. 


And now hurry on to the next instalment of this course, The Invisible Man is in your spreadsheet, messing with your data.


.. raw:: html

    <iframe src="http://okfnlabs.org/scodaquiz/howyoufeel.html#nuts-and-gum"
      width="510" height="310" frameborder="0"></iframe>

.. raw:: html
  
  <a href="../data-cleaning-invisible-man-in-spreadsheets/" class="btn btn-primary btn-large">Next Course <span
  class="icon-arrow-right"></span></a>


This course was created for the School of Data by `Tactical Technology
Collective`_. Tactical Tech is an international NGO working at the point where rights advocacy meets information and technology.

.. _Tactical Technology Collective: http://tacticaltech.org


.. raw:: html

  <div class="alert alert-info">Any questions? Got stuck? <a class="btn
  btn-large btn-info" href="http://ask.schoolofdata.org">Ask School of Data!
  </a></div>
