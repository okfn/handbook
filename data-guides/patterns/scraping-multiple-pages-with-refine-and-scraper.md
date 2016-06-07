---
title: Scraping multiple Pages using the Scraper Extension and Refine
---

Many times you’ll not have one single page to scrape. For example the Chilean Government has a very nice [transparency site](http://www.gobiernotransparentechile.cl/directorio/entidad) and offers the income statistics for many departments - let’s get them all!

To complete this recipe you’ll need:

1. The [Scraper Extension for Chrome]((https://chrome.google.com/webstore/detail/scraper/mbigbapnjcgaffohmbkdlecaccepngjd?hl=en)
2. A Google Account
3. [Refine](http://openrefine.org)
4. If you haven't yet: Look at the Recipe [Scraping websites using the Scraper Extension](http://schoolofdata.org/handbook/recipes/scraper-extension-for-chrome/)

To extract information out of multiple web-pages we’ll use a two step procedure: First we’ll get all the URLs for the web-pages with the scraper extension, then we will extract the Information out of these web-pages using Refine. To do this effectively, we rely on all the web-pages to be generated with similar structure. As you’ll see in this Recipe, it is not always the case.

Walkthrough: Getting a list of URLs with scraper extension
----------------------------------------------------------

1. Open [<http://www.gobiernotransparentechile.cl/directorio/entidad>](http://www.gobiernotransparentechile.cl/directorio/entidad) - the list of government departments in Chile.
2. Mark one department, right click and select `scrape similar...` as in [Scraping websites using the Scraper Extension](http://schoolofdata.org/handbook/recipes/scraper-extension-for-chrome/)
3. Depending on your selection you might have slightly different results.
4. Now pay attention to the left side of the scraper console - on the top you’ll see a text entry saying XPATH
![image](http://farm6.staticflickr.com/5532/9292783948_4886366d07_o_d.png)
5. The XPATH tells the computer where to find things. The text refers to html tags in the page - let’s modify this to make it work nicely for the page: First remove the [1] behind the second div. This will give you all the texts on the page.
6. Now let’s extract the links from the page. Go back to the page and “inspect” one of the links
![image](http://farm8.staticflickr.com/7446/9292783960_e180a05f1b_b_d.jpg)
7. See how the links are within an `<a>` element underneath the `<li>` element? Let’s add this to our xpath.
![image](http://farm4.staticflickr.com/3683/9290007049_490a8d3b2c_o_d.png)
8. We have a column now with the names - if you look closely in the inspected element the \<a\> tag has two attributes: class and href.
Href is the URL and class says something about the category the link belongs to. Let’s extract both.
9. To do so we’ll add more columns to the column list on the second page, do so by clicking the green + next to the one existing column
10. The scraper console wants two things: An Xpath and a name: enter `./@href` to the xpath and URL as a name
![image](http://farm8.staticflickr.com/7339/9290007057_9d7ef76e7e_o_d.png)
11. Now let’s do the same for the class. Enter ./@class and Class
![image](http://farm4.staticflickr.com/3820/9292784000_e861d194e9_o_d.png)
12. Perfect - click on Scrape (or press enter) to see how your list will look like. Nice isn’t it?
13. Now save it to google docs.

Once we have the list of URLs let’s go to Refine to scrape the salary pages we can find easily.

Walkthrough: Scraping multiple pages using Refine
-------------------------------------------------

1.  Download the Spreadsheet as CSV from google spreadsheets
2.  Open Refine - it will open a browser window at `http://127.0.0.1:3333`
3. Now select Create Project and this Computer
4. Click on Choose Files and select the file you just downloaded.
5. Click Next - this will open the Preview in Refine
![image](http://farm4.staticflickr.com/3728/9292784110_d46ec1f9a7_b_d.jpg)
6. Refine should parse the file correctly - name your project on the top right and click Create Project
7. If the special characters in the file look garbled - select UTF-8 as a Character Encoding.
8. You’ll see the data view of Refine. It looks very much like a spreadsheet - and works quite similar.
9. Let’s clean our data and only get the links we’re interested in - the secondary category links
10. Create a filter for the Class column: click on the small triangle next to the column and select Facet -\> Text Facet
![image](http://farm4.staticflickr.com/3762/9290007199_6c34392969_o_d.png)
11. This will open a Facet window in the left column that displays all the unique values found within the Class column, along with a count of how many times each of them appear in the column.
![image](http://farm6.staticflickr.com/5488/9290007183_e13832f56c_o_d.png)
12. Let’s remove everything but secondaryCat. Select secondaryCat in the filter and then click on the small invert label on the top right of the facet.
13. Now let’s remove the rows that are not secondaryCat - for this select the options in the All column and select edit rows - remove all matching rows
![image](http://farm3.staticflickr.com/2835/9292784184_e879b099df_o_d.png)
14. Perfect - now we can delete the Class Column, since we’re not going to use it anymore.
15. Do this with the Edit columns -\> re-order/remove columns options in the All menu
16. Now let’s scrape the pages. If you look at the page structure, the salary information is often in: `/per_planta/Ao-2013` relative to the URL we scraped with the scraper extension.
17. Let’s import the pages - do so by selecting the options of the URL column, and edit column -\> add column by fetching URLs
![image](http://farm6.staticflickr.com/5462/9290007265_a26a484e3e_o_d.png)
18. This will open an add column menu. We have to transform our cells so that we get the url we want to be fetching.
19. Let’s write our first expression in Refine: we want to append `/per_planta/Ao-2013` to each url, so our expression will be `value+/per_planta/Ao-2013\` - this appends to the value in the current row.
![image](http://farm8.staticflickr.com/7303/9292784300_7ba3ae6970_o_d.png)
20. The throttle delay sets the rate at which OpenRefine will request the pages from the webserver they live on. If we try to grab too many pages in a short period of time, the server may lock us out.
Requesting 1 or 2 pages a second (throttle delay of 1000 or 500 milliseconds) should be okay in this case. Just be respectful:-). We also need to give the column we’re creating for the scraped data a name - put Page into the column name.
21. click OK - refine will now download the webpages and give you a progress indicator, how it is doing. If you multiply the throttle delay by the number of rows in your dataset, you should get an estimate of the amount of time the download is likely to take.
22. Wooha, this quickly filled our document with HTML code - don’t be intimidated you don’t need to understand or read it - the computer will do this for you.
23. Now let’s first remove all the rows that didn’t get a page (because there is none...) (we could also go and investigate and see whether there’s information we missed - but for the sake of simplicity let’s just delete them).
24. Create a text facet on the Page column, select blank and remove all matching rows as we’ve done above.
25. Close the text facet again to continue working, Now let’s extract the table rows out of each page. Do so by selecting the options of the Page column and edit column -\> add column based on this column
26. Name the new column Rows
27. The expression for this is slightly more complicated: first we tell refine that this is an html document we do so by starting with `value.parseHtml()`.
28. Then we append `.select("table")[0]` - this will select the first table from it - see how the content in the new column changes?
29. Now we select all the rows in this column with `.select(tr)` - remember tr is the tag for the rows...
30. This will result in a list of rows - however refine can’t really handle lists. So we have to join the list - so we append `.join("|")` to join the list with a pipe character -- the vertical line. (I choose this character because it usually doesn’t appear in the text).
31. Your expression should now look like this:
![image](http://farm4.staticflickr.com/3770/9292784338_cdf6535bfe_o_d.png)
32. It looks complicated but is actually very simple - it’s just a row of commands - similar to spreadsheet formulas. If you struggle understanding it: Try to read it from the beginning (go back a couple of steps and try to see how the commands are chained together).
33. click OK to fill the Rows column.
34. Now remove the blank rows again as we did before.
35. Let’s split the Rows into actual Rows in refine
36. Select Edit Cells -\> Split multi-valued cells from the Rows menu
![image](http://farm6.staticflickr.com/5525/9292784364_d383666794_o_d.png)
37. A menu will pop up asking us for what kind of character we want to split at: we want to split at |
38. Now let’s extract the data cells in each row. We do this by edit column -\> add column based on this column like we did above.
39. Well do value.parseHtml() again - to tell refine this is HTML. Then we .select("td") to select the data cells and we’ll join them again with the | character. The expression should look like this:
![image](http://farm4.staticflickr.com/3775/9292784354_b269c3216b_o_d.png)
40. Click OK - you’ll notice now we have quite a bit of blank cells - before we remove them we have to make sure we have the department name with each row. - for this switch back to the column saying Text - this is the department names.
41. Select Edit cells -\> fill down from the options menu.
42. This will put the thing it finds in the row into each subsequent empty row until it does find a new filled row.
43. Now you can delete the blank rows.
44. So let’s go back and get the table data out. First we’ll strip the HTML tags from the text, since we don’t need them anymore.
45. We can do so by transforming the cell:
46. Select edit cells -\> transform from the options of the Data column.
47. We want to replace anything between pointy brackets with nothing: the expression for this is `value.replace(/\\\<.\*?\\\>/,"")`
![image](http://farm6.staticflickr.com/5333/9290007389_5d4d6e153d_o_d.png)
48. This has removed the HTML tags. If you look at the data: there is a further problem. A lot of the text has things like &Ntilde; we can parse this automatically
49. Select edit cells -\> common transforms -\> unescape HTML entities from the options of the Data column - now let’s split the data in this column into multiple columns
50. For this choose edit column -\> split into multiple columns and add the | character as the split character for the columns.
51. Now let’s look at what we’ve got: we have multiple columns with the data as presented in the table
52. One of the columns contains the amount - as you can see: it’s not always a number: The multiple . make refine think it’s not a number: let’s fix this: we’re transform the column
53. The expression for this is `value.replace(".","").toNumber()`
![image](http://farm4.staticflickr.com/3746/9290007969_6f23c84a2e_o_d.png)
54. Wonderful - There is still some things wrong: e.g. the special spanish characters don’t translate well - now you know how to use the replace function to replace them.
55. The last thing we do is remove the columns we don’t need anymore: URL , Page and Row
56. Congratulations you’ve scraped and cleaned up a large dataset from several pages on the web.

<div class="alert alert-info">Any questions? Got stuck? <a class="btn btn-large btn-info" href="http://ask.schoolofdata.org">Ask School of Data!</a></div>

