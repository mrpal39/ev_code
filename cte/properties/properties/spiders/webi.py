import scrapy


class WebiSpider(scrapy.Spider):
    name = 'webi'
    allowed_domains = ['web']
    start_urls = ['http://web/']

    def parse(self, response):
        pass
