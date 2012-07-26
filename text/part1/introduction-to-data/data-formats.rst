Data Formats
============

CSV: Lingua Data
----------------

People love CSV (Comma-Separated Values) for its simplicity: it stores tables
in plain text files, one row per line with the first row defining column
names. In many ways this is the lingua franca of data. Things become a bit
messy, however, when you realize that very little of the above description 
is ever true in practice: rows can extend across several lines, file headers
are often missing or preceded by some random headings and the flexible format
even invites producers to vary the number of cells per row.


Things that are not true about CSV: 

 * Every row is one line, every line is a row. 
 * The first column contains column headings.
 * All rows have the same number of columns.


Before you process CSV files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is advisable to deal with CSV encoding and quoting issues early 
in your workflow.

If there's a chance that your CSV file contains non-English words, or English
proper names such as surnames or placenames, then you should verify that
the data is in the character set encoding that you expect, e.g., UTF-8 or
ISO-8859-1. Otherwise, convert it to the encoding you work in, using iconv.
GNU iconv is limited to converting files which will fit in the RAM available
on your machine and which contain data in a single character set encoding.

There are multiple methods for quoting the markers which delimit fields
and lines in CSV files. The tool which generated your CSV files may have
done so such that they are unreadable by other computer programmes.
In particular, a naive CSV implementation may have left backslashes or
double quotes near the edges of fields in way that Excel will ignore but
which are unacceptable to stricter systems such as databases. Try to
identify these issues early; they may be trivially fixable with basic
UNIX tools such as 'tr' and 'sed'.

CSV options
^^^^^^^^^^^

The markers for lines and fields differ between CSV files. There are
four of them: line terminators, field separators, field quotes, and escape
markers.

CSV files comprise a set of lines. Each line is followed by a
termination marker, including the final line. Within each line there
are fields.

*  field separator
*  field quoting (delimiter and policy)
*  line separator (at end of every line)


Exporting from a relational database to CSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* MySQL (server-side): SELECT INTO OUTFILE
* postgres: COPY 'table_name' TO STDOUT WITH ...
* sqlite: .dump
* DB2: EXPORT COLSEP=0x09 SELECT * FROM schema.table;
* SQL Server: bcp

Import CSV to a relational database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* MySQL: LOAD DATA LOCAL INFILE '/path/to/file.csv' INTO TABLE 'table_name' FIELDS SEPARATED BY '\t' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES; SHOW WARNINGS;
* postgres: COPY 'table_name' FROM '/path/to/file.csv' WITH ... 
* sqlite3: .mode ; .import
* python: .executemany()

Exporting CSV from spreadsheets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Excel gotchas
* Refine gotchas
* Gnumeric gotchas


programming
^^^^^^^^^^^
* python csv module
* awk


Folding nested values into CSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

About halfway through producing a CSV export, you usually realize that the 
data does not neatly lend itself to be serialized into a single table: a 
cell value can really only be expressed as a mapping or it can have several
values at once. At this stage you have several options:

 * Quote CSV in CSV. Yo dawg, don't do that, please.
 * Generate a proper relational database dump or SQLite image. Not bad, 
   but not a well-defined and generally compatible data exchange format 
   either.
 * Export multiple CSV sheets that combine to a relational model. This is
   probably the cleanest solution but requires that you also specify how
   the sheets relate to each other, e.g. by releasing an SQL schema
   (or at least a list of foreign keys).
 * Generate the export in a more expressive format, such as JSON. This is 
   not such a bad idea, as it will leave rows as list items while giving 
   you the ability to have lists and mappings as values.
 * Have magic column names that allow folding and unfolding of nested
   structures. One nice example of this is formencode's `NestedVariables`_ 
   which can also be used without the remainder of the library.

.. _`NestedVariables`: http://formencode.org/Validator.html#http-html-form-input


JSON
----

XML
---

Databases
---------


RDF
---
.. sectionauthor:: Alvaro Graves <alvaro@graves.cl>

This chapter shows how to use data available in RDF (Resource Description Framework)

(Very) brief description of what is RDF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Resource Description Framework is a W3C specification to describe information 
on the Web. It is a graph-based language that uses **URIs** (Universal Resource Identifier)
to identify resources such as web pages, people, past wednesday and describe information
about such resources. Thus for example, Tim Berners-Lee (the inventor of the
Web) is identified by `http://www.w3.org/People/Berners-Lee/card#i
<http://www.w3.org/People/Berners-Lee/card#i>`_

The basic unit of information in RDF is a *triple*, which consists in three
Elements: The first one identifies a *subject* (the resource that is being
described), the second describes the *predicate*, a type of relation or attribute the subject has. Finally, the third describes
the *object*, which is the value or resource associated to the subject via the
predicate. For example, if we want to say that "the prefered name for Tim
Bernes-Lee is 'Tim'" we can create the following triple:

 <http://www.w3.org/People/Berners-Lee/card#i> <http://www.w3.org/2004/02/skos/core#prefLabel> "Tim"

