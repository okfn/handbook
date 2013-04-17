Making data on the web useful: scraping
=======================================

Introduction
------------
Many times data is not easily accessible - although it does exist. As much as we wish everything was available in CSV or the format of our choice - most data is published in different forms on the web. What if you want to use the data to combine it with other datasets and explore it independently? Scraping to the rescue!

Scraping describes the method to extract data hidden in documents - such as Web Pages and PDFs and make it useable for further processing. It is among the most useful skills if you set out to investigate data - and most of the time it’s not especially challenging. For the most simple ways of scraping you don’t even need to know how to write code.

This example relies heavily on Google Chrome for the first part. Some things work well with other browsers, however we will be using one specific browser extension only available on Chrome. If you can’t install Chrome, don’t worry the principles remain similar.

Extracting a table from a webpage using Google Spreadsheets
-----------------------------------------------------------

Knowing the structure of a website is the first step towards extracting and using the data. Let’s get our data into a spreadsheet - so we can use it further. An easy way to do this is provided by a special formula in Google Spreadsheets.

I’m always interested in politics - and parliaments websites are great places to go and start scraping. They usually have listings for members of parliament, their parties etc. Let’s look at a sample: The MP listing of the UK parliament: 

**Walkthrough:** Importing HTML tables into Google Spreadsheets. 

#. Go to http://drive.google.com, log in and create a new spreadsheet
#. Edit cell A1 (the top left cell)
#. Let’s import the table of UK MPs
#. Enter the following formula into the cell: =importHTML(“http://www.parliament.uk/mps-lords-and-offices/mps/”,”table”,2) (The last number indicates the number of the table in the document, just try them out and find the matching one...)
   .. image:: http://farm9.staticflickr.com/8224/8290901806_cffa226b9b_o_d.png        

#. Press Enter
#. Wait for a while and see the a table magically appear

   .. image:: http://farm9.staticflickr.com/8484/8163577989_c7dddb34ae_o_d.png
#. Now let’s do a little cleanup: Delete all heading rows (the ones containing *A* *B* and so on)
#. Notice how if you work with the sheet, the deleted rows appear again and again? This is because the formula keeps refreshing the content.
#. In order to change the content or delete it, we’ll need to copy the content of the first sheet into another sheet
#. Select the two columns that were imported in the spreadsheet
#. Copy them using “ctrl”+”c”
#. Create a new sheet in your spreadsheet
#. Right click the top left cell and select “paste special” - “paste values only”
   
   .. image:: http://farm9.staticflickr.com/8481/8163612088_fa538861bc_o_d.png

#. Once you’ve done this, filter the constituency field for “(blank)” values - this will give you all the letter headings (If you’re not sure how to do this - check out `this course </handbook/courses/sort-and-filter>`_ 
#. Delete the rows (you can simply select all and right click on the rows to delete them)
#. Turn off the filter to see the remaining rows
#. Notice how the first column contains three pieces of information (Surname, Name and Party). Let’s split this up
#. The surname is separated from the name and the party by a simple comma - let’s split it here.
#. The formula you’re going to use is =SPLIT(). It takes two values: 1. the String to be split 2. the delimiter.
#. Label the third column “Surname”. This is where our surname is going to be
#. In the second row enter =SPLIT(A2,”,”) and press enter
   
   .. image:: http://farm9.staticflickr.com/8478/8163612150_8a7579f818_o_d.png
#. This will split up the second row for Surname and Firstname (Party)
#. Extend the formula all the way down.
#. Now you can do the same with the first name (split with “(“ as delimiter)
#. Last let’s remove the trailing parenthesis from the party name
#. We are going to combine two formulas: =LEFT and =LEN. =LEFT gives us n characters of a text and LEN gives us the length of the text. We want all characters except the last one - so the formula is =LEFT(F2,LEN(F2)-1)
   
   .. image:: http://farm9.staticflickr.com/8070/8163612170_111f78b9fc_o_d.png
#. If you hide the columns you’re not interested in, you will end up with a sheet having Constituency, Surname and Name and Party of the MP.

