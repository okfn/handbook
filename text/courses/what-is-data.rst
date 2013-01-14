What is Data?
#############

Introduction
------------
Welcome to the beginners course of the School of Data. In this course we will cover the basics of data wrangling and visualization and will discover and tell a story in a dataset. 


In this module, you will learn where to start looking for data. We begin with an introduction to some of the basics of data – key terms like qualitative, quantitative, machine-readable, discrete and continuous data, which crop up again and again for Data Wranglers. 

Most things start with a question
---------------------------------

Most people don’t just wrangle data for fun. They have a story to tell or a problem to solve. 

Often you will start with a question in mind. This could be anything from: ‘How often does the sun shine in my hometown?’ to ‘How does my government spend its money? And where do they get it from?’. A question is a good starting point for exploring your data - it makes you focused and helps you to detect interesting patterns in the data. Understanding for whom your question is interesting will also help you to define the audience you need to work for, and will help you to shape your story.  

What if you start without a question? You’re just exploring. If you find something that looks interesting in your dataset, you can start examining it as if this was the question you had in mind. Sometimes patterns in data can be explained by investigating what causes the patterns. This is often a story worth telling. 

Whether you began with a question or not, you should always keep your eyes open for unexpected patterns, unusual results, or anything that surprises you. Often, the most interesting stories aren’t the ones you were looking for.

In this course we will start with a question and then explore a dataset with this question in mind. We will also roam around and explore whether there is something interesting hidden in the data.

The question for these tutorials will be: How does healthcare spending influence life expectancy? 

**Task:** Think of a question you would like to answer using data.

What is Data?
-------------
Data is all around us. But what exactly is it? Data is a value assigned to a thing. Take for example the balls in the picture below. 

.. figure:: http://farm9.staticflickr.com/8301/7871270682_ded37461a0_o_d.jpg
  :alt: Golf balls

  Golf balls at a market (CC) by Kaptain Kobold on Flickr.

What can we say about these? They are golf balls, right? So one of the first data points we have is that they are used for golf. Golf is a category of sport, so this helps us to put the ball in a taxonomy. But there is more to them. We have the color: “white”, the condition “used”. They all have a size, there is a certain number of them and they probably have some monetary value, and so on. 

Even unremarkable objects have a lot of data attached to them. You too: you have a name (most people have given and family names) a date of birth, weight, height, nationality etc. All these things are data. 

In the example above, we can already see that there are different types of data. The two major categories are qualitative and quantitative data. 

:term:`Qualitative data` is everything that refers to the quality of something: The color, the texture, the feel, a description of experiences, and interview are all qualitative data.

:term:`Quantitative data` is data that refers to a number. E.g. the number of golf balls, the size, the price, a score on a test etc. 

However there are also other categories that you will most likely encounter:

:term:`Categorical data` puts the item you are describing into a category: In our example the condition “used” would be categorical (with categories such as “new”, “used” ,”broken” etc.)


:term:`Discrete data` is numerical data that has gaps in it: e.g. the count of golf balls. There can only be whole numbers of golf ball (there is no such thing as 0.3 golf balls). Other examples are scores in tests (where you receive e.g. 7/10) or shoe sizes.


:term:`Continuous data` is numerical data with a continuous range: e.g. size of the golfballs can be any value (e.q. 10.53mm or 10.54mm but also 10.536mm), or the size of your foot (as opposed to your shoe size, which is discrete): In continuous data, all values are possible with no gaps in between. 


**Task:** Take the example of golf balls: can you find data of all different categories? 


From Data to Information to Knowledge.
--------------------------------------

Data, when collected and structured suddenly becomes a lot more useful. Let’s do this in the table below.

================  ============
Color             White
Category          Sport - Golf
Condition         Used
Diameter          43mm 
Price (per ball)  $0.5 (AUD)
================  ============

But each of the data values is still rather meaningless by itself. To create information out of data, we need to interpret that data. 

Let’s take the size: A diameter of 43mm doesn’t tell us much. It is only meaningful when we compare it to other things. In sports there are often size regulations for equipment. The minimum size for a competition golf ball is 42.67mm. Good, we can use that golf ball in a competition. This is information. But it still is not knowledge. Knowledge is created when the information is learned, applied and understood. 

Unstructured vs. Structured data
--------------------------------
A plain sentence - “we have 5 white used golf balls with a diameter of 43mm at 50 cents each” - might be easy to understand, but for a computer this is hard to understand. The above sentence is what we call unstructured data. Unstructured has no fixed underlying structure - the sentence could easily be changed and it’s not clear which word refers to what exactly. A table such as the one we did above would be more structured. 

Computers are inherently different from humans. It can be exceptionally hard to make computers extract information from certain sources. Some tasks that humans find easy are still difficult to automate with computers. For example, interpreting text that is presented as an image is still a challenge for a computer (have you ever signed up to a website and had to type some words which were presented to you as an image? This is because it’s so hard for computers to do so and so easy for you - proving that you’re not a machine). If you want your computer to process and analyse your data, it has to be able to read and process the data. This means it needs to be structured and in a machine-readable form.

One of the most commonly used formats for exchanging data is CSV. CSV
stands for comma separated values. The same thing expressed as CSV can look
something like::

  “quantity”, “color”, “condition”, “item”, “category”, “diameter (mm)”, “price per unit (AUD)”
  5,”white”,”used”,”ball”,”golf”,43,0.5

This is way simpler for your computer to understand and can be read directly by spreadsheet software. Note that words have quotes around them: This distinguishes them as text (string values in computer speak) - whereas numbers do not have quotes. It is worth mentioning that there are many more formats out there that are structured and machine readable. 

**Task:** Think of the last book you read. What data is connected to it and how would you make it structured data?


Summary
-------
In this tutorial we explored some of the essential concepts that crop up again and again in discussions of data. What discussed what data is, and how it is structured. In the next Tutorial we will look at data sources and how to get hold of data.

Extra Reading
-------------


1. When you get a new dataset, should you dive in / should you have a hypothesis ready to go? Caelainn Barr, an award winning journalist explains how she approaches new data sources. http://datajournalismhandbook.org/1.0/en/understanding_data_4.html
2. Overview of `common file formats`_ in the open data handbook.

Quiz
----

Take the following quiz to check whether you understood basic data
categories.

.. raw:: html
   
   <iframe 
   src="https://testmoz.com/109467"
   width="100%" height="750" frameborder="0" marginheight="0"
   marginwidth="0">Loading...</iframe><br/><br/>

.. raw:: html

  <a href="../finding-data/" class="btn btn-primary btn-large">Next
  Course<span class="icon-arrow-right"></span></a>

.. _common file formats: http://opendatahandbook.org/en/appendices/file-formats.html
