Reconciling Data with Nomenklatura
==========================

Data often is messy and unclean. Especially if multiple users enter Data about the same thing - there will be one or the other mis-spelling. `Refine`_ is a fabulous tool for reconciling columns and reconciling different spellings or formattings of the same thing. However, what do you do if you want to automate the cleaning (for a scraper run daily e.g). `Nomenklatura`_ to the rescue.

What is Nomenklatura
---------------------------------

`Nomenklatura`_ is a data reconciling service that helps you assigning multiple forms of expressing a value to a specific value. Take for example a person. This person could be adressed as "Firstname Lastname", "Lastname Firstname", "Title Firstname Lastname", "Title Lastname" etc - however in your data you want to have only one representation of one person. Nomenklatura helps doing exactly - using an API and a web-frontend for linking multiple representations to a single value.

Basic Concepts
-----------------------

Nomenklatura has two basic objects: Values and Links. 

**Values** are the final representation you want to have (e.g. Dr. Henry Jekyll).
**Links** are different representation pointing to the values (e.g. Mr. Edward Hyde)

Links do not neccessarily link to values - they also can be invalid or not matched. Non matched links need to be linked to values using either the API - or easier the web-frontend.

Using the Python Module
------------------------------------

Nomenklatura comes with a Python module to help you work with the data. A few simple steps will take you to reconciling data with Nomenklatura

#. Sign in to `Nomenklatura`_ using your github account
#. Create a new Dataset on Nomenklatura
#. Install the nomenklatura python module using ``pip install pynomenklatura``

Start posting links::

  import nomenklatura
  
  key= # put the API key of nomenklatura here.
  ds=nomenklatura.Dataset("myDataset",api_key=key)
  
  unclean=["Dr. Jekyll","Mr. Hyde", "Edward Hyde", "Margret Thatcher"]
  
  def lookup(key):
    try:
      value=ds.loopup(key)
      return value.value
    except ds.NoMatch:
      return key
      
  clean=[lookup(x) for x in unclean]
  
Now go back to the web interface - you will have some links to be reconciled (Button to the left) - Go ahead and link them to together. If you re-run your script after you've finished the reconciliation the cleaned data will be correct. 

Advanced Uses
-----------------------

If you have a lot of data to be reconciled, doing a lookup for each value might be overkill - you can add a simple caching layer around this::

  import nomenklatura
  import itertools
  
  class NKCache(object):
    def __init__(self,dataset,key):
        self.ds=nomenklatura.Dataset(dataset,api_key=key)
        self.fetch()
    
    def fetch(self):
        links=itertools.ifilter(lambda x: x.value: self.ds.links())
        self.cache=dict(((l.key,l.value["value"]) for l in links))
    
    def lookup(self,key):
        if key in self.cache.keys():
           return self.cache[key]
        else:
            try:
                value=self.ds.lookup(key)
                return value.value
            except self.ds.NoMatch:
                return key
                
This will download all known links in one chunk and only call lookup if the link is not present in the initial data use it like::

    cache=NKCache("myDataset",api_key=key)
    
    clean=[cache.lookup(x) for x in unclean]
    
This will speed your work up - as long as you don't get too many links (of course the effect will only be notable after a majority of links have been reconciled).



.. _Refine: https://github.com/OpenRefine/OpenRefine
.. _Nomenklatura: http://nomenklatura.okfnlabs.org 

