Section 2: the Invisible Man is in your spreadsheet, messing with your data
===========================================================================
Introduction
------------

There’s something creepy going on in your spreadsheet, and it’s not nice. 

.. figure:: http://farm9.staticflickr.com/8092/8402327514_10a8f622fd_n_d.jpg

   Illustration 1: The Invisible Man movie poster, 1933. Image source. Reproduced under Fair Use.

“Even the moon is frightened of me”, shrieks the Invisible Man, otherwise
known as Dr Griffen, a genius driven mad after experimenting on himself! If
you have the time, watch the short `trailer for the 1933 film`_. Creepy things start happening to people in a small town: mysterious footsteps in the snow, household objects seemingly flying through the air, people being pushed down stairs (and over cliffs!). And in our case: messing with our spreadsheet. 

.. _trailer for the 1933 film: http://www.youtube.com/watch?v=pb3n0g2NenI


We can’t see The Invisible Man himself (obviously, or he wouldn’t be invisible). But we can find traces of his work in our spreadsheet, as we can see his footsteps in the snow:

.. image:: http://farm9.staticflickr.com/8086/8402327534_fb1e33e0a7_o_d.png


One error he inserted you can clearly see, but the others are far harder to spot with the naked eye:

* Added extra white spaces at the ends of entries.
* Tabs that are inserted at the ends of lines
* Line breaks and 'carriage returns', which you insert by pressing enter (or Ctrl-Enter).

They’re called “non-printable” characters, and aren’t displayed all the time in spreadsheets. But you will still feel their sinister presence as they seriously affect data analysis. This is because spreadsheets treat these sorts of characters as real data. Ignoring the column label, in the data above you can see four terms that are essentially the same. The spreadsheet, however, sees four different, distinct pieces of data. If you were trying to count how many times “Your Data” was mentioned, a spreadsheet would only show a single entry. 

In the film, the police set up traps to catch the invisible man. We can do the same in our spreadsheets. By the end of this section you should have:

* some knowledge about how non-printable characters cause errors in data
* tried out different functions and features of the spreadsheet that will remove them

Some work
---------
To do both the quick and longer tasks below you’ll need:

#. A spreadsheet tool, such as Excel or Libre Office.
#. A copy of the `sample spreadsheet`_ for this section.
#. A copy of the course dataset, which is GRAIN’s data on “`land grabbing`_”.

.. _sample spreadsheet: http://datahub.io/dataset/theinvisibleman

.. _land grabbing: http://datahub.io/dataset/grain-landgrab-data

A quick task (15 minutes)
_________________________

* Download and open this `sample spreadsheet`_ on your computer. In column A is the data from above, with different sorts of non-printable characters. In columns B-E are four easy methods of removing non-printable characters from your data using:
  * the TRIM function (in column B)
  * the CLEAN function (in column C)
  * the TRIM and CLEAN functions …. together! (in column D)
  * the “Paste Special” feature (in column E)
* Apply an “AutoFilter” to the data (Data → Filter → AutoFilter). Click on the little downwards-pointing arrows and a selection list will pop up displaying the number of distinct entries in each column. If you click on the autofilter for each of columns A through to E you can see the effect of the different methods of removing non-printable characters. 
* Double click on cells to view the formulas see how the functions work in practice. There is more information on each of them in the 'Study' section below.
* Now try it yourself. Create or find a single column of data on your own. Apply these four methods in the same format as our sample the your spreadsheet. 


Use the discussion area below to share your work and any observations about this task.


A longer task (30-60 minutes)
_____________________________

From the Data Wrangling Handbook Recipe on Data Cleaning, run through
Problem 2: `Whitespace and new lines - data that shouldn’t be there`_ using the GRAIN dataset. This goes into more detail about the CLEAN and TRIM functions.

.. _Whitespace and new lines - data that shouldn’t be there: http://schoolofdata.org/handbook/recipes/cleaning-data-with-spreadsheets/#problem-2-whitespace-and-new-lines-data-that-shouldnt-be-there

Reading list
------------

* Watch  this useful YouTube video from `Excel is Fun`_ about using CLEAN and TRIM. 
* Read Microsoft's surprisingly helpful help page on removing extra spaces and non-printable characters, `here <http://office.microsoft.com/en-us/excel-help/top-ten-ways-to-clean-your-data-HA010221840.aspx#BMremoving_spaces_and_nonprinting_chara>`_. Much of this will work in LibreOffice and Google Spreadsheets, though there are differences. Cast your eye over the Function documentation: TRIM (Excel, `LibreOffice <https://help.libreoffice.org/Calc/Text_Functions#TRIM>`_, Google Docs) and CLEAN (Excel, `LibreOffice <https://help.libreoffice.org/Calc/Text_Functions#CLEAN>`_, Google Docs).         
* Read the Feature documentation: Paste Special (Excel, `LibreOffice <https://help.libreoffice.org/Common/Paste_Special>`_, Google Docs), Autofilter (Excel, `LibreOffice <https://help.libreoffice.org/Calc/Applying_AutoFilter>`_, Google Docs)        
* For advanced Invisible Man hunters you can read up about using regular  expressions in LibreOffice, `here <http://www.oooninja.com/2007/12/example-regular-expressions-for-writer.html>`_. We also cover this in the longer task above, but it's not straightforward.

.. _Excel is Fun: http://www.youtube.com/watch?v=o-dBCS2wgO4&feature=plcp


Rest and reflect
----------------

The Invisible Man can appear at any time, so we must be vigilant. 

* How does white space get into your data?
* Can you think of other ways to approach the problem? 


Post your thoughts in the discussion area.


Then get moving to the third section in this course on data cleaning, called “Your data is a witch’s brew”.


.. raw:: html
  
    <a href="../data-cleaning-witchs-brew/" class="btn
    btn-primary btn-large">Next Course <span
      class="icon-arrow-right"></span></a>



This course was created for the School of Data by `Tactical Technology
Collective`_. Tactical Tech is an international NGO working at the point where rights advocacy meets information and technology.

.. _Tactical Technology Collective: http://tacticaltech.org

