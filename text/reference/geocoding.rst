===============================
Geocoding / Georeferencing Data
===============================

Geocoding is the conversion of a human-readable location name into a numeric (or other machine-processable) location such as a longitude and latitude. For example::

  London
  
  [geocoding] =>

  {
    lat: -0.81,
    lon: 51.745
  }

By Hand
=======

There are a variety of Geo-coding services. We recommend using one based on **open data** such as the Mapquest Nominatim service which uses the Open Street Map Nominatim database:

http://open.mapquestapi.com/nominatim/v1/

Geo-Googledocs
==============

* Google docs app script allowing you to do the following with your google docs
  spreadsheet:

  * Export to :term:`GeoJSON`
  * :term:`Geocode` arbitrary addresses

* Code: https://github.com/mapbox/geo-googledocs
* Docs: http://developmentseed.org/blog/2011/10/12/mapping-google-doc-spreadsheet/
* Author: MapBox (DevelopmentSeed)

