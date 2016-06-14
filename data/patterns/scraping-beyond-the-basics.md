---
title: Scraping - Beyond the Basics
---

This guide focuses on how you can extract data from web sites and web services. We will go over the various resources at your disposal to find sources which are useful to you.

Extracting Data
---------------

### General tips

- Minimise the pages to scrape. This will save everybody time and resources.
- Inspect any AJAX fields. AJAX is generally performed by sending JavaScript objects between the server and the web browser. They are easy to parse and are generally very rich.
- Try looking for a sitemap.xml.
- Any pages in the robots.txt which disallow access are generally where the bulk of the value lies.
- Run an evented or multi-threaded system. Once you have gained the confidence of building a few scrapers, learn how to optimise performance. Given that you are using lots of external resources, there will be lots of latency involved. This means that your scraper's performance increases by using asynchronous programming.

### Types of scrapers

+ DOM-based approaches
	+ advantages
    	- familiar
        - relatively computationally efficient

    + disadvantages
		- requires parsing the entire document, which can be difficult with messy content
        - prone to breaking when encountering unexpected content
        - can be tricky to handle errors
        - may require learning a new language, [XPath](http://en.wikipedia.org/wiki/XPath)

	This is the most common form of scraper. All the data that you are looking to extract is identified by selecting portions from the DOM.

    Most modern libraries, such as [lxml](http://lxml.de/) accept CSS selectors. So, in Python to extract content from the `<title>` tag, you do something similar to `page.cssselect('title')[0].text`.

    [XPath](http://en.wikipedia.org/wiki/XPath), the XML Path Language, is a fuller way to select elements from XML and XML-like documents, such as HTML. As with CSS, it uses the structure of the page and tag attributes to be able to select specific elements or groups of elements. XPath expressions can look fairly complex and take some some time to learn.

+ Template
	- Regular expressions to look for common patterns in the text. One of the easiest template extraction systems is [scrapemark](https://github.com/arshaw/scrapemark). While it is not the most computationally efficient, using template systems requires far less manual work to get going with.

+ Machine-learning
	- Machine-learning packages work by training a model of example pages, then asking for matching material.

    One tool that is very good at removing boilerplate, such as headings from web pages and only leaving the content is called [boilerpipe](http://code.google.com/p/boilerpipe/). It is bundled together with the Data Science Toolkit\_ and there is an [demo of boilerpipe's capabilities is available](http://boilerpipe-web.appspot.com/).

### A scraping framework

Let's demonstrate some of the principles that we have been talking about.

We'll be creating a scraping framework, called `tbd`:

```python
"""
{{somthing}}.py : a webscraping framework..
"""
import bsddb
import pickle
import urllib2
from asynchat import fifo

from dateutil import parser as date_parser
import lxml
import lxml.html

START_URL = 'http://blog.okfn.org/'
db = bsddb.hashopen('okfnblog.db')

#
# UTILITY FUNCTIONS
#

def get_clean_page(url):
	page = get_page(url)
	page = lxml.html.tostring(page)
	page = lxml.html.fromstring(page)
	return page

def get_page(url):
	res = urllib2.urlopen(url)
	page = lxml.html.parse(res)
	page.make_links_absolute()
	return page

def save_post(post):
	save(post['post_id'], post)

def save_tag(tag):
	save('tag-%s' % tag['tag'], tag)

def save_author(author):
	save('author-%s' % author['name'], author)

def save(key, data):
	db[key] = pickle.dumps(data)

def extract_created_at_datetime(post):
	date = post.cssselect('span.entry-date')[0].text
	time = post.cssselect('div.entry-meta a')[0].attrib['title']
	return str(date_parser.parse(date + ' ' + time))

def process_post(url):
	source = get_page(url)
	post = {}
	post['title'] = source.cssselect('h1.entry-title')[0].text
	post['author'] = source.csselect('span.author a')[0].text
	post['content'] = source.cssselect('div.entry-content')[0].text_content()
	post['as_html'] = lxml.html.tostring(source.cssselect('div.entry-content')[0])
	post['created_at'] = extract_created_at_datetime(source)
	post['post_id'] = source.cssselect('div.post')[0].attrib['id']
	post['tags'] = [tag.text for tag in source.cssselect('a[rel~=tag]')]
	post['url'] = url
	yield save_post, post
	yield save_author, dict(name=post['author'])
	for tag in post['tags']
		yield save_tag, dict(tag=tag, post_id=post_id, author_name=post['author'])

def process_archive(url):
	archive = get_page(url)
	for post in archive.cssselect('.post .entry-meta a'):
		yield process_post, post.attrib['href']
	previous = archive.cssselect('.nav-previous a')
	if previous: #is found
		yield process_archive, previous[0].attrib['href']

def process_start(url):
	index = get_page(url)
	for anchor in index.cssselect('li#archives-2 a'):
		yield process_archive, anchor.attrib['href']

def main():
	queue = fifo((process_start, START_URL))
	while 1:
		status, data = queue.pop()
		if status != 1:
			break
		func, args = data
		for newjob in func(args):
			queue.push(newjob[0], newjob[1])
		db.sync()
```

### Dealing with JavaScript

JavaScript can be a pain for scrapers. JavaScript is often used to alter the DOM on pages after they have been created. This means that the page you see in an Internet browser is different that the page your scrapers see.

There are a few different approaches to dealing with this process. We will briefly outline them, then go through the easiest option.

#### Options

There are three broad options when considering how to deal with JavaScript:

- **Don't** Much of the AJAX content could be downloaded directly by your scraper. AJAX is generally sent as JSON, which means it is  very easy to parse. You could save yourself a lot of time if you spent some time evaluating the target more closely.
- **Do it offline** Under this approach, you download the content, send it to a JavaScript interpreter such as [SpiderMonkey](https://developer.mozilla.org/en/SpiderMonkey), then process the results. If this sounds like a lot of manual work, it is. Fortunately for us, other people have struggled with this problem before and have released software to take care of most of the detail. Take a look at [crowbar](http://simile.mit.edu/wiki/Crowbar) and webkitcrawler.
- **Automate a browser** This third approach involves relying on a web browser's handling JavaScript itself. Until recently, this has involved quite a bit of complicated effort. Now, a library called splinter has come along to make life much easier.

One of the biggest differences between the second and third options is that the second option does not require a monitor. That means, it can be much easier to deploy on a server. However, in general the tasks we'll be doing are fairly small and can happily run in the background while you're doing other work.

#### Path of least resistance - splinter

Splinter is Python library that takes all of the trouble out of this process:

```bash
>>> from splinter.browser import Browser
>>> br = Browser('webdriver.chrome')
```
As a trivial example, let's find Auckland's current weather from [the New Zealand Herald](http://www.nzherald.co.nz). If you visit their homepage without JavaScript enabled on your internet browser, you'll see nothing. However, with JavaScript, an icon appears :
```bash
>>> br.visit('http://www.nzherald.co.nz/')
>>> high = br.find_by_css('span.high').first.value
>>> low  = br.find_by_css('span.low').first.value
>>> high, low
'19\xb0', '11\xb0' # \xb0 is the degree sign
```

### Dealing with PDF content

PDF documents are a pain. Some PDF generators don't actually have the concept of a word-- every letter is individually placed. This makes it very hard to create a software tool that can combine letters to make words, and combine words to make sentences. However, depending on the source documents, there are possibilities for extracting information from them.

The [Data Science Toolkit]() is now the best way to get up and running with these kinds of tasks. Its "File to Text" tool takes an image, PDF or MS Word document and returns text to you.

If you only have a few documents to process, the website actually allows you to do the processing on their servers.

#### Extracting plain text

A quick way to extract text from a PDF programmatically is with the Python library, [slate](). Disclaimer: I maintain slate. Its philosophy is to have a very low barrier to entry, but only extracts plain text out of the document:

```bash
>>> import slate
>>> with open('salesreport.pdf') as f:
...    report = slate.PDF(f)
...
>>> report[0]
"2011 ..."
```

#### Digging deeper

One of the better free tools is called [pdftohtml](). It generates an HTML version of the document, which can then be processed by tools that you are used to. It does a good job of understanding the layout.

It is possible to circumvent security measures in PDF documents. The PDF viewer [xpdf]() provides this by default. This allows you to print or extract content that may be otherwise prevented through security measures.

### General Tips

#### Avoiding being blocked

It's possible to use sophisticated techniques to circumvent rate limitations and IP address blocking. However, the best technique for avoiding being blocked is by being a good netizen and adding pauses between your requests.

Scrape during the night of the site's local time. This is very likely to have very few users, meaning the site will have more capacity to serve your scraper.

#### Be part of the open data community

When scraping open data, you should use ScraperWiki. ScraperWiki allows people to cooperatively build scrapers. They will also take care of rerunning your scraper periodically so that new data are added.

By being part of the community, you increase your profile, learn much more and benefit from people fixing your scraper when it breaks.

#### Learn async programming

Network programming is inherently wasteful in many ways. Your processor is consistently waiting for things to arrive from other parts of the world. Therefore, you can speed up the processing steps of your scrapers significantly if you take the time to learn asynchronous programming.

