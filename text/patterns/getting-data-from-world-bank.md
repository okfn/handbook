Getting data from the World Bank
================================

In Data Fundamental, we address the question of how healthcare spending affects life expectancy around the world. This is one of the answers we can find looking at data from the World Bank.

Walkthrough: Downloading Data from the World Bank
-------------------------------------------------

1. Open the World Bank data portal: it lives in [http://data.WorldBank.org](http://data.WorldBank.org)
2. Select `Data Catalog` from the menu on the top.
![image](http://farm9.staticflickr.com/8180/8051105884_f23e200bae_o_d.jpg)
3. In the long list on the bottom find “World Development Indicators”
4. Click on the blue `databank` button next to it.
![image](http://farm9.staticflickr.com/8454/8051105990_7a7467bf79_o_d.png)
5. You’ll find a very different site: The Databank - The databank is an interface to the World Bank database. You can select what data you want to see from which countries for what period of time.
6. First select the countries. We’re interested in all the countries click on `select all` in the country view and then on `next`
![image](http://farm9.staticflickr.com/8181/8051106310_86ffe90bdc_b_d.jpg)
7. Now you’ll see a long list of data series you can export. We’ll need a few of them.
8. First we are interested in healthcare expenditure so type “Health” in the little search box on the top of the list and click `Go`
9. Select “Health expenditure, private (% GDP)”, “Health expenditure, public (% GDP)” and “Health expenditure, total (% GDP)”. And click on `Select`
![image](http://farm9.staticflickr.com/8033/8051099651_aeec6d8ec3_b_d.jpg)
10. Since the expenditure is in % of GDP we’ll need to get the GDP as well. Since we want to compare countries directly we’ll need GDP in US\$. To do this type GDP into the search box and find the entry “GDP (current US\$)” 
11. If we want to see how healthcare expenditure affects the life expectancy we need to add life expectancy to the data.
12. Now let’s add one more thing: Population - like this we can calculate how much is spent by and on an average person. Search for “Population” and select “Population, total”.
13. Bring GDP and Population to the top with the arrows on the side of the list, your selection should now look like this:
![image](http://farm9.staticflickr.com/8451/8051099565_9274f466e7_b_d.jpg)
14. Click on `Next` to select the years we are interested in.
15. To keep things simple, select the years 2000-2012 (you can do multiple selections by either pressing `ctrl` or `shift`). And click `next`,
16. You’ll see an overview screen now on the top left there is a rough layout of how your downloaded file will look like. You’ll see “time” in the columns bit and “series” in the rows bit - this influences how the spreadsheet will look like.
![image](http://farm9.staticflickr.com/8462/8051106168_62d3a4032a_o_d.png)
17. While this might be great for some people: The data is a lot easier to handle if all of our “series” are in columns and the years are different rows. So let’s change this.
18. Simply drag the “time” from columns to “rows” and the “series” from rows to columns
19. Your arranged organization diagram should look like this:
![image](http://farm9.staticflickr.com/8317/8051099813_f707789d17_o_d.png)
20. Now let’s go and `Export`
21. If you click on the `Export` button a pop up will appear asking you for the format. Select `CSV`.
22. You will then be able to download a file - store and name it in a folder so you remember where it comes from and what it is for.

<div class="alert alert-info">Any questions? Got stuck? <a class="btn btn-large btn-info" href="http://ask.schoolofdata.org">Ask School of Data!</a></div>

