Spreadsheet
***********
.. sectionauthor:: Michael Bauer (@mihi_tr on twitter)

.. figure:: http://farm9.staticflickr.com/8435/7851115132_509518d076_o_d.jpg
    :align: right
    :alt: a sample spreadsheet
    :width: 400

    A sample spreadsheet

Spreadsheets are the most basic tools of handling data. They are simple to
use, yet with experience they become powerful. You can collect, wrangle,
analyze and visualize data with a good spreadsheet program. The only
downside to them is: they are not good at handling relational data and
data sets that become too large. The big advantage is: learning how
to use them is simple. Not surprisingly spreadsheet applications are common
and widely used. The most well known is probably Microsoft's Excel (from the
Office package). However there is a large number of spreadsheet programs
available.

Google Docs
===========

You do not need to purchase or download programs to your computer to use
spreadsheets: `Google docs`_ offer a spreadsheet application. It is quite
commonly used when collaborating online, since data can be shared and
edited collaboratively. Google docs also offers interesting features, such
as integration of Google search into the spreadsheet. 

Getting Started
---------------

The Knight Digital Media Center has an `extensive tutorial on Google docs spreadsheets`_.
This is a solid introduction to spreadsheets. If you want to
try what you just learned or get a more interactive introduction try the
`School of Data basic data wrangling challenge`_. 

Sorting Data
------------

One thing you frequently want to do with your spreadsheet is sorting data.
If you don't know how, don't worry, we'll walk you through.

.. figure:: http://farm8.staticflickr.com/7252/7851175836_d6f6722234_o_d.jpg
    :alt: making a copy of a google-doc spreadsheet
    :align: center
    
    Making a copy of a google doc spreadsheet

First grab our `sample spreadsheet`_ and copy it. Do this by clicking the
"File" menu and "Make a copy". This will result in a new spreadsheet, this
is your personal copy you can edit and play around with. Don't worry: you
can't break anything. If you get stuck or mess the spreadsheet up: just
make a new copy. 

.. _`sample spreadsheet`: https://docs.google.com/spreadsheet/ccc?key=0AlgwwPNEvkP7dGxzQzBVYV91Z09ITjJFRzRVTE5UWEE

.. figure:: http://farm8.staticflickr.com/7255/7851114342_4b1d4390c7_o_d.jpg
    :alt: selecting all the data cells
    :align: center

    Selecting the data cells

Next you want to mark the data you want to sort. We want to sort the whole
sheet by names. Click on the top left cell (A1) and simply drag to the
bottom right cell. The selected cells should be marked in blue as shown on
the screenshot on the right. You can alternately click on the grey
rectangle at the upper left corner where the column and row names are: this
will select the whole sheet for you.

.. figure:: http://farm9.staticflickr.com/8424/7851114060_b3c3ed9d69_o_d.jpg
    :alt: Sorting a dataset
    :align: center

    Sorting a dataset

To sort a dataset, open the "data" menu and select "Sort range...". This
will open a Popup

.. figure:: http://farm9.staticflickr.com/8303/7851114206_97a5b15a69_o_d.jpg
    :alt: Sort options
    :align: center

    Sort options

The popup will present several sort options to you. Make sure that if your
selection contains title rows check the box named "Data has header row".
This will allow you to select the column you want to sort with by title. If
you click on "Sort" the popup will be closed and your data sorted. Pay
attention to always mark the complete dataset: otherwise just the selected
columns will be sorted - this might not be what you want to acheive.

Filtering Data
--------------

Filtering data is another important function of spreadsheets. Let's say in
our `sample spreadsheet`_ we only want to see what Eve did. Of course this
is easy if our spreadsheet is as small as this one - but filtering will be
really powerful if you have larger datasets.

.. figure:: http://farm9.staticflickr.com/8290/7851113938_0b01ae057a_o_d.jpg
    :alt: Filtering a dataset
    :align: center

    Filtering a dataset

First select all the datacells as mentioned above. Then select "Filter"
from the "data" menu. This will slightly change the first row of your
dataset: notice the small triangles in the cells? These are the filter
options.

