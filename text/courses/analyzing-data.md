‘But what does it mean?’: Analyzing data (spreadsheets continued)
=================================================================

Introduction
------------

Once you have cleaned and filtered your dataset - it’s time for analysis. Analysing data helps us to learn what our data might mean and helps us to extract answers to our questions from the dataset.

Look at the data we imported. (In case you didn’t finish the previous tutorial, don’t worry. You can copy a sample spreadsheet [here](https://docs.google.com/spreadsheet/ccc?key=0AlgwwPNEvkP7dHZxU3h2YkczdFdMYnJmTVQzcE54a2c#gid=2)).

This is World Bank data containing GDP, population, health expenditure and life expectancy for the years 2000-2011. Take a moment to have a look at the data. It’s pretty interesting - what could it tell us?

=={.well}
**Task:** Brainstorm ideas. What could you investigate using this data?
==

Here are some ideas we came up with:

1.  How much (in USD) is spent on healthcare in total in each country?
2.  How much (in USD) is spent per capita in each country?
3.  In which country is the most spent per person? In which country is the least spent? What is the average for each continent? For the world?
4.  What is the relationship between public and private health expenditure in each country? Where do citizens spend more (private expenditure)? Where does the state spend more (public expenditure)?
5.  Is there a relationship between expenditure on healthcare and average life expectancy?
6.  Does it make any difference if the expenditure is public or private?

**NOTE:**: With these last two questions, you have to be really careful. Even if you find a connection, it doesn’t necessarily mean that one caused the other! For example: imagine there was a sudden outbreak of the plague; it’s not always fatal, but many people who contract it will die. Public healthcare expenditure might go up. Life expectancy drops right down. That doesn’t mean that your healthcare system has suddenly become less efficient! You always have to be *REALLY* careful about the conclusions you draw from this kind of data... but it can still be interesting to calculate the figures.

There are many more questions that could be answered using this data.
Many of them relate closely to current policy debates. For example, if my country were debating its healthcare spending right now, I could use this data to explore how spending in my country has changed over time, and begin to understand how my country compares to others.

Formulas
--------

So let’s dive in. The data we have is not entirely complete. At the moment, healthcare expenditure is only shown as a percentage of GDP. In order to compare total expenditure in different countries, we need to have this figure in US Dollars (USD).

To calculate this, let’s introduce you to spreadsheet formulas.

Formulas are what helped spreadsheets become an important tool. But how do they work? Let’s find out by playing with them...

=={.well}
**Tip:** Whenever you download a dataset, the very first thing you should do is to make a copy of it. Any changes you should make should be done in this copy - the original data should remain pure and untouched! This means that you can go back and check it at any time. It’s also good practice to note where you got your data from, when and how it was retrieved.
==

Once you have your own copy of the data (try adding ‘working copy’ or similar after the original name), create a new sheet within your spreadsheet. This is for you to mess around with whilst you learn about formulae.

Now move across to the “Total fruits sold” column. Start in the first row. It’s time to write a formula...

### Walkthrough: Using spreadsheets to add values.

Using this [example data](https://docs.google.com/spreadsheet/ccc?key=0AlgwwPNEvkP7dFBxSFp1c096V19zNnI2TF9yLWVUMkE#gid=0). Let’s calculate the total of fruits sold.

1. Get the data and create a working copy.
2. To start, move to the first row.
3. Each formula in a spreadsheet starts with `=`
4. Enter `=` and select the first cell you want to add. Notice how the cell reference appears in the formula?
![image](http://farm9.staticflickr.com/8179/8073780056_05b170a958_o_d.png)
5. now type `+` and select the second cell you want to add
![image](http://farm9.staticflickr.com/8173/8073780166_59fb9bcaa0_o_d.png)
6.  Press `Enter` or `tab` .
7.  The formula disappears and is replaced by the value.
![image](http://farm9.staticflickr.com/8176/8073780244_836ef3f299_o_d.png)
8.  Try changing the number in one of the original cells (apples or plums) you should see the value in total update automatically.
9.  You can type each formula individually, but it also possible to cut and paste or drag formulas across a range of cells.
10. Copy the formula you have just written (using `ctrl` + `c` ) and paste it into the cell below (using `ctrl` + `v` ), you will get the sum of the two numbers on the row below.
11. Alternatively click on the lower right corner of the cell (the blue square), and drag the formula down to the bottom of the column. Watch the `‘total’` column update. Feels like magic!

=={.well}
**Task:** Create a formula to calculate the total amount of apples and plums sold during the week.

**Did you add all of the cells up manually?:** That's a lot of clicking - for big spreadsheets, adding each cell manually could take a long time. Take a look at the "[spreadsheet formulae](http://schoolofdata.org/handbook/recipes/formulae-with-spreadsheets/)" section in the Handbook - can you see a way add a range of cells or entire columns simply?
==

Where Next?
-----------

Once you've got the hang of building a basic formula - the sky is your limit! The [School of Data Handbook](http://schoolofdata.org/handbook/recipes/formulae-with-spreadsheets/) will additionally walk you through:

-   Multiplication using spreadsheets
-   Division using spreadsheets
-   Copying formulae sideways
-   Calculating minimum and maximum values
-   Dealing with empty cells in your data (complex formulae). This stage uses Boolean logic .

You may need to refer to these chapters to complete the following challenges.

### Multiplication and division challenge

=={.well}

**Task:** Using the data from the World Bank (if you don't have it already, download it [here](http://dump.tentacleriot.eu/wb-gdp-health-life.csv).). In the data we have figures for healthcare only as a % of GDP. Calculate the full amount of private health expenditure in Afghanistan in 2001 in USD.
If your percentages are rusty - check out the formulae section in the Handbook.


**Task:** Still using the World Bank Data. Find out how much money (USD) is spent on healthcare per person in Albania in 2000.

**Task:** Calculate the mean and median values for all the columns.

**Task:** What is the formula for healthcare expenditure per capita? Can you modify it so it’s only calculated when both values are present (i.e. neither cell is blank)?
==


Summary & Further Reading
-------------------------

In this module we had an in depth view on analysis. We explored our dataset looking at the range of data. We further took a leap into conditional formulas to handle missing values and developed a quite complex formula step by step. Finally we touched on the subject of normalizing data to compare entities.

1.  [Google Spreadsheets Function List](https://support.google.com/docs/bin/static.py?hl=en&topic=25273&page=table.cs)
2.  [Introduction to Boolean Logic at the Wikiversity](http://en.wikiversity.org/wiki/Introduction_to_boolean_logic)

#### Quiz

Take the following quiz to check your analysis skills.

<div id="external-quiz">
<iframe
	src="http://okfnlabs.org/scodaquiz/index.html#data/analyzing-data.json"
	width="100%" height="850"
	frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>
<br/><br/>
<a href="../data-to-diagrams/" class="btn btn-primary btn-large">Next Course<span class="icon-arrow-right"></span></a>
<div class="alert alert-info">Any questions? Got stuck?
<a class="btn btn-large btn-info" href="http://ask.schoolofdata.org">Ask School of Data!</a>
</div>
