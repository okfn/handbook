===================================================================
‘But what does it mean?’: Analyzing data (& spreadsheets continued)
===================================================================

Introduction
=============
Once you have cleaned and filtered your dataset - it’s time for analysis. (In case you didn’t finish the previous tutorial, don’t worry you can copy a sample spreadsheet `here <https://docs.google.com/spreadsheet/ccc?key=0AlgwwPNEvkP7dHZxU3h2YkczdFdMYnJmTVQzcE54a2c#gid=2>`__). Analysing data helps us to learn what our data might mean and helps us to extract answers to our questions from the dataset.

Look at the data we imported: This is worldbank data containing GDP, population, health expenditure and life expectancy for the years 2000-2011. Take a moment to have a look at the data. It’s pretty interesting - what could it tell us? 

**Task:**
 Brainstorm ideas. What could you investigate using this data?  

Here are some ideas we came up with:

#. How much (in $) is spent on health care in total in each country?
#. How much (in $) is spent per capita in each country? 
#. In which country is the most spent per person? In which country is the least spent? What is the average for each continent? For the world?
#. What is the relationship between public and private health expenditure in each country? Where do citizens spend more (private expenditure)? Where does the state spend more (public expenditure)?
#. Is there a relationship between expenditure on health care and average life expectancy?
#. Does it make any difference if the expenditure is public or private?

**NOTE:**
 With these last two questions, you have to be really careful. Even if you find a connection, it doesn’t necessarily have to be causal! For example: imagine there was a sudden outbreak of the plague. It’s not always fatal, but many people who contract it will die. Public healthcare expenditure might go up. Life expectancy drops right down. That doesn’t mean that your healthcare system has suddenly become less efficient! You always have to be *REALLY* careful about the conclusions you draw from this kind of data... but it can still be interesting to calculate the figures

There are many more questions that could be answered using this data. Many of them relate closely to current policy debates. For example, if my country were debating its health care spending right now, I could use this data to explore how spending in my country has changed over time, and begin to understand how my country compares to others. 

Formulas
========
So let’s dive in. The data we have is not entirely complete. At the moment, healthcare expenditure is only shown as a percentage of GDP. In order to compare total expenditure in different countries, we need to have this figure in US$. 

To calculate this, let’s introduce you to spreadsheet formulas. 

Formulas are what helped spreadsheets become an important tool. But how do they work? Let’s find out by playing with them...

**Tip:**
 Whenever you download a dataset, the very first thing you should do is to make a copy of it. Any changes you should make should be done in this copy - the original data should remain pure and untouched! This means that you can go back and check it at any time. It’s also good practice to note where you got your data from, when and how it was retrieved.

Once you have your own copy of the data (try adding ‘working copy’ or similar after the original name), create a new sheet within your spreadsheet. This is for you to mess around with whilst you learn about formulae. 

Now move across to the “Total fruits sold” column. Start in the first row. It’s time to write a formula...

**Walkthrough:**
 your first formula

#. Get the `example data <https://docs.google.com/spreadsheet/ccc?key=0AlgwwPNEvkP7dFBxSFp1c096V19zNnI2TF9yLWVUMkE#gid=0>`_ and create a copy.
#. Let’s calculate the total of fruits sold.
#. To start, move to the first row.
#. Each formula in a spreadsheet starts with ``=``
#. Enter ``=`` and select the first cell you want to add. Notice how the cell reference appears in the formula?

   .. image:: http://farm9.staticflickr.com/8179/8073780056_05b170a958_o_d.png
#. now type ``+`` and select the second cell you want to add

   .. image:: http://farm9.staticflickr.com/8173/8073780166_59fb9bcaa0_o_d.png
#. Press **“Enter”** or **“tab”**
#. The formula disappears and is replaced by the value.

   .. image:: http://farm9.staticflickr.com/8176/8073780244_836ef3f299_o_d.png
#. Try changing the number in one of the original cells (apples or plums) you should see the value in total update automatically.
#. You can type each formula individually, but it also possible to cut and paste or drag formulas across a range of cells. 
#. Copy the formula you have just written (using **“ctrl”**+**”c”**) and paste it into the cell below (using **“ctrl”**+**”v”**), you will get the sum of the two numbers on the row below. 
#. Alternatively click on the lower right corner of the cell (the blue square), and drag the formula down to the bottom of the column. Watch the ``‘total’`` column update. Feels like magic!


