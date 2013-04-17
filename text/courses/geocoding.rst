Geocoding is the conversion of a human-readable location name into a numeric (or other machine-processable) location such as a longitude and latitude. For example:

    London => [geocoding] => {latitude: -0.81, longitude: 51.745}

Geocoding is a common need when working with data as you may only have human-readable locations (e.g. "London" or a zip code like "12245") but for a computer to display the data on a map or query it requires one to have actual numerical geographical coordinates.

*Aside: in the example just given we've the term "London" has been converted to a point with a single Latitude and Longitude. Of course, London (the City in the UK) covers a significant area and so a polygon would be a better representation. However, for most purposes a single point is all we need.*

Online geocoding
----------------

In theory, to do geocoding we just need a database that lists place names and their corresponding coordinates. Several, such `open databases`_ exist including [geonames](http://geonames.org/) and [Open Street Map][osm].

[osm]: http://openstreetmap.org/

.. _open databases: http://opendefinition.org

However, we don't want to have to do the lookups ourselves - that would either involve programming or a lot of very tedious scrolling.

As a result, various web services have been built which allow look ups online or over a [web API][]. These services also assist in find the *best match* for a given name -- for a given simple place name such as London there may be several matching locations (e.g. London, UK and London, Ontario) and one needs some way to match and rank these alternatives.

[web API]: http://schoolofdata.org/handbook/appendix/glossary/#term-web-api

Nominatim - An Open Geocoding Service
-------------------------------------

There are a variety of Geocoding services. We recommend using one based on **open data** such as the [MapQuest Nominatim][mapquest] service which uses the [Open Street Map][osm] database. This service provides both "human-readable" service (HTML) and a "machine-readable" API (JSON and XML) for automated Geocoding.

[mapquest]: <http://open.mapquestapi.com/nominatim/v1/>

Geocoding - The challenge
--------------------

Right, so now it's time to get your hands dirty.

a) Pick a dataset with locations you would like to geocode
b) Follow the [recipe][georecipe] in the handbook to show you how to geolocate.
c) If you like - go one step further and put your data on a map. There are lots of great services available to do this, [Tilemill][tilemill] by Mapbox is very elegant, allowing you to customise your map to your house style - the documentation is also very clear and accessible, [Google Fusion Tables][fusion] also allows you to easily plot points on a map and is a popular choice with many data journalists for it's ease of getting started.

[georecipe]: <http://schoolofdata.org/2013/02/19/geocoding-part-ii-geocoding-data-in-a-google-docs-spreadsheet/>
[tilemill]: <http://mapbox.com/tilemill/>
[fusion]: <http://support.google.com/fusiontables/answer/2571232?hl=en>

Once you've finished - drop us a link to what you have produced in the comments below - that could just be a full geocoded dataset - or a beautiful map, go as far as you need!


Example - Human-readable HTML
-----------------------------

<http://open.mapquestapi.com/nominatim/v1/?q=London>

<img src="http://i.imgur.com/zCpzg8a.jpg" alt="" />

Example - Machine-readable JSON
-------------------------------

(JSON is also [human-readable if you have a plugin][json-ref])

<http://open.mapquestapi.com/nominatim/v1/?format=json&q=London>

<img src="http://i.imgur.com/SjoQuYP.png" alt="" />

[json-ref]: http://schoolofdata.org/handbook/appendix/glossary/#term-json
