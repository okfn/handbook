======================
Cleaning spending data
======================

Often, you will need to clean up the spending data that you receive. Even government data is not perfect. 

In this section, we highlight some common issues experience when working with spending data. 

In the recipe book - you will find a recipe to help you solve these issues. 

Common issues with spending data: 

* **Typos** - E.g. some of your cells contain “Rroceeds from global taxes” rather than “Proceeds from global taxes”
* **Inconsistencies** - You may be looking to try and find out how much money does company X receive from government. However in your data, sometimes the company is entered variously as "Fuzzy Robot Llama Exporters", "Fuzzy Robot Llama Exporters Ltd", "FRLE Ltd" - you need a way to tell that these are all the same. 
* **Blank columns, rows and cells** - When you are summing up values it is very important to know what is a genuine zero and what is a blank due to the absence of data. 
* **Human Friendly Formatting** - such as pseudo rows and things being in horizontal rows when you need them in verticals - your computer probably needs the computer to be laid out somewhat consistently if it is to be able to process it.  
* **Multiple types of information contained in a single column**. For example:  

========================  ============
Revenue, Extractives      300,000,000
Revenue, Taxation         100,000,000
Expenditure, Healthcare   50,000,000
=======================  ============

Actually, it would be more helpful to have a column just to have one column with just whether a transaction was revenue or expenditure and a second to allow you to filter by revenue / expenditure type. 

* **Whitespace** - You don't see it, but it causes big problems in datasets. To many databases, the two transactions below would be treated differently due to the extra space at the end: 
=====================  =============
Fiscal revenue          50,000
Fiscal revenue[space]   50,000
======================  =============

So if you ever filtered or searched for just "Fiscal revenue" [no space at the end] - you would actually be omitting the latter case - possibly leading to incorrect conclusions. You can remove the nasty white space quite easily. 

