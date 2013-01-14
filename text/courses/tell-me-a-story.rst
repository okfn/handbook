Tell me a story: Working out what's interesting in your data
============================================================

Introduction
--------------
Data alone is not very accessible. However it is a great fundament to build on. To create information from data it needs to be made tangible. Telling a story with the data is the most straightforward way to do this.

To tell a story with you data you need to figure out certain questions. Why would someone be interested in your story? Who is the someone? How does that someone connect or interact with you data?

The process
--------------
The process of telling a story with data is very similar to this track. It includes

#. Finding Data - find the data that is suitable to answer your question
#. Wrangle the Data - bring it to a format that is useable
#. Merge Datasets - Bring different datasets together
#. Filter and sort the Data - Pick the data that is interesting
#. Analyze Data - Is there something to it
#. Visualize Data - If so: how can we best see it, and show it to others?

Finding a Story in Data
----------------------------
Sometimes you will start out to explore a dataset with a given question in mind. Sometimes you start with a dataset and want to find a story hidden in it. In both cases visualizing the data will be helpful to find the interesting parts. A good way to discover stories is to have interactive visualizations. Live bubble charts are great to do so -since we can compare multiple values at once.

**Walkthrough:** Interactive bubble chart

#. Start with the worldbank dataset.
#. Select all years and all countries (except the names that are definitely not countries: such as world, North America and son on).
#. Copy the data to a new sheet.
#. In order to do animated bubble plots you'll need to order your columns so that is country names, B is year and the rest are values you're interested in. The column order will affect the way the gadget is set up per default.

   .. image:: http://farm9.staticflickr.com/8453/7982243972_2913843fa7_o.png
#. Now mark the whole sheet and click "insert" "gadget"
#. Select "charts" and "motion chart".

   .. image:: http://farm9.staticflickr.com/8463/8112394477_f78ca0eecf_o.png
#. You'll see the chart loading.
#. You can adjust the values for each of the axis and the size. And you can slide through the years.
#. Click on play and see how the world changes in 10 years.

.. raw:: html
  
  <div class="well">

**Task:** Look at life expectancy over total healthcare expenditure per person. Look at Botswana and Swaziland. Do you notice something? What is the story there?

.. raw:: html
  
  </div>

Telling the story
-------------------
Once you're through the steps: How do you frame your data? How do you provide the context needed? What format are you going to chose? It could be an article, a blog post, an infographic, or an interactive website dedicated to just this problem. The formats vary as do the ways to tell your story. So what format you pick also depends on who you are and what you want to tell. Are you with a NGO and want to use the data for a campaign? Are you a journalist and want to use the data with a story? Are you a researcher trying to make sense of a research data? Or just a curious blogger looking for interesting things? You will have different audiences and different means to tell your story. Don't be afraid to share your work with friends and colleagues early - they can give you great insight on how to improve your presentation and story.

.. raw:: html

  <div class="well">

**Task:** What stories can be told from data above and can you identify additional information or data to 
.. raw:: html
  
  </div>

Publishing our results
----------------------
Now let's go ahead and publish our results on a webpage. This will get a bit techy but don't worry we'll guide you through. We will create a small web page containing some of the visualizations we created using a simple online tool called pastehtml. Pastehtml allows you to create html websites easily by simply editing the text online and then saving it for sharing.

**Walkthrough:** Presenting our information as a webpage

#. To start a webpage simply visit pastehtml.com
#. See the input box with all the brackets? This is html code and we'll be editing it to present your results. (If you want to learn more about html code head to the `school of webcraft <https://p2pu.org/en/schools/school-of-webcraft/>`_

   .. image:: http://farm9.staticflickr.com/8470/8112394583_9c6c439893_o.png
#. First let's change the title of the webpage: This is the bit between "<title>" and "</title>". Edit it so it is appropriate. 
#. Then let's go and edit the content for a webpage (this is the part between "<body>" and "</body>"). See the text between "<p>" this defines a paragraph. Go ahead and edit it!
#. You can click on "Publish page" to see how your page will look like (approximately).
#. On the top you'll always have the possibility to go back and edit.

#. Now let's add some charts we made.
#. Go back to one of the charts in the spreadsheet.
#. Click on the chart. See the small triangle top right of the chart: this is the options menu.
#. Go and select "Publish chart\'85".There will be a popup with a lot of code in a grey box:

   .. image:: http://farm9.staticflickr.com/8195/8112418106_fac64f623f_o.png
#. Copy this code and paste it into the pastehtml (somewhere between <body> and </body>). Now if you go and look at your page, the chart should be there.

   .. image:: http://farm9.staticflickr.com/8050/8112418146_72872fde90_o.png
#. Once you are finished, click on publish and you'll get a url to your webpage. use this to share your results with your friends.

Of course if you already have a blog or something similar you can share the results there.

Summary
-----------
Throughout this course we started out acquiring and storing a dataset in a spreadsheet, exploring it and calculating new values, visualizing and finally telling a story about it. Of course there is much more to data than we covered in this basic course. You won't be on your own though the School of Data is here to help. Now go out, look at what others have done and explore data!

.. raw:: html 
 
   <a href="../" class="btn btn-primary btn-large">You've finished Data
   Fundamentals
     <span class="icon-star-empty"></span></a> 

