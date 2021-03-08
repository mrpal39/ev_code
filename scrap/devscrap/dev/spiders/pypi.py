# -*- coding: utf-8 -*-
import scrapy


class PypiSpider(scrapy.Spider):
    name = 'pypi'
    allowed_domains = ['https://pypi.org']
    start_urls = ['http://https://pypi.org/']

    def parse(self, response):
        pass
