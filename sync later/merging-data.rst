================================================
Merging in data from another project/spreadsheet
================================================

One of the most powerful functions of Google Refine is the option to combine information from multiple Refine Projects. Given a shared set of values in a particular column, attributes from one table can be imported into the other.

NOTE: Users of Microsoft Excel might know a similar function called VLOOKUP, while users of relational databases will be familiar with the idea of a JOIN. 

Merges in Context
^^^^^^^^^^^^^^^^^

Assume, for example, that one core dataset contains information about how much money was spent (the accounts) but the departments are referred to only by codes. We have another code sheet where we have reference data - a list of all of the codes and their human-readable names in both English and French.  

Example
^^^^^^^^

Using this `accounts data`_ and this `codes and translations data`_ let's demonstrate how a cross works. You will need to load these into Google Refine. 

.. _accounts data: http://datahub.io/dataset/sample-spending-data-for-school-of-data-tutorial/resource/328c3782-073e-4833-8cb4-07b2030c7521
.. _codes and translations data: http://datahub.io/dataset/sample-spending-data-for-school-of-data-tutorial/resource/6d3d2b71-adf2-4d39-9f70-2ab6e1fda223

The merge function, called "cross" in Refine, is somewhat complex to use since it must be scripted as a command and the code involves both the concept of a cell and various rows. It’s `documentation`_ may give further guidance. 

To run it, open the “Cod” column dropdown in your accounts data:: 
  Edit column > Add column based on this column...
  
(This function is also useful when applying general transformation where you want both the original and transformed data to remain available.) 

.. _documentation: https://code.google.com/p/google-refine/wiki/GRELOtherFunctions

In the transformation code box, type the following:: 

	cell.cross(“Cameroon Budget Codes”, “code_category”).cells[“en”].values[0]

This command, when executed, will pull in the chapter titles from the budget codes project. 

As may be obvious, the first argument to cross, “Cameroon Budget Codes” is the project name of the project from which we’ll pull in our data. 
The next argument “code_category” is the name of the column which contains the chapter codes in that project. 
Each value in the investment data “Chapter” column will thus be searched in the “code_category” column. 

If a match is found, we will receive a reference to the row in which it occurred. This reference can be used to look up a specific column in the budget codes project: cells[“en”] will pick the value column called “en”. 
Finally, any such linkage may yield multiple results: a given chapter code may occur not once but many times in the project we’re crossing with. In this example, we’re using .values[0] to select the first match, irrespective of the total number of possible links (which will always be one, as the budget codes spreadsheet has no duplicates).

After verifying the result in the preview and adding a name for the new column, pressing “OK” will add the desired values. You can repeat this for each column you want to import, e.g. for the focus sector or COFOG codes.

Further Reading
^^^^^^^^^^^^^^^
The operations explained in this tutorial are the most common actions needed when cleaning up data for OpenSpending. The software offers a much larger set of functions for data cleansing, so it is worthwhile to browse the documentation at: 

http://code.google.com/p/google-refine/wiki/DocumentationForUsers

In particular, we recommend using the clustering functions on manually created and messy datasets as well as the web retrieval options to add further attributes to a table from an external source.

and has a column “Chapter”, which contains only a numeric identifier for the budget chapter the investment was allocated under. At the same time, another dataset may contain more information about each chapter, such as the full title and its association to other classification schemes.

