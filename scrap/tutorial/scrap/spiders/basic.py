import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'com'
    allowed_domains = ['djangopackages.org']
    start_urls = ['https://djangopackages.org']

    # rules = (
    #     # Extract links matching 'category.php' (but not matching 'subsection.php')
    #     # and follow links from them (since no callback means follow=True by default).
    #     Rule(LinkExtractor(allow=('category/', ), deny=('subsection/', ))),

    #     # Extract links matching 'item.php' and parse them with the spider's method parse_item
    #     Rule(LinkExtractor(allow=('item/', )), callback='parse_item'),
    # )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="usage-link-sentry"]/text()')
        item['name'] = response.xpath('//td[@id="usage-image-sentry"]/text()').get()
        item['description'] = response.xpath('//td[@class="package-githubcommits"]/text()').get()
        item['link_text'] = response.meta['/packages/p/sentry/']
        url = response.xpath('//td[@id="additional_data"]/@href').get()
        return response.follow(url, self.parse_additional_page, cb_kwargs=dict(item=item))

    def parse_additional_page(self, response, item):
        item['additional_data'] = response.xpath('//p[@id="additional_data"]/text()').get()
        return item