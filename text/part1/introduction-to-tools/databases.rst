Databases
*********
.. sectionauthor:: @vruba at the Portland sprint

From `databases outline`_ Created by @vruba at the Portland sprint

stuff that’s written as running text is really an outline: it’s describing
points that are essential to cover.

I am not aiming for strict accuracy. This is a guide, not an advanced textbook. Some half-truths are asserted and some technical terms are abused.

Relational
=====================

Concepts
--------
Relational databases are what most tech people mean most of the time when they say “database”. They are essentially always used with some version of the SQL family of query languages (pronounced either “es kew el” or “sequel”). Popular relational databases include MySQL, PostgreSQL, MS SQL, Oracle, and SQLite.

A given database is a collection of tables. Each table is basically a spreadsheet [emphasize this: almost everyone “gets” spreadsheets]: a collection of data rows that fit into some column definitions. A table of bus stops might look like this:

=========== ============ ======== =========
stop_number address      latitude longitude
=========== ============ ======== =========
809         300 Elm St   22.9232  130.3413
957         902 MLK Blvd 22.941   130.339
=========== ============ ======== ========= 

And so on. To record which busses come by a given stop, you might assume we
would have a column called bus_lines that’s a list of bus lines. In fact,
lists are generally bad form in relational databases [underlying
concept/sidebar/further reading: database normalization]. To express this
kind of data, we would instead make another table that looks something like
this:

===================== ========
bus_line              stops_at
===================== ========
#45                   809
#45                   810
#45                   957
#12 Commuter Express  271
===================== ========

And so on. [Joins.]

Querying a database
-------------------

[Mention SQL security and escaping so people don’t go out and write public
web apps that send query strings straight to their RDBMSes.]

Setting up a database
---------------------

.. this example is great- I would use sqlite though - it's remarkably
   easier to install 
Here’s what it looks like when I set up a database from the command line.
I’m using postgres, which I have already installed and running on my
computer, and there’s a user with my login name (char)::

    $ psql                 #This is the interactive PostgreSQL command-line client.
    psql (9.1.4)
    Type "help" for help.
    char=#         #It’s connected me to the database matching my login name.
    char=# create database busses with owner char;
    CREATE DATABASE
    char=# \c busses        #Connect to the database I just created.
    busses=# create table bus_stops (
    busses(#   stop_number integer primary key,
    busses(#   address text,
    busses(#   latitude float,
    busses(#   longitude float
    busses(# );
    NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index "bus_stops_pkey" for table "bus_stops"
    CREATE TABLE
    busses=# select * from bus_stops;
     stop_number | address | latitude | longitude 
    -------------+---------+----------+-----------
    (0 rows)
    
    busses=# 
    busses=# insert into bus_stops values (809, '300 Elm St', 22.9232, 130.3413);
    INSERT 0 1
    
Primary keys. References.

Case study
----------

Find, load, and run interesting queries against some appropriate data.

noSQL
=====

Concepts
--------

noSQL databases are a newly popular way of dealing with the kind of large, loosely structured data that multiuser platforms (like yadda yadda) tend to produce. Although in principle anything that can be done in a relational database can be done with a non-relational one and vice versa, noSQL tends to be more popular where data is more irregular and free-form. (There are also a lot of advantages and disadvantages to do with things like efficiency and ACID that are outside our scope here.) Popular noSQL databases include CouchDB and MongoDB.

Mini-tutorial
-------------

[Since noSQL doesn’t require schemas up front, I think it makes sense to merge the setup and querying.]

Case study
----------

Lots of JSON data out there would work for this.

.. _databases outline: https://docs.google.com/document/d/1TrCuVla9cSdaWx8_vzeuS_gGQDYIuewRXJOq9cXFFf4/edit