**Task:**
 Create a formula to calculate the total amount of apples, plums and fruit sold during the week.

A quick introduction to common spreadsheet symbols
==================================================
Now that you have a sense of how spreadsheet formula work, here’s a quick introduction to some of the most common formula symbols that you are likely to come across. 

These are all ‘basic maths functions’ - the kind of things you would find on a simple calculator. 

``=``
  Tells your spreadsheet that you are writing a formula. This is the |      first thing that should go in your formula cell. (NOTE: A spreadsheet assumes that *everything* that begins with an ‘=’ is a formula... so be careful how you use it!)

``+``
  Add

``-`` 
  Subtract

``*``
  Multiply (this would be ‘x’ on a calculator)

``/``
  Divide (this would be ‘÷’ on a calculator)

It is worth remembering that basic maths rules about the order of functions apply. For example, the formula  ``=3+5*2`` will give you ``13``, NOT 16. If you’re not sure why or can’t quite remember the rules, check out `this basic introduction <http://www.mathsisfun.com/operation-order-bodmas.html>`__. If you want to change the order of function you’ll need parentheses: Formulas inside parentheses will be evaluated before any other formula. If you want the formula above to result in 16 you’ll need to type: ``=(3+5)*2``

Have a go at using these formula in the ‘play sheet’ of your spreadsheet until you feel comfortable with them. You should find that they work pretty much as you would expect them to. 

What if you wanted to add more numbers? You could always add them manually using `+` or you could use `SUM` a formula to sum up all the values in the given range. Let’s try to calculate how many apples, plums and total fruit we sold during the week: Go to cell B7 and type ``=SUM(A2:A6)`` this will add the numbers of apples. 

**Task:** 
 Find out how many plums and total fruit were sold during the week.

 
Calculating more Values with Worldbank Data
===========================================
Now that you’ve got to grips with the basics of spreadsheet formula, let’s go back to our worldbank dataset.
The first thing we wanted to calculate how much money (in US$) is spent on healthcare per country and year. Let’s get started!

In our original data, we have three columns related to health expenditure; ‘health expenditure (private)’, ‘health expenditure (public)’ and ‘health expenditure (total)’. So you’re going to need to add three new columns to the right of the spreadsheet to do your calculations. Give them each a heading; perhaps ‘health expenditure (private) in $’ etc.


**Task:**
 What formula will you need to calculate the amount of private health expenditure in $? See if you can do it yourself! 

If you didn’t manage it, here’s how to work out the formula you need.

**Walkthrough:**
 Calculating healthcare expenditure

In the original data, public, private and total healthcare expenditure is expressed as a % of GDP. The GDP is already given in US$. To work out the expenditure in US$ from these two facts is just one step. 

