# -*- coding: utf-8 -*-


class UrlManagerService(object):
    def __init__(self):
        self.new_urls = []
        self.old_urls = []

    def has_new_url(self):
        return len(self.new_urls) > 0

    def add_url(self, url):
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.append(url)

    def get_url(self):
        if len(self.new_urls) == 0:
            return None
        else:
            new_url = self.new_urls.pop()
            self.old_urls.append(new_url)
            return new_url

    def add_urls(self, urls):
        for url in urls:
            self.add_url(url)
