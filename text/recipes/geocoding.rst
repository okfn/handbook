Geocoding Data in a Google Docs Spreadsheet
===========================================

A very common need is to geocode data in a Google Spreadsheet (for example, in creating TimeMaps with the `Timeliner`_ project). There are several options here:

.. _Timeliner: http://timeliner.okfnlabs.org/

By hand – use a Geocoding service (see the `course`_ on geocoding) and then copy and paste by hand.
Use the ImportXML (or ImportCSV) formulae to grab data from a geocoding service – great but with limitations on the number of rows you can code at one time (~50).
Use a Google App Script – the most powerful but requires installation of an App Script in your spreadsheet.
In this tutorial I’m going to cover the latter two automated options and specifically focus on option 2.

.. _course: http://schoolofdata.org/handbook/courses/geocoding/

Using Formulas
All of the following is illustrated live in this `google spreadsheet`_.

.. _google spreadsheet: https://docs.google.com/a/okfn.org/spreadsheet/ccc?key=0AqR8dXc6Ji4JdHBhY25yQkpHWF9NcEt1d3hrU0JWcUE#gid=0

We start with a formula like the following::

  =ImportXML("http://open.mapquestapi.com/nominatim/v1/search?format=xml&q=London", "//place[1]/@lat")

This formula uses the ImportXML function to look up XML data from the `Mapquest Nominatim geocoding service`_ (see the previous tutorial for more about geocoding services). The first argument to ImportXML is the URL to fetch (in this case the results from querying the geocoding service) and the second part is an XPath expression to select data from that returned XML. In this case, the XPath looks up the first place object in the results: place[1] and then gets the lat (latitude) attribute. To understand this more clearly, here’s the XML returned by that XML query:

.. _Mapquest Nominatim geocoding service: http://open.mapquestapi.com/nominatim/

.. image:: http://i.imgur.com/9ZCchXY.png

In reality we want both latitude and longitude, so let’s change it to::

  =ImportXML("http://open.mapquestapi.com/nominatim/v1/search?format=xml&q=London", "//place[1]/@lat | //place[1]/@lon")

This uses an “or” || expression in XPath and the result will now be an array of results that Google Docs will put in 2 cells (one below another). You can see this in Column C of the example spreadsheet.

What happens if we wanted the data in just one cell, with the two values separated by commas, for example? We could use the JOIN function::

  =JOIN(",", ImportXML("http://open.mapquestapi.com/nominatim/vi/search?format=xml&q=London", "//place[1]/@lat | //place[1]/@lon"))

Lastly, we’d like to geocode based on a place name in an another cell in the spreadsheet. To do this we just need to add the place name to our API request to MapQuest’s Nominatim service using the CONCATENATE function (this example assures the value is in cell A2)::

  =ImportXML(CONCATENATE("http://open.mapquestapi.com/nominatim/v1/search?format=xml&q=", A2), "//place[1]/@lat")

  =JOIN(",", ImportXML(CONCATENATE("http://open.mapquestapi.com/nominatim/v1/search?format=xml&q=",A2), "//place[1]/@lat | //place[1]/@lon"))

App Script
----------
If you want an even more powerful approach you can use a Google App Script. In particular, Development Seed’s `MapBox`_ team have prepared a great ready-made Google AppScript that will do geocoding for you.

.. _Mapbox: http://developmentseed.org/

Find the `script plus instructions`_ online.

.. _script plus instructions: https://github.com/mapbox/geo-googledocs