1. Math recap: If you have the percentage and the value it is associated with you can calculate the value of the percentage. e.q. let’s say 25% of people in a town of 1000 inhabitants are below 15 years. You can calculate the number of inhabitants by: 25*1000/100 = 250 people in the town are below 15 years old. (For more thorough explanation of percentages check out `BBC Skillswise <http://www.bbc.co.uk/skillswise/topic/percentages>`__
2. Let’s start by looking at the very first complete row (NB: spot the gap! we don’t have the data for Afghanistan’s GDP in 2000. just be aware of this for now (we will talk in more detail about gaps in data later). The first complete row is Afghanistan in 2001
3. In 2001, Afghanistan’s GDP was $2,461,666,315. Their private healthcare expenditure was 6.009337744% of this. So the calculation you need to do is 

``2461666315 * 6.009337744 / 100``

4. With a spreadsheet formula, we don’t have to worry about all the numbers - you just need to enter the cells. So the formula you are going to need is: ``=E3*H3/100`` (where cell E3 contains Afghanistan’s GDP in 2001, and cell H3 contains private health expenditure in Afghanistan in 2001).
5. Drag this formula all the way down the column and hey presto! You should have calculated the private health expenditure in $ for every country for the past 10 years. Much quicker than doing all the sums yourself!

**Task:**
 Can you work out the formula for public health expenditure and total health expenditure? Note: There is an easier way than writing a new formula every time!

**Answer:**
 In the same way as we could drag the formula down the column and the spreadsheet recognized the pattern and chose the correct cells, we can also drag the formula sideways to the new columns (public health expenditure in $ and total health expenditure in $). BUT we need to make one minor adjustment.

Try just dragging it across for a moment. Can you see the problem? The spreadsheet automatically moves *all* the cells its looking at one column to the right. So whereas before we had:

``=E3*H3/100``

we now have

``=F3*I3/100``

...but GDP is still in column E, so this formula is not the one we want.

To ‘fix’ a column or row, all you need to do is add ‘$’ in front of the section you want to fix. So, if you adapt your original formula to

``=$E3*H3/100``

you should be able to drag it over to the right without any problems. 

**Tip:**
 It can be a little confusing getting used to the ``$`` command at first. If this is the first time you’ve come across it, we suggest you spend some time playing around and seeing what it can do. Go back to your ‘play’ spreadsheet, make up some numbers, and experiment! Try for example ``=$B2*C2`` vs ``=B$2*C2``````, drag it around, and see what difference that makes. The best way to get comfortable with formulae is to use them! 

So now, with one simple formula, you can calculate the actual expenditure of public, private and public+private healthcare, in every country, for the past ten years. Spreadsheets are pretty powerful things..

**Task:**
 Find out how many USD ($) is spent on healthcare per person.

Minimum and Maximum Values
==========================
Now let’s go to our first step of analysis. One thing that is very interesting to us is the maximum and minimum values of each of the columns we have. This will help us understand if the values are close together or far apart. Let’s do this!

**Walthrough:**
 Minimum and Maximum Values

#. Open a new sheet. Do so by clicking the “+” in the lower left corner

   .. image:: http://farm9.staticflickr.com/8322/8074120798_3d93affac2_o_d.png
#. Leave the first column in the first row blank, in the second column enter ``=`` to tell the spreadsheet you will be using a formula. 
#. Switch back to the sheet with your worldbank dataset.
#. Select the first column that has numerical data on the sheet where your data lives. 

   .. image:: http://farm9.staticflickr.com/8041/8074136559_b4bff47e8d_o_d.png
#. press enter and you will see the name in the first sheet: magic. Why do we do it like this and not simply copy and paste? This will automatically change the headings if you change your headings (e.q. you move columns around or rename things). 
#. Now the first column is going to be what you calculate: type Minimum in the second row first column (A2) for the minimum value. 
#. In the cell right next to it type ``=MIN(`` (MIN is the formula for minimum)
    
   .. image:: http://farm9.staticflickr.com/8173/8074138256_a28c26e012_o_d.png
#. Go back to the other sheet to select the first column with numerical data - to select the whole column click on the grey area with the column letter. 

   .. image:: http://farm9.staticflickr.com/8038/8074152513_ec168d9411_o_d.png
#. Close the brackets by typing ``)``. 
#. You should now see the minimum value in that field. 
#. Now do the same for Maximum in the third row. Once you are done, just mark the three values in the second row (the formula for maximum is =max() )
#. See the blue square in the right lower corner? Grab it and pull it right. Release it and if you still not have all columns, carry on until you have all values. 
#. This way you created a table with the minima and maxima of each of the columns.

**Task:**
  Calculate the average and median values for all the columns

How to deal with empty cells
============================
Did you notice some of the minimum values are 0? Do you really believe there are countries not spending money on health care? There aren’t the zeroes are because there are empty cells. Properly handling missing values is an important step in data cleaning and analysis - hardly ever are large datasets complete and you have to find a strategy to deal with missing parts. 

In the next walkthrough we will create a complex formula. We will do so with an iterative process  - this means one little formula at the time. If you follow us through you’ll notice you can create quite complex formulas and results simply step by step.

**Waltkthrough:**
 Dealing with empty cells.

#. To deal with empty cells we have to fix parts of our calculation formulas in the worldbank datasheet
#. To start - create a mock spreadsheet to play with data. Copy the first few rows of the worldbank dataset into it so you’ll have a start. To validate our formulas try to remove values in some of the rows.

   .. figure:: http://farm9.staticflickr.com/8189/8076432091_46b551a5fe_b_d.jpg
#. we got a missing problem right in the first value: Afghanistans GDP is missing for the year 2000. 
#. Think about our goal. What we want to achieve: if either of the values we are multiplying (in this case, GDP or health expenditure) is **not** a number (probably because the value is missing), we don’t want to display the total. 
#. To put it another way: **Only if** a value for both GDP and healthcare expenditure is present should the spreadsheet carry out the calculation; **otherwise** it should leave the cell blank. 
#. The formula to express this condition is ‘IF’. (You can find an overview on formulas like this on the `google doc help <https://support.google.com/docs/bin/static.py?hl=en&topic=25273&page=table.cs>`__.) 
#. The formula asks us to fill out the three things: (1) Condition, (2) value if the condition is true, (3) value if the condition is false. 

   ``=IF(Condition, Value if condition is true, Value if condition is false)``

#. In our case we know parts (2) and (3). (2) is the formula we used above  this is the calculation we want to carry out if both values are present in the spreadsheet.

   ``=IF(Condition, $E3*H3/100, Value if condition is false)``

#. (3) is a blank - if the numbers aren’t there, we don’t want to display anything, so we fill in that value with nothing at all.

   ``=IF(Condition, $E3*H3/100,)``

#. So now we just need to work out (1), the condition. 

   ``=IF(Condition, $E3*G3/100,)``

#. Remember that we want the condition to be that BOTH the GDP and healthcare expenditure values are a number. The formula to see whether a cell is a number is: ``ISNUMBER``. 
#. This is another one of those little formulas that you should try playing with! If you type ``=ISNUMBER(F2)`` and ``F2`` is an empty field, it will say ``FALSE``. If there is a number it will say ``TRUE``. Handy isn’t it?

   .. image:: http://farm9.staticflickr.com/8326/8076431832_5de5ce1dd2_o_d.png
#. We want a formula that will only be calculated if both GDP *and* healthcare expenditure are actual numbers. 
#. We need to combine the results of both ``ISNUMBER(GDP)`` and ``ISNUMBER(healthcare expenditure)`` together. The formula to do so is AND. This will simply say ``TRUE`` if both of them are ``TRUE`` (i.e. both of them numbers) or ``FALSE`` if either one or both of them is ``FALSE``. 

   .. image:: http://farm9.staticflickr.com/8332/8076444273_f554a395cc_o_d.png
#. Which is exactly what we need. So our condition will be:

   ``AND(ISNUMBER(gdp),ISNUMBER(healthcare expenditure))``

#. or, to use our cells from before

   ``AND(ISNUMBER($E3),ISNUMBER(H3))`` 

   .. image:: http://farm9.staticflickr.com/8186/8076443230_8ef7b909e6_b_d.jpg
#. Phew! So now we can put parts (1), (2) and (3) from above all together in one big formula, using ‘IF’

   ``=IF(Condition, $E2*H2/100,)``

   ``=IF(AND(ISNUMBER($E2),ISNUMBER(H2)),$E2*H2/100,)``

#. Try it out: enter it to the first row of the first column of the calculation and paste it to all the other places. It should leave the cells empty.

   .. image:: http://farm9.staticflickr.com/8185/8076469857_3c5153582f_b_d.jpg

If you look at the data you will quickly find out that countries with higher number of people spend more on healthcare than countries with lower number of people. Intuitive isn’t it. So how to compare the countries more directly? Break it down to healtcare expenditure per person!. This step is called normalization and is a step often done when comparing different entities - such as countries etc. 

**TASK:**
 What is the formula for health care expenditure per capita? Can you modify it so it’s only calculated when both values are present?


Summary & Further Reading
=========================

In this module we had an in depth view on analysis. We explored our dataset looking at the range of data. We further took a leap into conditional formulas to handle missing values and developed a quite complex formula step by step. Finally we touched on the subject of normalizing data to compare entities.

1. `Google Spreadsheets Function List <https://support.google.com/docs/bin/static.py?hl=en&topic=25273&page=table.cs>`__
2. `Introduction to Boolean Logic at the Wikiversity <http://en.wikiversity.org/wiki/Introduction_to_boolean_logic>`__



