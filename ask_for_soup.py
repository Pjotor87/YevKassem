#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from bs4 import BeautifulSoup
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
"""
Description: Asks for soup. Might misinterpret your order as an insult...
"""

def html_page(url):
    logging.debug('requesting: {0}'.format(url))
    soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers={'User-Agent': "Magic Browser"})).read(), "html.parser")
    if not soup:
        logging.error("No soup for you! {0}".format(url))
    return soup

def main():
    print(html_page("https://en.wikipedia.org/wiki/The_Soup_Nazi"))
        
if __name__ == "__main__":
    main()