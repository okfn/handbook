''' Upload datawrangling handbook to wordpress site.

Copy this file to same directory as your sphinx build directory and then do

    python upload.py -h

NB: You need to enable XML-RPC access to the wordpress site (via Settings -> Writing)

NB: this requires pywordpress (pip install pywordpress) and associated config
file - see https://github.com/rgrp/pywordpress
'''

import os
import optparse
import pywordpress
import itertools
from pyquery import PyQuery
import re
import pprint

# TODO: deal with utf8 encoding
def prepare_html(fileobj):
    pq=PyQuery("".join(fileobj))

    out = PyQuery(pq("div.content").html() )
    # TODO: do we want to extract the title
    # Do we want title at all?
    toc=pq("div.toc ul.current").outerHtml()
    if pq("div.section h1"):
      title= pq("div.section h1")[0].text
      if toc:
        out("div.section h1").after(toc)
      pq("div.section h1").remove()  
    else:
      title=""

    # TODO: insert toc (??)

    # insert after h1 on 4th ine
    # lines = out.split('\n')
    # out = '\n'.join(lines[:4] + [ '[toc]' ] + lines[4:])

    # now various regex
    
    out=out.html()
    # replace .html with / and index.html with simple ./
    pattern = '(href=".[^"]*)index\.html"'
    out = re.sub(pattern, '\\1"', out)
    pattern = 'href="index\.html"'
    out = re.sub(pattern, 'href="./"', out)
    pattern = '(href="[^"]*).html"'
    out = re.sub(pattern, '\\1/"', out)

    return (out, title)

def upload(wordpress_site_url='', handbook_path='/handbook/'):
    '''Convert and upload built sphinx content to destination site

    1. Clean up and extract html for uploading
    2. Upload

    NB: you'll need a config.ini to exist as per pywordpress requirements
    '''
    pages = {}
    for (root, dirs, files) in os.walk('build/html'):
        files=itertools.ifilter(lambda x: re.search(".html$",x),files)
        if '_sources' in root:
            continue
        for f in files:
            path = os.path.join(root, f)
            print path
            subpath = os.path.join(
                root[len('build/html'):].lstrip('/'),
                # index.html => /
                f.replace('index.html', '')
                )
            urlpath = handbook_path + os.path.splitext(subpath)[0]
            # everything has a trailing '/' e.g. /handbook/introduction/
            if not urlpath.endswith('/'):
                urlpath += '/'
            (out, title) = prepare_html(open(path))
            pages[urlpath] = {
                'title': title,
                'description': out
            }

    # do the upload
    wp = pywordpress.Wordpress.init_from_config('config.ini')
    wp.verbose =True
    print 'Creating pages in wordpress'
    changes = wp.create_many_pages(pages)
    print 'Summary of changes'
    pprint.pprint(changes)


if __name__ == '__main__':
    usage = '''%prog {action}

    upload: upload handbook to website
    '''
    parser = optparse.OptionParser(usage)
    options, args = parser.parse_args()
    if len(args) < 1:
        parser.print_help()
        sys.exit(1)
    action = args[0]
    if action == 'upload':
        upload()
    else:
        parser.print_help()
        sys.exit(1)
