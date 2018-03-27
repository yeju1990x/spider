# -*- coding: utf-8 -*-
import requests


class DownloaderService(object):
    def download(self, new_url):
        response = requests.get(new_url)
        return response.text
