# -*- coding: utf-8 -*-
from html_downloader import DownloaderService
from html_outputer import OutputerService
from html_parser import ParserService
from url_manager import UrlManagerService


class SpiderMain(object):
    def __init__(self, root_url):
        self.root_url = root_url

    def crawl(self):
        ums = UrlManagerService()
        dls = DownloaderService()
        prs = ParserService()
        ops = OutputerService()

        ums.add_url(self.root_url)

        cnt = 0

        while True:
            cnt += 1
            if not ums.has_new_url():
                return
            new_url = ums.get_url()
            print('当前爬取第 %d 个页面，当前url: %s' % (cnt, new_url))
            html_content = dls.download(new_url)
            new_urls, magnet_urls = prs.magnet_parser(html_content)
            ums.add_urls(new_urls)
            ops.save_content(magnet_urls)
            if cnt >= 10:
                break


if __name__ == '__main__':
    r_url = \
        "http://cililianc.com/list/%E7%8E%AF%E5%A4%AA%E5%B9%B3%E6%B4%8B/1.html"
    spider = SpiderMain(r_url)
    spider.crawl()