.. raw:: html
  
  <div class="well">

**Task:** Find a website with a table and scrape the information from it. Share your result on the datahub.io (make sure to tag your dataset with schoolofdata.org)

.. raw:: html
  
  </div>

Detour - a short introduction to HTML
-------------------------------------
Getting data from websites might seem a little complicated at first - but rest assured, once you’ve done it a couple of times it will be similar. To extract data from websites we need to peek under the hood and look at the underlying HTML code. Don’t worry you don’t need to understand every detail of it just to be able to do so. 


HTML is the acronym for Hypertext Markup Language and is the language used to describe (markup) web pages. It is the underlying language to structure web-page content. HTML itself does not determine the way things look - it only helps to classify and structure content. So let’s peek at some websites. 

**Walkthrough:** Exploring HTML with Google Chrome

#. Open the website listing all MPs for the UK Parliament at http://www.parliament.uk/mps-lords-and-offices/mps/ in Chrome
#. Scroll down to the list of MPs
#. Right click on one of the entries
#. Select “Inspect Element”

   .. image:: http://farm9.staticflickr.com/8059/8163611876_c4f6fe8b57_o_d.png
#. Chrome will open a second area on the bottom of the page showing the underlying HTML code - focussed on the element you clicked
   
   .. image:: http://farm8.staticflickr.com/7280/8163577887_778ca2b7a6_o_d.png
#. The pointy brackets are the HTML tags. 
#. Now move your mouse up and down and notice how chrome tells you which element is which
#. You can expand and collapse certain sections by clicking on the triangles
#. Did you notice something? Every row in the long list of MPs is within one <tr></tr> section. <tr> indicates a table row. 
#. The names and the constituency are in <td></td> tags - td indicates table data. So we’re dealing with a table here?
#. If you scroll up the list you’ll notice a <table> element, followed by a <tbody> element - so yes this is a proper HTML table.

   .. image:: http://farm8.staticflickr.com/7266/8163611962_0b8a8c977a_o_d.png
#. Go ahead and explore!

HTML is no mystery. If you want to know more about it and how to build
webpages with it - visit the `School of Webcraft`_ for a gentle introduction.

.. _School of Webcraft: https://p2pu.org/en/schools/school-of-webcraft/

.. raw:: html

  <div class="well">

**Task:** Pick a website and look at the HTML code using Inspect Element. Did you find something interesting?

.. raw:: html
  
  </div>

Scraping websites using the Scraper extension for Chrome
--------------------------------------------------------
If you are using Google Chrome there is a browser extension for scraping web pages. It’s called “Scraper” and it is easy to use. It will help you scrape a website’s content and upload the results to google docs.


**Walkthrough:** Scraping a website with the Scraper extension

#. Open Google Chrome and click on Chrome Web Store
#. Search for “Scraper” in extensions
#. The first search result is the “Scraper” extension
#. Click the add to chrome button.
#. Now let’s go back to the listing of UK MPs
#. Open http://www.parliament.uk/mps-lords-and-offices/mps/
#. Now mark the entry for one MP
   
   .. image:: http://farm9.staticflickr.com/8490/8264509932_6cc8802992_o_d.png

#. Right click and select “scrape similar...”

   .. image:: http://farm9.staticflickr.com/8200/8264509972_f3a9e5d8e8_o_d.png
        
#. A new window will appear - the scraper console

   .. image:: http://farm9.staticflickr.com/8073/8263440961_9b94e63d56_b_d.jpg
        
#. In the scraper console you will see the scraped content
#. Click on “Save to Google Docs...” to save the scraped content as a Google Spreadsheet.


Easy wasn’t it? Now let’s do something a little more complicated. Let’s say
we’re interested in the roles a specific actress played. The source for all
kinds of data on this is the IMDB (You can also search on sites like
`DBpedia`_ or `Freebase`_ for this kinds of information; however, we’ll stick to IMDB to show the principle)

.. _DBpedia: http://dbpedia.org
.. _Freebase: http://freebase.com