.. figure:: http://farm9.staticflickr.com/8287/7851268800_84740415d4_o_d.jpg
    :alt: Filter options
    :align: center

    Filter options

The filter options allow you to select which data rows to show. In our
examle you see green tickmarks next to all three names: this means: show
all three names. Just click on a name and the tickmark will disappear. Note
how the table view changes. Don't worry this will not delete any data -
it's just hiding it. Play around with filtering until you feel confortable. 

Pivot Tables
------------

Pivot tables are summary tables produced from your data. These kind of
summary tables are so frequent that some spreadsheet software has
specialized functions for building them from your data. You'll probably
create some sort of summary in the future - so let's look at them.

.. figure:: http://farm9.staticflickr.com/8292/7851114476_f3b595da5f_o_d.jpg
    :alt: Creating a Pivot Table
    :align: center
    
    Creating a pivot table

To create a pivot table select the data as described above. Then choose the
option "Pivot table report..." from the "data" menu. This will
automatically create a new sheet with a pivot table. You can switch back to
your original data sheet by selecting the sheet in the tabs on the bottom. 

.. figure:: http://farm8.staticflickr.com/7128/7851114580_e7826e81c7_o_d.jpg
    :alt: Creating the Pivot report - selecting rows
    :align: center

    Creating the pivot report - selecting row information

Now let's create our pivot report. Go to the pivot table sheet and look to
the right. You should have a "Report Editor". If you do not see the Editor
click somewhere within the marked area, it should appear. Since the
spreadsheet does not know how you want to summarize your data, you'll need
to provide this information. First: what categories do you want for your
rows. In our example let's say we want to know the names of the person: so
let's select "Who". 

.. figure:: http://farm9.staticflickr.com/8444/7851114688_50db378d32_o_d.jpg
    :alt: Creating the pivot report - selecting colums
    :align: center

    Creating the pivot report - selecting columns

Next on are the columns: Let's select "What" for columns, since we want to
know who did what.

.. figure:: http://farm9.staticflickr.com/8297/7851114830_bcdab54720_o_d.jpg
    :alt: Creating the pivot report - selecting values
    :align: center
    
    Creating the pivot report - selecting values

And the last step is to tell our report editor which values to report on.
Let's select "Hours". This will result in a pivot report similar to the one
below:

.. figure:: http://farm9.staticflickr.com/8287/7851114972_0e878a0ce5_o_d.jpg
    :alt: the completed pivot report
    :align: center

    The completed pivot report

You can see how our selections in the report changed the pivot report
created. Now go back and edit the data - the pivot report will
automatically change. You can play around with the options in the report
editor until you feel confortable with creating and manipulating pivot
reports. Remember: You can't break anything.

Reference
---------
* `Google Docs Spreadsheet function list`_
* `Google Docs keyboard shortcuts`_
* `Google Docs Spreadsheet help`_
* `Pivot tables in Google Spreadsheet`_ (video)

.. _Knight Digital Media Center: http://multimedia.journalism.berkeley.edu/
.. _extensive tutorial on Google docs spreadsheet: http://multimedia.journalism.berkeley.edu/tutorials/spreadsheets/
.. _school of data basic data wrangling challenge: https://p2pu.org/en/groups/data-cleaning-and-basic-spreadsheet-skills/
.. _Google Docs Spreadsheet function list: https://support.google.com/docs/bin/static.py?hl=en&topic=25273&page=table.cs
.. _Google docs: http://docs.google.com
.. _Google Docs keyboard shortcuts: http://support.google.com/docs/bin/answer.py?hl=en&answer=181110
.. _Google Docs Spreadsheet help: http://support.google.com/docs/bin/topic.py?hl=en&topic=1360901&parent=1360868&ctx=topic
.. _Pivot tables in Google Spreadsheet: http://www.youtube.com/watch?feature=player_embedded&v=giuD7KSmock



..
    Excel
    =====
    
    Open/Libre Office
    =================
