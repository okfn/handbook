Scraping websites using the Scraper extension for Chrome
========================================================

If you are using Google Chrome there is a browser extension for scraping web pages. It’s called “Scraper” and it is easy to use. It will help you scrape a website’s content and upload the results to google docs.


Walkthrough: Scraping a website with the Scraper extension
----------------------------------------------------------

1. Open Google Chrome and click on Chrome Web Store
2. Search for “Scraper” in extensions
3. The first search result is the “Scraper” extension
4. Click the add to chrome button.
5. Now let’s go back to the listing of UK MPs
6. Open [http://www.parliament.uk/mps-lords-and-offices/mps/](http://www.parliament.uk/mps-lords-and-offices/mps/)
7. Now mark the entry for one MP
![image](http://farm9.staticflickr.com/8490/8264509932_6cc8802992_o_d.png)
8.  Right click and select `scrape similar...`
![image](http://farm9.staticflickr.com/8200/8264509972_f3a9e5d8e8_o_d.png)
9. A new window will appear - the scraper console
![image](http://farm9.staticflickr.com/8073/8263440961_9b94e63d56_b_d.jpg)
10. In the scraper console you will see the scraped content
11. Click on `Save to Google Docs...` to save the scraped content as a Google Spreadsheet.


Walkthrough: extended scraping with the Scraper extension
---------------------------------------------------------

Note: Before beginning this recipe - you may find it useful to understand a bit about HTML. Read our [HTML primer](http://schoolofdata.org/handbook/recipes/introduction-to-html/).

Easy wasn’t it? Now let’s do something a little more complicated. Let’s say we’re interested in the roles a specific actress played. The source for all kinds of data on this is the IMDB (You can also search on sites like [DBpedia](http://dbpedia.org) or [Freebase](http://freebase.com) for this kinds of information; however, we’ll stick to IMDB to show the principle)

1. Let’s say we’re interested in creating a timeline with all the movies the Italian actress Asia Argento ever starred; where do we start?
2. The IMDB has a quite comprehensive archive of actors. Asia Argento’s site is: [http://www.imdb.com/name/nm0000782/](http://www.imdb.com/name/nm0000782/)
3. If you open the page you’ll see all the roles she ever played, together with a title and the year - let’s scrape this information
4. Try to scrape it like we did above
5. You’ll see the list comes out garbled - this is because the list here is structured quite differently.
6. Go to the scraper console. Notice the small box on the upper left, saying XPath?
7. XPath is a query language for HTML and XML.
8. XPath can help you find the elements in the page you’re interested in - all you need to do is find the right element and then write the xpath for it.
9. Now let’s assemble our table.
10. You’ll see that our current Xpath - the one including the whole information is `//div[3]/div[3]/div[2]/div`
![image](http://farm9.staticflickr.com/8344/8264510130_ae31697fde_o_d.png)
11. Xpath is very simple it tells the computer to look at the HTML document and select `<div>` element number 3, then in this the third one, the second one and then all `<div>` elements (which if you count down our list, results in exactly where you are right now.
12. However, we’d like to have the data separated out.
13. To do this use the columns part of the scraper console...
14. Let’s find our title first - look at the title using Inspect Element
![image](http://farm9.staticflickr.com/8355/8263441157_b4672d01b2_o_d.png)
15. See how the title is within a \<b\> tag? Let’s add the tag to our xpath.
16. The expression seems to work well: let’s make this our first column
17. In the “Columns” section, change the name of the first column to “title”
18. Now let’s add the XPATH for the title to it
19. The xpaths in the columns section are relative, that means “./b” will select the \<b\> element
20. add “./b” to the xpath for the title column and click “scrape”
![image](http://farm9.staticflickr.com/8357/8263441315_42d6a8745d_o_d.png)
21. See how you only get titles?
22. Now let’s continue for year? Years are within one \<span\>
23. Create a new column by clicking on the small plus next to your “title” column
24. Now create the “year” column with xpath “./span”
![image](http://farm9.staticflickr.com/8347/8263441355_89f4315a78_o_d.png)
25. Click on scrape and see how the year is added
26. See how easily we got information out of a less structured webpage?

<div class="alert alert-info">Any questions? Got stuck? <a class="btn btn-large btn-info" href="http://ask.schoolofdata.org">Ask School of Data!</a></div>

