# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup


class ParserService(object):
    def magnet_parser(self, html_content):
        new_urls = []
        soup = BeautifulSoup(html_content, 'lxml')
        """
        处理规则
        """
        magnets_nodes = soup.find_all(
            name='a', attrs={"href": re.compile(r'^magnet:?')}
        )
        magnets = []
        for node in magnets_nodes:
            magnets.append(node.get('href'))
        url_nodes = soup.find_all(name='a', attrs={
            'class': 'flag_pg'
        })
        for node in url_nodes:
            new_urls.append(node.get('href'))
        return new_urls, magnets


if __name__ == '__main__':
    p = ParserService()
    p.parser('')
