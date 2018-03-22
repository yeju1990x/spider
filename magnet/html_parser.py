# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

class ParserService(object):
    def parser(self, html_content):
        bs = BeautifulSoup(html_content)
        bs.fin