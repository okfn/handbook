=====================
Formatting your data
====================

Local Council Budget Data Cameroon 

This guide is a reference for future data loads of Local Budget Data into OpenSpending based on the types of issues encountered upon converting the data into the correct format during the setup of cameroon.openspending.org. 

This is not a full list of instructions for how to format data for OpenSpending, but a condensed list based on frequently recurring problems with the data. 
Why we need the data in a normalized format?
The OpenSpending database requires structured, machine-readable data. 
What is machine-readable data? 
Machine-readable data is data which a computer can easily sort, filter and analyse. Common file formats which are machine-readable are Excel files, CSV (Comma Separated Values) and XML. OpenSpending takes CSV files, these can easily be exported from Excel or other spreadsheet programmes. Look in the export options of the programme you are using), in Excel: File -> Save As -> Format: “Windows Comma Separated (csv)”; Google Docs: File > Dowload as... > CSV. 
Why isn’t a table in a Word document or PDF file ‘structured data’? 
Programs like Word are designed to present page layouts which look visually pleasing from a human perspective. Yet these files are not machine-readable in the same sense: tables inside them cannot be analyzed, sorted, filtered or exported easily into another application like OpenSpending.

It is often possible to convert unstructured data into structured data, e.g. by copying and pasting a version of a table in a Word document into Excel. Some errors may be introduced in the process, so some data cleaning will be required, but this document details some guidelines for how to clean up data upon conversion. In other cases, especially with PDF files, copy and paste may fail completely, and you need to use a specific application, such as Acrobat Professional, ABBYY FineReader or pdf2html, a command-line tool for bulk transformation.
Structuring data for OpenSpending
Besides ensuring that the file format for the data is machine-readable. Data also needs to be structured in a specific way in order to be loaded into OpenSpending. OpenSpending is very flexible with regard to structure, for example, it does not specify the column order, however the content of the columns must be standardised. 

Based on the local council data for Cameroon, we have drawn up a simple template which could serve as a model for future data conversions. This file contains some sample data from the council of Tignere and a template for data. Below are some guidelines which will help to format data for use in OpenSpending. 

1. OpenSpending requires there to be one header row in the file. This is what the software will look for to identify the names of your columns. 

For example, in this file of the Tignere budget, there were 3 rows of header before the actual data begins. The header row needs to be the first row in the file; all the others are treated as data rows.
The original data:


Revised data:



You will notice several changes: 

First row of the original data was removed, this was a title (you will have the opportunity to give your dataset a title when you get to the loading phase of OpenSpending)
Rows should contain only one type of information i.e. one budget line (or “fact”). In the original file, you will see that any individual row contains data for multiple years, as well as both budgeted and actual spend. In the revised version, one individual row contains a maximum of one time period, and contrasts have been created within columns. For example, it is now possible to filter column H by revenue / expenditure to see only line items that relate to revenue, likewise for other criteria such as reporting type. Note that formatting data for OpenSpending often means creating many more rows than were found in the original document. 
Percentage columns have been omitted. OpenSpending can do the maths itself. 

Note that this could equally be translated into French, provided here in English purely for demonstration purposes.

2. Columns in a file should be homogeneous. This means: 
No blank rows or cells. Data imported into OpenSpending should be fairly de-normalized: while there may be references to external code sheets/master data, each row should contain all the information required to construct the resulting item. Columns (particularly classifications) should have a value for each row; they will not automatically “fill down”.
No pre-aggregated totals (e.g. sub-totals or “roll-ups”) within the data (OpenSpending will do the maths and compute these automatically)

Example:
As you will see in the example above:

Many cells are blank, these should either be replaced with 0, filled in, or removed. 
There is a pre-aggregated total (in grey), this line should be removed. 

We will cover how to transform data and check for a few common errors in later tutorials. 

3. There must be a combination of columns or an individual column which constitutes a ‘unique identifier’

OpenSpending was built with a view to re-loading entries into the database at any time, even when existing data is loaded. This means that there must be some way to calculate a unique fingerprint for each row in the data which OpenSpending can use to determine whether it should update an existing row or create a new one. 

The easiest way to do this is to just add a dummy column to the dataset in which you put a number that increases for each row (you can do this in Excel by typing the numbers into the first two rows, selecting both cells and dragging down the lower right corner of the cell to extend the series).
Other things to look out for when preparing data for OpenSpending 
Amounts should be presented in purely numerical format (i.e. no commas, points (“.”) should be used as decimal separators only). 
Amounts should be actual amounts i.e. 


Amount
1657000

rather than

Amount (in thousands)
1657

The transformations we have performed on the data are relatively simple and the datasets provided for this project so far are relatively small. This means that it is perfectly possible to transform data by manually re-entering or using only simple spreadsheet functions. However, there are tools which can help to quickly transform the data and help to reduce the chances of errors such as typos being introduced into the data. 

This list of transformations is not exhaustive, but targets the common errors and amendments required. Preliminary steps for how to fix other common errors in data have been outlined in this webpage on OpenSpending. 
Pre-export checklist

There is only one header column
Each row contains only one logical type of information (e.g. not multiple years) 
There are no blank rows or cells
There are no pre-aggregated totals
There is a column / combination of columns which constitutes a unique identifier 
Run a spell-check - OpenSpending groups together objects which it thinks are the same so having a typo e.g. ‘Ministère des Affaires sociales’ and ‘Ministere des Affaires sociales’ - would be treated as two separate entities. Also check for things such as differences in capitalisation. 
There are no digit separators such as commas in the amount column. 
Amounts in the amount column are real numbers rather than e.g. amounts in thousands. 
Dates are in the format YEAR-MM-DD or YEAR-MM or YEAR
There is no personal information such as phone numbers / addresses in the file

You are now ready to export your file as a CSV ready to upload online. NOTE - please make sure to save your file with UTF-8 encoding to ensure special characters and diacritics are preserved. 

How to export your file as CSV

In Google Docs: File > Publish To the Web > [Select correct sheets to publish] > Republish now > Under ‘Get a link to the published data’ select ‘CSV’ from the dropdown menu and select relevant sheets

In Excel: File > Save As Type > Windows Comma Separated Values (In some versions: ‘CSV Comma Delimited’)

In Numbers: File > Export > CSV

In Libre Office (formerly OpenOffice or StarOffice): File > Save As.. > In the “File type” menu: “Text CSV (.csv)”
Post export checklist: 

After exporting open your file to check:
Diacritics and special characters display correctly in your new file
For source data in Excel files, make sure that all macros in the document were correctly turned into static values by the CSV exporter function. If your Excel sheet has export protection, you may need to find an appropriate cracking tool.

Upload it to the web
^^^^^^^^^^^^^^^^^^^^

You now need to get your data online so that OpenSpending knows where to look for it. There are many ways to do this e.g. in a public folder in Dropbox, or exporting directly from Google Docs (File > Publish to the Web > Republish Now > [In ‘Get a Link to Published Data’ Section] Select CSV and the correct sheet of your data > Copy the link from the box). 

We used the DataHub, an online repository for data, which is a quick and easy option. We’ve made a quick video to show you how to do this below: 

https://vimeo.com/43720463 

Ideally you should upload both the original file (before changes) and the modified version. This allows for easy comparison should there be any issues or question regarding the provenance. You can add both datasets as resources to the same package on the DataHub, so that it is clear that they refer to the same thing.