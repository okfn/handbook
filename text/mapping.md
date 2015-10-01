---
title: Mapping
---
It's very common for data wranglers to use mapping as a tool. The majority of datasets are in some way related to people and objects in the real world, and if we can figure out their real world location, a latitude and longitude or some other geo-locating property, then we can plot points on a map. This can be a quick and easy way to transform a tabular dataset into a visually compelling display, but mapping doesn't end there. In fact mapping technology, "geo-technology", can let us filter and connect data in powerful ways without even involving a visual map.

Web map mashup
--------------
Although there's more to mapping than showing a map, and showing a map can mean many different things, there is one trick which is very simple, very effective, and essential part of the data wrangler's toolbox. The "web map mashup". Let's dive right in see what this looks like

Create a new file called 'mymap.html', paste the following into it, save and then double-click and open it in a your web browser to see the result.::

```XML
<!DOCTYPE HTML>
<html>
<head>
<title>A web map mashup with OpenLayers and OpenStreetMap</title>

<script src="http://www.openlayers.org/api/OpenLayers.js"></script>
<script>
function init() {
	map = new OpenLayers.Map("mapdiv");
	var mapnik = new OpenLayers.Layer.OSM();
	map.addLayer(mapnik);

	var lonlat = new OpenLayers.LonLat(-1.788, 53.571).transform(
		new OpenLayers.Projection("EPSG:4326"), // transform from WGS 1984
		new OpenLayers.Projection("EPSG:900913") // to Spherical Mercator
	);

	var zoom = 13;

	var markers = new OpenLayers.Layer.Markers( "Markers" );
	map.addLayer(markers);
	markers.addMarker(new OpenLayers.Marker(lonlat));

	map.setCenter(lonlat, zoom);
}
</script>

<style>
#mapdiv {
	width:350px;
	height:250px;
}
div.olControlAttribution {
	bottom:3px;
}
</style>

</head>

<body onload="init();">
	<p>My HTML page with an embedded map</p>
	<div id="mapdiv"></div>
</body>
</html>
```

You should see a map with marker!

**TODO**: screenshot image

This example HTML and javascript makes use of the open source mapping javascript mapping library called 'OpenLayers' and the open licensed maps from [OpenStreetMap.org]().

In the javascript code we see how to initialise a map object which will appear within a div on your HTML page. A LonLat object is created to represent the centre point of the map. Try playing with the latitude, longitude values. A call to `transform` sorts out the projections, and we use this same location to place a marker.



Geo-locations Latitude and Longitude
------------------------------------

**TODO**
