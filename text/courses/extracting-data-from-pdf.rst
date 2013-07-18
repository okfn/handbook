Extracting Data from PDFs
=========================

It's happened to all of us, we want some nice, fresh data that we can sort, analyse and visualise and instead, we get a PDF. What a disappointment. 

This course will guide you through the main decisions involved in getting data out of PDFs into a format that you can easily use in data projects. 

.. raw:: html

  <iframe src="http://dump.tentacleriot.eu/extracting-data-from-pdf/index.html" style="width: 650px; height: 500px; border:
  0px;" scrolling="no"></iframe>

Navigate the slideshow with the arrow keys.

When cut and paste fail, you'll sometimes need to resort to more powerful means. Below is a little more information on the two of the trickiest paths highlighted by the flowchart above. 

Note: Bad PDFs and worse PDFs 
=============================

PDFs are not all the same, some are generated from computer programs (best case scenario) but frequently, they are scanned copies of images. Worst case scenario, they are smudged, tea stained, crooked scans of images. In the latter case - your job will be considerably harder. Nevertheless, there are a couple of tips you can take to make your job easier, read on! 

(Modified from text contributed by Tim McNamara)

Path 1: OCR 
===========

The OCR Pipeline
----------------

Creating a system for Optical Character Recognition (OCR) can be challenging.
In most circumstances, the `Data Science Toolkit`_ will be able to extract
text from files that you are looking for.

.. _Data Science Toolkit: http://www.datasciencetoolkit.org/

OCR largely involves creating a conveyor belt of programming tools (but read on and you will discover a couple which don't) The whole process can include several steps:

  * Cleaning the content
  * Understanding the layout
  * Extracting text fragments from pieces of each page, according to the 
    layout of each page
  * Reassembling text fragments into a usable form

Cleaning the pages
^^^^^^^^^^^^^^^^^^

This generally involves removing dark splotches left by scanners,
straightening pages and adding contrast between the background 
and the printed text. One of the best free tools for this is `unpaper`_. 

File type conversion
^^^^^^^^^^^^^^^^^^^^

One thing to note is that many OCR engines only support a small number of input file types. Typically, you will need to convert your images to
portable pixmap format (.ppm) files.

In this section, we'll highlight a few of the options for extracting data or text out of a PDF. We don't want to reinvent the wheel, with all of these options, you'll need to read the manuals for the individual piece of software - we aim here to merely serve as a guide to help you choose your weapon! 

Without learning to code, the options on this front are unfortunately somewhat limited. Take a look at the following pieces of software: 

* `Tabula`_ - currently causing a lot of buzz and excitement, but you currently need to install your own version, which makes the barrier to entry quite high. 
* `ABBYY Finereader`_ - unfortunately not free but highly regarded by many as a powerful piece of kit for busting data out of its PDF prisons.  
* `CometDocs`_ - an internet based service

.. _Tabula: http://tabula.nerdpower.org/
.. _ABBYY Finereader: http://finereader.abbyy.com/ 
.. _CometDocs: http://www.cometdocs.com/

Warning - the tools below require you to open your `command line`_ to install and run. And some require knowledge of code to use. We mention them here so that you get an idea of what is possible.  

The main contenders in the code-based ones are:

* `Tesseract OCR`_
* `Ocropus`_
* `GNU Ocrad`_
* `PDF2HTML`_

.. _unpaper: http://unpaper.berlios.de/
.. _command line: http://en.wikipedia.org/wiki/Command-line_interface
.. _Tesseract OCR: https://code.google.com/p/tesseract-ocr/wiki/ReadMe
.. _Ocropus: https://code.google.com/p/ocropus/
.. _GNU Ocrad: http://www.gnu.org/software/ocrad/ 
.. _PDF2HTML: http://pdf2htmlex.blogspot.de/

Path 2: Transcription and Microtasking
======================================

Besides the projects mentioned in the presentation, there are a few other options. 

The open source project, `TaskMeUp`_ is designed to allow you to distribute jobs
between hundreds of participants. If you have a project that could benefit 
from being reviewed by human eyes, this may be an option for you.

Alternatively, there are a small number of commercial firms providing this 
service. The most well known is Amazon's Mechanical Turk. They providing 
something of a wholesale service. You may be better off using a service such
as `Cloudflower`_ or `Microtask`_. Microtask also has the ethical advantage of not
providing service below the minimum wage. Instead, they team up with video 
game sellers to provide in-game rewards. 

.. _TaskMeUp: https://bitbucket.org/waj/taskmeup
.. _Cloudflower: http://crowdflower.com/
.. _Microtask: http://www.microtask.com/

Challenge: Free the Budgets
---------------------------

.. raw:: html

  <div class="well">

**Task:**   Find yourselves some PDFs to bust!

  For example, there are many PDFs which need your help in the `Budget Library of the International Budget Partnership`_

.. _Budget Library of the International Budget Partnership: https://docs.google.com/folder/d/0ByA9wmvBrAnZN3ZrdzNzcS1JZzg/edit?pli=1

  Remember - once you've liberated your data, share it and save someone else the job! Why not upload to `the OpenSpending group on the datahub`_ and drop the `OpenSpending Mailing List`_ a line to say you have done so, people are always looking for raw data to visualise and explain. 

  .. _the OpenSpending group on the datahub: http://datahub.io/dataset?groups=openspending&q=openspending 
  .. _OpenSpending Mailing List: http://lists.okfn.org/mailman/listinfo/openspending
.. raw:: html
  
  </div>

.. raw:: html

  <div class="alert alert-info">Any questions? Got stuck? <a class="btn
  btn-large btn-info" href="http://ask.schoolofdata.org">Ask School of Data!
  </a></div>