The "<" and ">" characters encloses a URI. Thus, we can add more information (say, "Tim has the twitter account http://twitter.com/timberners_lee")
simply by adding more triples

 <http://www.w3.org/People/Berners-Lee/card#i> <http://xmlns.com/foaf/0.1/account> <http://twitter.com/timberners_lee>

Graphically what we have is a graph where each URI can be linked to others of
can be given values in different values.

.. figure::  images/rdfBasicGraph.png

Further Reading
^^^^^^^^^^^^^^^

For a more comprehensive and detailed description of RDF, please refer to the
`RDF Primer <http://www.w3.org/TR/rdf-primer/>`_ which describes in more details
URIs, blank nodes, literals, etc.


Obtaining data from SPARQL endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Data in RDF can be obtained as `Dereferenceable URIs
<http://en.wikipedia.org/wiki/Dereferenceable_URI>`_ but in most of the cases,
you might want to obtain it from a SPARQL endpoint, which is a service on the
web (usually open) where people can execute `SPARQL <http://en.wikipedia.org/wiki/SPARQL>`_ queries, which is a query
language for RDF. SPARQL has several similarities to SQL, making the adoption
from relational databases to RDF databases not so difficult. For example, we can
list all the people in a SPARQL endpoint by executing the following query::

 SELECT ?person ?name WHERE{
  ?person <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
  ?person <http://xmlns.com/foaf/0.1/name> ?name .
 }


Lets analyze this query: First, the reserved word ``SELECT`` defines that we want to bind the results to the
 variables described using the question mark (``?person`` and ``?name``). After
 the ``WHERE`` reserved word we describe the *graph patterns* we want to
 specify. The first patterns contains a variable ``?person``, a predicate that 
 says that this variable is of a certain type and an object which represents the class "Person". Then, this can be translated as "something that is of type Person".
 
 The second pattern indicates that the same thing we want to retrieve **must
 also** have a predicate http://xmlns.com/foaf/0.1/name (which associates a
 resource with its name).
 
 In simple terms, we ask for "something that is of type Person and it also has a
 name". The results will be delivered in the variables described between the
 ``SELECT`` and ``WHERE`` reserved words. It is important to note that it is not
 necessary to retrieve all the variables described in the graph patterns.
 
 Simplifying SPARQL's syntax
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
 
 The previous query can have a simpler syntax, first by using prefixes::
 
  PREFIX foaf: <http://xmlns.com/foaf/0.1/>
  PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  
  SELECT ?person ?name WHERE{
    ?person rdf:type foaf:Person .
    ?person foaf:name ?name .
  }
  
Also, since we are describing two patterns with the same subject, we don't need
to write it twice. We can use a semicolon for every pattern except the last one
(which has to have a period)::
  
  PREFIX foaf: <http://xmlns.com/foaf/0.1/>
  PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  
  SELECT ?person ?name WHERE{
    ?person rdf:type foaf:Person ;
            foaf:name ?name .
  }
    
  
Example: Querying information about chilean poets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An importan source of RDF is `DBpedia <http://dbpedia.org>`_, a project focused
on extracting data from Wikipedia and publish it as RDF.
We can create a query to obtain the name of chilean poets by querying::
  
  PREFIX dcterms: <http://purl.org/dc/terms/>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  SELECT ?poet ?poetName WHERE{
       ?poet dcterms:subject <http://dbpedia.org/resource/Category:Chilean_poets>;
              rdfs:label ?poetName .
       FILTER (LANG(?poetName) = "en")
  }
  
The ``FILTER`` operator forces to obtain only the names in english, avoiding names in other languages. You can go to DBpedia's SPARQL endpoint (http://dbpedia.org/sparql) and execute
the query. The result should be something similar to
  
+--------------------------------------------------+-------------------------+
|                 poet                             |      poetName           |
+==================================================+=========================+
| http://dbpedia.org/resource/Nicanor_Parra        |    "Nicanor Parra"      |
+--------------------------------------------------+-------------------------+
| http://dbpedia.org/resource/V%C3%ADctor_Jara     |  "Víctor Jara"          |
+--------------------------------------------------+-------------------------+
| http://dbpedia.org/resource/Eduardo_Parra_Pizarro| "Eduardo Parra Pizarro" |
+--------------------------------------------------+-------------------------+
| http://dbpedia.org/resource/Alberto_Baeza_Flores |  "Alberto Baeza Flores" |
+--------------------------------------------------+-------------------------+


