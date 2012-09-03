Accessing Data from Google Storage
==================================
.. sectionauthor:: Michael Bauer (@mihi_tr on twitter)

Google Storage is a Google hosted cloud storage solution. Storage is not
for free - nevertheless some projects such as the Google sponsored
`measurement lab`_ host their openly available data with Google storage. To
download and list the data Google offers a command line tool: `gsutil`_

How to find files
-----------------

To find files without the need of a sign in, you'll need to know the
initial "bucket" the data is in. "Bucket" is just googles term for folder.
For example measurement-lab data is in "gs://m-lab/".

Listing the content of a bucket
-------------------------------

The gstool generally follows naming of the unix command line. So to list
the contents of a bucket simply type::

    gsutil ls <bucket>

This should give you a list of items within the bucket. 
``ls -R`` will result in a recursive list of buckets

Downloading content from a bucket
---------------------------------

Once you identified the object you want to download simply use::

    gsutil cp <object> .

to copy it into the current directory. If you want to copy the contents of
a bucket (and it's sub-buckets), simply type::
    
    gs cp -R <bucket> .

The second argument after bucket can also be a local directory to copy to.    


.. _measurement lab: http://measurementlab.net
.. _gsutil: https://developers.google.com/storage/docs/gsutil
