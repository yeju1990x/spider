# -*- coding: utf-8 -*-
from magnet.html_downloader import DownloaderService
from magnet.html_outputer import OutputerService
from magnet.html_parser import ParserService
from magnet.url_manager import UrlManagerService



class SpiderMain(object):
    def __init__(self, root_url):
        self.root_url = root_url

    def crawl(self):
        ums = UrlManagerService()
        dls = DownloaderService()
        prs = ParserService()
        ops = OutputerService()

        ums.add_url(self.root_url)

        while True:
            new_url = ums.has_new_url()
            if not new_url:
                return
            html_content = dls.download(new_url)
            new_urls, content = prs.parser(html_content)
            ums.add_urls(new_urls)
            ops.save_content(content)


if __name__ == '__main__':
    r_url = "www.baidu.com"
    spider = SpiderMain(r_url)
    spider.crawl()