In most SPARQL endpoints, it is possible the format of the results (XML, JSON,
HTML, etc). For example, the same results in JSON are similar to this::
  
  
  { "head": { "link": [], "vars": ["poet", "poetName"] },
  "results": { "distinct": false, "ordered": true, "bindings": [
    { "poet": { "type": "uri", "value": "http://dbpedia.org/resource/Nicanor_Parra" }	, 
      "poetName": { "type": "literal", "xml:lang": "en", "value": "Nicanor Parra" }
    },
    { "poet": { "type": "uri", "value": "http://dbpedia.org/resource/V%C3%ADctor_Jara" }	, 
      "poetName": { "type": "literal", "xml:lang": "en", "value": "V\u00EDctor Jara" }
    },
    { "poet": { "type": "uri", "value": "http://dbpedia.org/resource/Eduardo_Parra_Pizarro" }	, 
      "poetName": { "type": "literal", "xml:lang": "en", "value": "Eduardo Parra Pizarro" }
    },
    { "poet": { "type": "uri", "value": "http://dbpedia.org/resource/Alberto_Baeza_Flores" }	, 
      "poetName": { "type": "literal", "xml:lang": "en", "value": "Alberto Baeza Flores" }
    }
    ]
   }
  }

  
Using SPARQL results with JavaScript
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This the results can be used also to fill a webpage. For example, if we want to include a list of chilean poets in a webpage, we execute the following code (based on jQuery)::

  <html>
  <head>
      <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>
      <script type="text/javascript">
      $(document).ready(function() {
         var q='PREFIX dcterms: <http://purl.org/dc/terms/>\
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\
                PREFIX dbp: <http://dbpedia.org/ontology/>\
                \
                SELECT ?poet ?poetName WHERE{\
                       ?poet dcterms:subject <http://dbpedia.org/resource/Category:Chilean_poets>;\
                              rdfs:label ?poetName .\
                FILTER (LANG(?poetName) = "en")\
                }';
                
         $.ajax({
           dataType: 'jsonp',
           data: {
              query: q,
              format: 'application/sparql-results+json'   // We specify we want the results as a JSON object
              },
           url: 'http://dbpedia.org/sparql',
           success: function(data){
            $(data.results.bindings).each(function(i, item){              
              $("#poetTable").append("<tr><td><a href='"+item.poet.value+"'>"+item.poetName.value+"</a></td>");
             });
           }
         });
      });
    </script>
  </head>
  <body>
    <table id="poetTable">
    <tr><th>Poet name</th></tr>
    </table>
  </body>
  </html>
  

Using SPARQL results with Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


`SPARQL Wrapper <http://sparql-wrapper.sourceforge.net/>`_ is a SPARQL client written in python that can be used to query SPARQL endpoints using Python. The interface is very simple and clean::

  from SPARQLWrapper import SPARQLWrapper, JSON
  
  sparql = SPARQLWrapper("http://dbpedia.org/sparql")
  sparql.setQuery("""
  PREFIX dcterms: <http://purl.org/dc/terms/>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  SELECT ?poet ?poetName WHERE{
       ?poet dcterms:subject <http://dbpedia.org/resource/Category:Chilean_poets>;
              rdfs:label ?poetName .
       FILTER (LANG(?poetName) = "en")
  }
  """)
  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()
  
  for result in results["results"]["bindings"]:
      print("%s's DBpedia URI is %s" % (result["poetName"]["value"], result["poet"]["value"]))
      
      
References and further reading
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* `RDF Primer <http://www.w3.org/TR/rdf-primer/>`_, is a good introduction to RDF
* `RDF Schema specification <http://www.w3.org/TR/rdf-schema/>`_ provides tools to create new vocabularies
* `A well detailed presentation on Semantic Web and Linked Data <http://www.bbc.co.uk/blogs/radiolabs/s5/linked-data/s5.html>`_
* `RDFa <http://rdfa.info/>`_ is a specification to add RDF embedded in HTML


Tools
^^^^^

* `RDF Validator <http://www.w3.org/RDF/Validator/>`_ check your RDF doesn't have errors
* `SparQled <http://sindicetech.com/sindice-suite/sparqled/>`_ is an interacrive SPARQL editor
* `Marbles <http://marbles.sourceforge.net/>`_ is a RDF/Linked Data explorer
* `visualRDF <http://graves.cl/visualRDF/>`_ provides a graphical visualization of RDF graphs

Libraries
^^^^^^^^^

* Java
    * `Jena <http://jena.apache.org/>`_
    * `Sesame <http://www.openrdf.org/>`_
* Python
    * `RDFLib <https://github.com/RDFLib/rdflib>`_
    * `SPARQL Wrapper <http://sparql-wrapper.sourceforge.net/>`_
* Ruby
    * `Linked Data for Ruby <http://rdf.rubyforge.org/>`_
* PHP
    * `ARC2 <https://github.com/semsol/arc2/wiki/>`_ parses and serializes RDF, provides a SPARQL endpoint (using MySQL as a backend) and much more
    * `RAP <http://www4.wiwiss.fu-berlin.de/bizer/rdfapi/>`_ an API for RDF
* C
    * `Redland RDF Libraries <http://librdf.org/>`_
* Scala
    * `Scardf <http://code.google.com/p/scardf/>`_
    
