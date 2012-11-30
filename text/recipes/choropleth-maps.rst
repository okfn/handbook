Creating a Choropleth Map
=========================
.. sectionauthor:: Michael Bauer (@mihi_tr on twitter)

Choropleth maps are a common kind of map. In this type of map a region is
colored according to a value. They are fairly simple to create. In this
recipe we will create a html/javascript based choropleth map from worldbank
data. The HTML and JavaScript used for this example can be found in
`github`_.


Downloading the necessary JavaScript libraries
-----------------------------------------------

In this example we will use `jvectormap`_ to create our choropleth maps.
The interface for creating these maps is very simple and versatile. You
will need the following JavaScript libraries

* Jvectormap from http://jvectormap.com
* Jquery from http://jquery.com
* The Jvectormap world map from: http://jvectormap.com/maps/world/world/

Creating the basic HTML site
----------------------------

Once you've downloaded the necessary JavaScript files, create the basic
HTML site for your map. It should include all the JavaScript libraries in
the header. It'll look something like::

   <!DOCTYPE html>
        <html>
            <head>
                <title>A Choropleth Map</title>
                <script src="jquery-1.8.1.min.js"></script>
                <script src="jquery-jvectormap-1.0.min.js"></script>
                <script src="jquery-jvectormap-world-mill-en.js"></script>
                <link rel="stylesheet" href="jquery-jvectormap-1.0.css" type="text/css" />
            </head>
            <body>
                <div id="worldmap" style="width: 600px; height: 600px;"></div>
            </body>
        </html>
 
Initializing the map
--------------------

Let's create some JavaScript code to initialize the map. 
You can either put this in a ``<script>`` tag in the HTML or create a
standalone file. I prefer to do the latter. This would be the very basic
code to initialize the map::

    function init() {
        $("#worldmap").vectorMap({map:'world_mill_en'});
        }

    $(document).ready(init);    
    

Include the script you just created after all the scripts in the header
have been loaded.

Displaying data
---------------

The map we just created still has no values associated to the countries.
Jvectormap adds values as so called "series". the series we want to create
is a region series. So let's extend our JavaScript file. First let's create
some data. A series consists of a JavaScript object where 2 letter country
codes are the key and the value is the value for displaying. e.g. this
could be::
    
    var data={"GB":20, "IN":11, "CN":17, "US":9, "AU":25};

Add this on top of your ``init()`` function and change the map
initialization code to::
    
    $("#worldmap").vectorMap({map:'world_mill_en',
            series: {regions:[{ values: data }]}
            });

Now you will see some countries have become colored based on the value. 

Getting more data
-----------------

Now let's get some more data. Usually you don't want to write the data
into the file like we did before - you want to have it from a source that
might be changing. The best way to do this is to query an API that provides
data in json format. Many contemporary APIs do so. Let's try this with some
data from the `net neutrality map`_. The data of the project lives freely
available on http://netneutralitymap.org/json/ here the countries.json file
contains information for all the countries. If you look at it it contains
an array of objects, each object has ``cc`` the country code, ``total`` the
number of total tests, ``shaped`` the number of shaped tests and
``percent`` the percentage of shaped tests. Let us display the percentage
of shaped tests. Change your ``init`` function so it looks like this::

  function init() { 
    var data={}; 
    $.getJSON("http://netneutralitymap.org/json/countries.json",function 
    (results) { 
        for (i in results) {
                    var cc=results[i].cc
                    // build the data object for vectorMap
                    data[cc]=results[i].percent+1; 
                }
            console.log(data);
    $("#worldmap").vectorMap({map:'world_mill_en',
           series: {regions:[ {
               values: data}]}
               });

                });
    }

Notice the percent+1? This is necessary because vectorMap does not display
countries if the value is 0. Now look at your HTML page: The map should be
nicely colored with darker blue colors as higher values and lighter blue
colors as lower values. 

Color scale
----------

We have one color scale selected here. This is a mono-hue color scale: all
blue and just the lightness changes. If you want to switch to a different
color scale, you can do this in your definition for series::
    
    series: {regions:[ {
        values: data,
        scale: ["#EEEEEE","#000000"]
    }]}

The above code changes to a Grey scale color code. You can add multiple
intermediate steps if needed. You can see the finished result as a github
page here: http://mihi-tr.github.com/example-choropleth-map/



.. _github: https://github.com/mihi-tr/example-choropleth-map
.. _jvectormap: http://jvectormap.com
.. _worldbank provides an API: http://data.worldbank.org/developers
.. _net neutrality map: http://netneutralitymap.org
