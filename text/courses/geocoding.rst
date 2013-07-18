Geocoding is the conversion of a human-readable location name into a numeric (or other machine-processable) location such as a longitude and latitude. For example:

    London => [geocoding] => {latitude: -0.81, longitude: 51.745}

Geocoding is a common need when working with data as you may only have human-readable locations (e.g. "London" or a zip code like "12245") but for a computer to display the data on a map or query it requires one to have actual numerical geographical coordinates.

*Aside: in the example just given we've the term "London" has been converted to a point with a single Latitude and Longitude. Of course, London (the City in the UK) covers a significant area and so a polygon would be a better representation. However, for most purposes a single point is all we need.*

Online geocoding
----------------

In theory, to do geocoding we just need a database that lists place names and their corresponding coordinates. Several, such `open databases`_ exist including `geonames`_ and `OpenStreetMap`_.

.. _open databases: http://opendefinition.org
.. _geonames: http://geonames.org/
.. _OpenStreetMap: http://openstreetmap.org/


However, we don't want to have to do the lookups ourselves - that would either involve programming or a lot of very tedious scrolling.

As a result, various web services have been built which allow look ups online or over a `web API`_. These services also assist in find the *best match* for a given name -- for a given simple place name such as London there may be several matching locations (e.g. London, UK and London, Ontario) and one needs some way to match and rank these alternatives.

.. _web API: http://schoolofdata.org/handbook/appendix/glossary/#term-web-api

Nominatim - An Open Geocoding Service
-------------------------------------

There are a variety of Geocoding services. We recommend using one based on **open data** such as the `MapQuest Nominatim`_ service which uses the `Open Street Map`_ database. This service provides both "human-readable" service (HTML) and a "machine-readable" API (JSON and XML) for automated Geocoding.

.. _MapQuest Nominatim: http://open.mapquestapi.com/nominatim/v1/

Geocoding - The challenge
--------------------

Right, so now it's time to get your hands dirty.

a) Pick a dataset with locations you would like to geocode
b) Follow the `recipe`_ in the handbook to show you how to geolocate.
c) If you like - go one step further and put your data on a map. There are lots of great services available to do this, `Tilemill`_ by Mapbox is very elegant, allowing you to customise your map to your house style - the documentation is also very clear and accessible, `Google Fusion Tables`_ also allows you to easily plot points on a map and is a popular choice with many data journalists for it's ease of getting started.

.. _recipe: http://schoolofdata.org/handbook/recipes/geocoding/
.. _Tilemill: http://mapbox.com/tilemill/
.. _Google Fusion Tables: http://support.google.com/fusiontables/answer/2571232?hl=en

Once you've finished - drop us a link to what you have produced in the comments below - that could just be a full geocoded dataset - or a beautiful map, go as far as you need!


Example - `Human-readable HTML`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. image:: http://i.imgur.com/zCpzg8a.jpg

.. _Human Readable: http://open.mapquestapi.com/nominatim/v1/?q=London

Example - `Machine-readable JSON`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(JSON is also human-readable if you have a `plugin`_)

  .. image:: http://i.imgur.com/SjoQuYP.png

.. _Machine-readable JSON : http://open.mapquestapi.com/nominatim/v1/?format=json&q=London
.. _plugin: http://schoolofdata.org/handbook/appendix/glossary/#term-json
.. raw:: html

  <div class="alert alert-info">Any questions? Got stuck? <a class="btn
  btn-large btn-info" href="http://ask.schoolofdata.org">Ask School of Data!
  </a></div>
