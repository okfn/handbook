from urlparse import urljoin
from lxml import html

INITIAL_URL = 'http://cordis.europa.eu/fetch?CALLER=FP7_PROJ_EN'

def get_index():
    """ Traverse the search results of an empty query for projects in 
    the CORDIS database. """

    # fetch an initial page:
    doc = html.parse(INITIAL_URL)
    # infinite loop isn't nice, but we'll break when no 'next' link is
    # available.
    while True:
        # iterate over the links for all projects on this page
        for project_link in doc.findall('//div[@id="PResults"]//a'):

            # join up URLs to generate the proper path
            href = project_link.get('href').replace('..', '')
            yield urljoin(INITIAL_URL, href)

        next_url = None

        # look at all links in the navigation section of the listing
        for nav in doc.findall('//p[@class="PNav"]/a'):

            # if the link is a 'next' link, follow it
            if 'Next' in nav.text:
                href = nav.get('href').replace('..','')
                next_url = urljoin(INITIAL_URL, href)

                # replace the document to traverse the next page in
                # the following iteration
                doc = html.parse(next_url)

        # no next link was found, so cancel
        if not next_url:
            break

if __name__ == '__main__':
    for link in get_index():
        print link
