Sort and Filter: The basics of spreadsheets
===========================================

Introduction
------------
In this tutorial, we will look at the basics of spreadsheets. Spreadsheets are a powerful tool for a Data Wrangler. Data contained in a spreadsheet is in a structured, machine-readable format. You can quickly begin to process data once it is in a spreadsheet - whether by sorting and filtering, carrying out simple sums (finding the total, the average etc.), applying bulk processes, or pulling out different graphs and charts.


By the end of the module, you will have learned how to download data, how to import it into a spreadsheet, and how to begin cleaning and interpreting it using the ‘sort’ and ‘filter’ functions.




Spreadsheets: An Overview
-------------------------

Data wranglers use a range of software to work with data. Data varies in its extent and complexity - and depending on the nature of the data, we need different approaches and tools to process it. In the beginning, we will focus on data which can be handled quite easily. As you progress, we will look at more powerful ways of handling data.

The most basic tool used for data wrangling is a spreadsheet. Nowadays spreadsheets are widespread so a lot of processes involve them. You may well be familiar with them already. A variety of spreadsheet programs and applications exist. For example Microsoft's Office package comes with Excel, the OpenOffice package comes with Calc and so on. Not surprisingly, Google decided to add spreadsheets to their documents package. Since it does not require you to purchase or install any additional software, we will be using Google Spreadsheets for this course.

Depending on what you want to do you might consider using different spreadsheet software:

=====================  ======================  ============================  ============================
Spreadsheet            Google Spreadsheets     Open(Libre)Office             Microsoft Excel
=====================  ======================  ============================  ============================
Usage                  Free (as in Beer)       Free (as in Freedom)          Commercial
Data Storage           Google Drive            your harddisk                 your harddisk
Needs Internet         Yes                     No                            No
Installation required  No                      Yes                           Yes
Collaboration          Yes                     No                            No
Sharing results         Easy                    Harder                        Harder
Visualizations         Large range             Basic                         Basic
=====================  ======================  ============================  ============================

Creating a spreadsheet and uploading data
-----------------------------------------
In this course we will use Google docs for our data-wrangling - it allows you to start right away without need of installing software. Since the data we are working with is already public we also don’t need to worry about the fact that it is not stored on our local drive.

**Walktrough:** Creating a Spreadsheet and uploading data.

#. Head over to Google docs.
#. If you are not yet logged in to Google docs, you need to login.
#. The first step is going to be creating a new spreadsheet.
#. Do this by clicking the ``create`` button to the left and select spreadsheet.

   .. image:: http://farm9.staticflickr.com/8448/7871786616_ef5892fe33_o_d.jpg
#. Doing so will create a new spreadsheet for you.
#. let’s upload some data.
#. You will need the file we downloaded from the worldbank in the last tutorial. If you haven’t done the
   tutorial or lost the file: download it `here`_
#. In your spreadsheet select ``import`` from the ``file`` menu. This will open a dialog for you.
#. Select the file you downloaded.
#. Don’t forget to select ``insert new sheets``, and click ``import``

   .. image:: http://farm9.staticflickr.com/8306/7872679284_c321614681_b_d.jpg


.. _here: http://dump.tentacleriot.eu/wb-gdp-health-life.csv

Navigating and using the Spreadsheet
------------------------------------
Now we loaded some data let’s deal with the basics of spreadsheets. A spreadsheet is basically a table of “cells” in which you can input data. The cells are organized in “rows” and “columns”. Typically rows are labeled by numbers, columns by letters. This also means cells can be addressed by their “column” and “row” coordinates. The cell A1 denotes the cell in the first row in the first column, A2 the one in the second row, B1 the one in the second column and so on.

To enter or change data in a cell click on it and start typing - this will change the contents of the cell. Basic navigation can be done this way or via keyboard. Find a list of keyboard shortcuts good to know below:

