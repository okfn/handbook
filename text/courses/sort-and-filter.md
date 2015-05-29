Sort and Filter: The basics of spreadsheets
===========================================

Introduction
------------

The most basic tool used for data wrangling is a spreadsheet. Data contained in a spreadsheet is in a structured, machine-readable format and hence can quickly be sorted and filtered. In other recipes in the handbook, you'll learn how to use the humble spreadsheet as a power tool for carrying out simple sums (finding the total, the average etc.), applying bulk processes, or pulling out different graphs and charts.

By the end of the module, you will have learned how to download data, how to import it into a spreadsheet, and how to begin cleaning and interpreting it using the ‘sort’ and ‘filter’ functions.

Spreadsheets: An Overview
-------------------------

Nowadays spreadsheets are widespread so a lot of people are familiar with them already. A variety of spreadsheet programs and applications exist. For example Microsoft's Office package comes with Excel, the OpenOffice package comes with Calc and so on. Not surprisingly, Google decided to add spreadsheets to their documents package. Since it does not require you to purchase or install any additional software, we will be using Google Spreadsheets for this course.

Depending on what you want to do you might consider using different spreadsheet software. Here are some of the considerations you might make when picking your weapon of choice:

  | Spreadsheet            |  Google Spreadsheets  | Open(Libre)Office      | Microsoft Excel
  |----------------------- | --------------------- | ---------------------- | -----------------
  | Usage                  | Free (as in Beer)     | Free (as in Freedom)   | Commercial
  | Data Storage           | Google Drive          | Your hard disk         | Your hard disk
  | Needs Internet         | Yes                   | No                     |No
  | Installation required  | No                    | Yes                    | Yes
  | Collaboration          | Yes                   | No                     | No
  | Sharing results        | Easy                  | Harder                 | Harder
  | Visualizations         | Large range           | Basic charts           | Basic charts

Creating a spreadsheet and uploading data
-----------------------------------------

In this course we will use Google docs for our data-wrangling - it allows you to start right away without need of installing software.
Since the data we are working with is already public we also don’t need to worry about the fact that it is not stored on our local drive.

### Walktrough: Creating a Spreadsheet and uploading data.