**Waltkthrough:** extended scraping with the Scraper extension

#. Let’s say we’re interested in creating a timeline with all the movies the Italian actress Asia Argento ever starred; where do we start?
#. The IMDB has a quite comprehensive archive of actors. Asia Argento’s site is: http://www.imdb.com/name/nm0000782/
#. If you open the page you’ll see all the roles she ever played, together with a title and the year - let’s scrape this information
#. Try to scrape it like we did above
#. You’ll see the list comes out garbled - this is because the list here is structured quite differently.
#. Go to the scraper console. Notice the small box on the upper left, saying XPath?
#. XPath is a query language for HTML and XML.
#. XPath can help you find the elements in the page you’re interested in - all you need to do is find the right element and then write the xpath for it.
#. Now let’s assemble our table.
#. You’ll see that our current Xpath - the one including the whole information is “//div[3]/div[3]/div[2]/div”

   .. image:: http://farm9.staticflickr.com/8344/8264510130_ae31697fde_o_d.png       
#. Xpath is very simple it tells the computer to look at the HTML document and select <div> element number 3, then in this the third one, the second one and then all <div> elements (which if you count down our list, results in exactly where you are right now.
#. However, we’d like to have the data separated out. 
#. To do this use the columns part of the scraper console...
#. Let’s find our title first - look at the title using Inspect Element
   
   .. image:: http://farm9.staticflickr.com/8355/8263441157_b4672d01b2_o_d.png
#. See how the title is within a <b> tag? Let’s add the tag to our xpath.
#. The expression seems to work well: let’s make this our first column
#. In the “Columns” section, change the name of the first column to “title”
#. Now let’s add the XPATH for the title to it
#. The xpaths in the columns section are relative, that means “./b” will select the <b> element
#. add “./b” to the xpath for the title column and click “scrape”
   
   .. image:: http://farm9.staticflickr.com/8357/8263441315_42d6a8745d_o_d.png
#. See how you only get titles?
#. Now let’s continue for year? Years are within one <span>
#. Create a new column by clicking on the small plus next to your “title” column
#. Now create the “year” column with xpath “./span” 
   
   .. image:: http://farm9.staticflickr.com/8347/8263441355_89f4315a78_o_d.png
#. Click on scrape and see how the year is added
#. See how easily we got information out of a less structured webpage?

.. raw:: html
  
  <div class="well">

**Task:** Find a webpage having information you are interested in and scrape it! Don’t forget to post your results on datahub.io.

.. raw:: html
  
  </div>

Scraping more than one webpage: Scraperwiki
-------------------------------------------
Until now we’ve only scraped data from a single webpage. What if there are
more? Or you want to scrape complex databases? You’ll need to learn how to
program - at least a bit. Fortunately for you there is a good website for
programming scrapers: `Scraperwiki.com`_

.. _Scraperwiki.com: http://scraperwiki.com

Scraperwiki has two main functions: You can write scrapers - which are
optionally run regularly and the data is available to everyone visiting -
or you can request them to write scrapers for you. The latter costs some
money - however it helps to contact the Scraperwiki community (`Google
Group`_) someone might get excited about it and help you!.

.. _Google Group: https://groups.google.com/forum/?fromgroups=#!forum/scraperwiki


If you are interested in writing scrapers with Scraperwiki, check out this sample scraper - scraping the MP data like we did in the examples above: https://scraperwiki.com/scrapers/members_of_the_uk_parliament/ - click View source to see the details. Also check out the scraperwiki documentation: https://scraperwiki.com/docs/python/


Summary:
--------
In this course we’ve covered Web scraping and how to extract data from websites. The main function of scraping is to convert data that is semi-structured into structured data and make it easily useable for further processing. While this is a relatively simple task with a bit of programming - for single webpages it is also feasible without any programming at all. We’ve introduced =importHTML and the Scraper extension for your scraping needs.

Further Reading
---------------
See blogpost: http://schoolofdata.org/2012/12/04/the-webpage-is-the-api-scraping-resources/