======================  ============================================================================
Key or Combination      What it does
======================  ============================================================================
Tab                     End input on the current cell and jump to the cell right to the current one
Enter                   End input and jump to the next row (This will try to be intelligent, so if 
                        you're entering multiple columns, it will jump to the first column you are 
                        entering
Up                      Move to the cell one row up
Down                    Move to the cell one row down
Left                    Move to the cell left
Right                   Move to the cell on the Right
Ctrl+<direction>        Move to the outermost cell in the direction given
Shift+<direction>       Select the current cell and the cell in <direction>
Ctrl+Shift+<direction>  Select all cells from the current to the outermost cell in <direction>
Ctrl+c                  Copy – copies the selected cells into the clipboard
Ctrl+v                  Paste – pastes the clipboard
Ctrl+x                  Cut – copies the selected cells into the clipboard and removes them from 
                        their original position
Ctrl+z                  Undo – undoes the last change you made
Ctrl+y                  Redo – undoes an undo
======================  ============================================================================
	
**Tip:** Practice a bit, and you will find that you will become a lot faster using the keyboard than the mouse!

Locking Rows and Columns
------------------------
The spreadsheet we are working on is quite large. You will notice, that while scrolling the column with the column labels will frequently disappear, leaving you quite lost. The same with the country names. To avoid this you can “lock” rows and columns so they don't disappear.


**Walkthrough:** Locking the top row

#. Go to the Spreadsheet with our data and scroll to the top
#. On the top left, where the column and row labels are you'll see a small striped area
   
   .. image:: http://farm9.staticflickr.com/8322/8070104022_e233a65687_o_d.png
#. Take the one facing the row labels and drag it one row down
#. Your result should look like this: 
   
   .. image:: http://farm9.staticflickr.com/8176/8070115059_d960b3d09e_o_d.png
#. Try scrolling – notice how the top row remains fixed?

Sorting Data
------------
The first thing to do when looking at a new dataset is to orient yourself. This involves at looking at maximum/minimum values and sorting the data so it makes sense. Let's look at the columns. We have data about the GDP, healthcare expenditure and life expectancy. Now let's explore the range of data by simply sorting.

**Walkthrough:** Sorting a dataset.

#. Select the whole sheet you want to sort. Do this by clicking on the right upper gray field, between the row and column names.
   
   .. image:: http://farm9.staticflickr.com/8322/8070104022_e233a65687_o_d.png 
#. Select “Sort Range...” from the “Data” menu – this will open an additional Selection
#. Check the “Data has header row” checkbox
   
   .. image:: http://farm9.staticflickr.com/8437/7872826062_017d1bfe19_o_d.jpg
#. Select the column you want to sort by in the dropdown menu
#. Try to sort by GDP – Which country has the lowest?
#. Try again with different values, can you sort ascending and descending?


**Tip:** Be careful! A common mistake is to forget to select *all* the data. If you sort without selecting all the data, the rows will no longer match up.

Filtering Data
--------------
The next thing commonly done with datasets is to filter out the values you don't want to see. Did you notice that some “Country Names” are actually not countries? You'll find things like “World”, “North America” and “Arab World”. Let's filter them out.


**Walkthrough:** Filtering Data

#. Select the whole table.
#. Select “Filter” from the “Data” menu.
#. You now should see triangles next to the column names in the first row.
#. Click on the triangle next to country name.
#. you should see a long list of country names in the box. 

   .. image:: http://farm9.staticflickr.com/8316/8070573150_2cf29b914f_o_d.png
#. Find those that are not a country and click on them (the green check mark will disappear).
#. Now you have successfully filtered your dataset.
#. Go ahead and play with it - the data will not be deleted, it’s just not displayed.

Summary
-------
In this module we talked about basic spreadsheet skills. We talked about
data entry and how to sort and filter data using a spreadsheet program. In
the `next course`_ we will talk about data analysis and introduce you to formulas.

Further Reading and References
------------------------------
#. The School of Data Handbook on `spreadsheets`_.
#. `Google help`_ on spreadsheets

.. _spreadsheets: http://schoolofdata.org/handbook/tools/spreadsheet/
.. _Google help: http://support.google.com/drive/bin/topic.py?hl=en&topic=2811806&parent=2811739&ctx=topi
.. _next course: http://schoolofdata.org/handbook/course/analyzing-data/

Quiz
----
Check your sorting and filtering skills with the following quiz.

.. raw:: html
   
         <iframe src="https://testmoz.com/109521" width="100%" height="750"
         frameborder="0" marginheight="0"
         marginwidth="0">Loading...</iframe><br/><br/>

.. raw:: html 
 
   <a href="../analyzing-data/" class="btn btn-primary btn-large">Next 
     Course<span class="icon-arrow-right"></span></a> 


