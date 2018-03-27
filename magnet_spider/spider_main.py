# -*- coding: utf-8 -*-
import argparse
from urllib import parse

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
                break
            new_url = ums.get_url()
            print('当前爬取第 %d 个页面，当前url: %s' % (cnt, new_url))
            html_content = dls.download(new_url)
            new_urls, magnet_urls = prs.magnet_parser(html_content)
            ums.add_urls(new_urls)
            ops.save_content(magnet_urls)
            if cnt >= 5:
                break

        print(ops.magnets)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True, help='信用卡ID')
    args = parser.parse_args()

    key = args.name
    # key = "环太平洋"
    parsed_key = parse.quote(key)
    r_url = "http://cililianc.com/list/{}/1.html".format(parsed_key)
    spider = SpiderMain(r_url)
    spider.crawl()