1.  Head over to Google docs.
2.  If you are not yet logged in to Google docs, you need to login.
3.  The first step is going to be creating a new spreadsheet.
4.  Do this by clicking the `create` button to the left and select spreadsheet.

    ![image](http://farm9.staticflickr.com/8448/7871786616_ef5892fe33_o_d.jpg)

5.  Doing so will create a new spreadsheet for you.
6.  Let’s upload some data.
7.  You will need the file we downloaded from the World Bank in the last tutorial. If you haven’t done the tutorial or lost the file: download it [here](http://dump.tentacleriot.eu/wb-gdp-health-life.csv).
8.  In your spreadsheet select `import` from the `file` menu. This will open a dialog for you.
9.  Select the file you downloaded.
10. Don’t forget to select `insert new sheets`, and click `import`
    ![image](http://farm9.staticflickr.com/8306/7872679284_c321614681_b_d.jpg)

Navigating and using the Spreadsheet
------------------------------------

Now we loaded some data let’s deal with the basics of spreadsheets. A spreadsheet is basically a table of “cells” in which you can input data.
The cells are organized in “rows” and “columns”. Typically rows are labeled by numbers, columns by letters. This also means cells can be addressed by their “column” and “row” coordinates. The cell A1 denotes the cell in the first row in the first column, A2 the one in the second row, B1 the one in the second column and so on.

To enter or change data in a cell click on it and start typing - this will change the contents of the cell. Basic navigation can be done this way or via keyboard. Find a list of keyboard shortcuts good to know below:

  | Key or Combination         | What it does |
  | -------------------------- | -------------------------------------------------------------------- |
  | `Tab`                        | End input on the current cell and jump to the cell right to the current one |
  | `Enter`                      | End input and jump to the next row (This will try to be intelligent, so if you're entering multiple columns, it will jump to the first column you are entering |
  | `Up`                         | Move to the cell one row up |
  | `Down`                       | Move to the cell one row down |
  | `Left`                       | Move to the cell left |
  | `Right`                      | Move to the cell on the Right |
  | `Ctrl+<direction>`         | Move to the outermost cell in the direction given |
  | `Shift+<direction>`        | Select the current cell and the cell in `<direction>` |
  | `Ctrl+Shift+<direction>`   | Select all cells from the current to the outermost cell in `<direction>` |
  | `Ctrl+c`                     | `Copy` – copies the selected cells into the clipboard
  | `Ctrl+v`                     | `Paste` – pastes the clipboard
  | `Ctrl+x`                     | `Cut` – copies the selected cells into the clipboard and removes them from their original position |
  | `Ctrl+z`                     | `Undo` – undoes the last change you made |
  | `Ctrl+y`                     | `Redo` – undoes an undo |

=={.well}
**Tip:** Practice a bit, and you will find that you will become a lot faster using the keyboard than the mouse!
==


Locking Rows and Columns
------------------------

The spreadsheet we are working on is quite large. You will notice, that while scrolling the column with the column labels will frequently disappear, leaving you quite lost. The same with the country names. To avoid this you can “lock” rows and columns so they don't disappear.

### Walkthrough: Locking the top row

1.  Go to the Spreadsheet with our data and scroll to the top.
2.  On the top left, where the column and row labels are you'll see a small striped area.
![image](http://farm9.staticflickr.com/8322/8070104022_e233a65687_o_d.png)

3.  Hover over the striped bar on top of box showing row "1". A hand shaped cursor should appear, click and drag it down one row.
4.  Your result should look like this:
![image](http://farm9.staticflickr.com/8176/8070115059_d960b3d09e_o_d.png)

5.  Try scrolling – notice how the top row remains fixed?

Sorting Data
------------

The first thing to do when looking at a new dataset is to orient yourself. This involves at looking at maximum/minimum values and sorting the data so it makes sense. Let's look at the columns. We have data about the GDP, healthcare expenditure and life expectancy. Now let's explore the range of data by simply sorting.

### Walkthrough: Sorting a dataset

1.  Select the whole sheet you want to sort. Do this by clicking on the right upper grey field, between the row and column names.
![image](http://farm9.staticflickr.com/8322/8070104022_e233a65687_o_d.png)

2.  Select “Sort Range...” from the “Data” menu – this will open an additional Selection
3.  Check the “Data has header row” checkbox
![image](http://farm9.staticflickr.com/8437/7872826062_017d1bfe19_o_d.jpg)

4.  Select the column you want to sort by in the dropdown menu
5.  Try to sort by GDP – Which country has the lowest?
6.  Try again with different values, can you sort ascending and descending?

=={.well}
**Tip:** Be careful! A common mistake is to forget to select *all* the data. If you sort without selecting all the data, the rows will no longer match up.
==

*A version of this recipe can also be found in the Handbook.*

Filtering Data
--------------

The next thing commonly done with datasets is to filter out the values you don't want to see. Did you notice that some “Country Names” are actually not countries? You'll find things like “World”, “North America” and “Arab World”. Let's filter them out.

### Walkthrough: Filtering Data

1.  Select the whole table.
2.  Select “Filter” from the “Data” menu.
3.  You now should see triangles next to the column names in the first row.
4.  Click on the triangle next to country name.
5.  you should see a long list of country names in the box.
![image](http://farm9.staticflickr.com/8316/8070573150_2cf29b914f_o_d.png)

6.  Find those that are not a country and click on them (the green check mark will disappear).
7.  Now you have successfully filtered your dataset.
8.  Go ahead and play with it - the data will not be deleted, it’s just not displayed.

*A version of this recipe can also be found in the Handbook.*

Summary
-------

In this module we talked about basic spreadsheet skills. We talked about data entry and how to sort and filter data using a spreadsheet program.
In the [next course](http://schoolofdata.org/handbook/course/analyzing-data/) we will talk about data analysis and introduce you to formulas.

Further Reading and References
------------------------------

* [Google help](http://support.google.com/drive/bin/topic.py?hl=en&topic=2811806&parent=2811739&ctx=topi) on spreadsheets

Quiz
----

Check your sorting and filtering skills with the following quiz.

<iframe src="http://okfnlabs.org/scodaquiz/index.html#data/sort-and-filter.json" width="100%" height="850"
frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe><br/><br/>
<a href="../analyzing-data/" class="btn btn-primary btn-large">Next Course<span class="icon-arrow-right"></span></a>
<div class="alert alert-info">Any questions? Got stuck? <a class="btn btn-large btn-info" href="http://ask.schoolofdata.org">Ask School of Data!</a></div>

