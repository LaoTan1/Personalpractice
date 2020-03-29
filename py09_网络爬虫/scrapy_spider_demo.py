# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'

    def start_requests(self):
        urls = [
            'http://python123.io/ws/demo.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def prase(self, response):
        fname = response.url.split("/")[-1]
        with open(fname, "wb") as f:
            f.write(response.body)
        self.log('Saved file %s.' % fname)

DemoSpider()