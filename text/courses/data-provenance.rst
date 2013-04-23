================
Data provenance
================

Good documentation on data provenance (the origin and history of a dataset) can be compared to the chain of custody which is maintained for criminal investigations: each previous owner of a dataset must be identified, and they are held accountable for the processing and cleaning operations they have performed on the data. For Excel spreadsheets this would include writing down the steps taken in transforming the data, while advanced data tools (such as Open Refine, formerly Google Refine), often provide methods of exporting machine-readable data containing processing history. Any programs that have been written to process the data should be available when users access your end result and shared as open-source code on a public code sharing site such as GitHub.

Tools for documenting your data work
------------------------------------

Documenting the transformations you perform on your data can be as simple as a detailed prose explanation and a series of spreadsheets that represent key, intermediate steps. But there are also a few products out there that are specifically geared towards helping you do this. Socrata is one platform that helps you perform transforms on spreadsheet-like data and share them with others easily. You can also use the `Data Hub`_ (pictured below), an open source platform that allows for several versions of a spreadsheet to be collected together into one dataset, and also auto-generates an API to boot.

If you want to get really smart, you may like to try using version control for your data work. Using version control will track every change made to the data, and allow you to easily roll back if there are any mistakes. Software Carpentry offer a good `introduction`_ to the topic. 

.. image:: http://content.openspending.org/resources/handbook/static/Screen%20Shot%202012-11-15%20at%2015.35.38.png

.. _Data Hub: http://datahub.io/
.. _introduction: http://software-carpentry.org/4_0/vc/  

Tips for documenting your work
------------------------------

#. Link to the original data and mention where you got it from. This is important to show exactly where the original source was. 
#. Show and describe everything that you change in the data along the way. This is equally important, both for you and for others to be able to check your work. (See how in the screenshot above - we have adjusted units for currency and explained what we have done at every step). 



