=================================
Categorization and reference data
=================================

Adapted from the `Spending Data Handbook`_.

.. _Spending Data Handbook: 

One of the most powerful ways of making data more meaningful for analysis is to combine it with reference data and code sheets. Unlike transaction data - such as statistical time series or budget figures - reference data does not describe observations about reality - it merely contains additional details on category schemes, government programmes, persons, companies or geographies mentioned in the data.

For example, in the German federal budget, each line item is identified through an eleven-digit code. This code includes three-digit identifiers for the functional and economic purpose of the allocation. By extending the budget data with the titles and descriptions of each economic and functional taxonomy entry, two additional dimensions become available that enable queries such as the overall pension commitments of the government, or the sum of all programmes with defence functions.

The main groups of reference data that are used with government finance include code sheets, geographic identifiers and identifiers for companies and other organizations:

Classification reference data
==============================
Reference data are dictionaries for the categorizations included in a financial datasets. They may include descriptions of government programmes, economic, functional or institutional classification schemes, charts of account and many other types of schemes used to classify and allocate expenditure.

Some such schemes are also standardized beyond individual countries, such as the UN's classification of functions of government (COFOG - http://unstats.un.org/unsd/cr/registry/regcst.asp?Cl=4) and the OECD DAC Sector codes (http://www.oecd.org/dac/aidstatistics/dacandcrscodelists.htm). Still, the large majority of governments use their own code sheets to allocate and classify expenditure. In such cases, it is often advisable to request access to the code list versions used internally by government, including revisions over time that may have changed how certain programmes were classified.

A library of reference data that can be re-used across different projects and it is a valuable asset for any organization working with government finance. Sharing such data with others is crucial, as it will help to enable comparable outputs and open up options for future data integration. Existing repositories include the IATI Standard (http://iatistandard.org/) and datahub.io.

Geographic identifiers
======================
Geographic identifiers are used to describe administrative boundaries or specific locations identified in a dataset. While some regional classifications (such as the `EU NUTS`_) are released on the web, there is also an increasing number of open databases which contain geographic names - including geonames.org and the recently developed `world.db`_.

.. _EU NUTS: http://epp.eurostat.ec.europa.eu/portal/page/portal/nuts_nomenclature/introduction
.. _world.db: https://code.google.com/p/worlddb/

Another related technique is the process of reverse geo-coding: translating a human-readable address into a pair of coordinates. Services like nominatim (http://nominatim.openstreetmap.org/) will not only enable users to generate precise maps of projects in a region, they will also return the responsible administrative boundary for many coordinates. This means that projects which are given by precise address can also be aggregated by state, region or any other geographic unit.

Additionally, many countries have `shapefiles`_ of their political and geographic districts available (usually through the census or interior bureaus) that can be imported into custom mapping applications, like TileMill (http://mapbox.com/tilemill/).

.. _shapefiles: http://en.wikipedia.org/wiki/Shapefile

Company and organisational identifiers
======================================

As you look into spending data that includes recipients outside the government, you'll find companies which act as suppliers to government, but also other types of entities including charities, associations, foreign governments, political parties and even individuals which act as recipients of direct assistance.

Identifying such entities is notoriously hard, since the only information kept by government is often a simple name (which may not uniquely identify the beneficiary, for example "MS"). While most (if not all) countries maintain company registers which assign some type of unique identifier to a company, these databases are often not accessible in bulk and not used coherently across different parts of government. Alternative identifiers - such as tax identifiers and company IDs from private business information suppliers (such as Dun & Bradstreet in the US) - further complicate this process.

As an alternative, open registries are beginning to compile organisational identifiers in a form that is easy to re-use and thus enables the sharing of databases which have been augmented with such information. OpenCorporates.com (http://opencorporates.com) is a startup that collects information from companies world-wide and provides a convenient API to match datasets with the list of known countries. They offer a service to 'reconcile' companies to link information about a company to a company name. This is especially useful when you have an exist spreadsheet or dataset featuring lots of companies. Matching (or reconciling) to legal entities allows you to get more information about the companies (for example the registered address or statutory filings), and makes it easier to match with other datasets or exchange with other organisations.  

The IATI project for aid transparency is working towards similar standards for other organisations, such as foreign governments and charities active in the development space.

.. raw:: html
  
  <div class="well">

**Tasks** 

#. Find out - does your country use a standard classification for its data such as COFOG?
#. If you have code sheets for your data - try combining them with your main dataset. Take the `merging data course`_  if you need a hand. 
#. If relevant: Try geocoding your data. For example - does your data include particular projects? Can you find an address for them? If so, you can geocode them and put them on a map! Take a look at the `geocoding`_ course if you need more help. 
#. If you have spending data, try to answer the question "how much did company X receive from government". You may need to correct typos and find out answers to questions such as "is company X" the same thing as "company X Ltd" (this is why having organisational identifiers is so important!)? If there is `company data for your country`_, use the OpenCorporates reconciliation service to find out more information about the company (on the right hand side of the page on OpenCorporates.com). 

.. _merging data course: http://schoolofdata.org/handbook/courses/merging-data
.. _geocoding: http://schoolofdata.org/handbook/courses/geocoding
.. _company data for your country: http://opencorporates.com/

.. raw:: html
  
  </div>



