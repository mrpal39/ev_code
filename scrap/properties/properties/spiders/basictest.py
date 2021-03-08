from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from properties.items import PropertiesItem
import datetime
from urllib.parse import urlparse
import socket

import scrapy

class BasicSpider(scrapy.Spider):
    name = "basictest"
    allowed_domains = ["web"]
    start_urls=(
        'https://developers.facebook.com/blog/post/2021/01/26/introducing-instagram-content-publishing-api/?utm_source=email&utm_medium=fb4d-newsletter-february21&utm_campaign=organic&utm_offering=business-tools&utm_product=instagram&utm_content=body-button-instagram-graph-API&utm_location=2',
         )

    def parse (self,response):
       """ @url https://developers.facebook.com/blog/post/2021/01/26/introducing-instagram-content-publishing-api/?utm_source=email&utm_medium=fb4d-newsletter-february21&utm_campaign=organic&utm_offering=business-tools&utm_product=instagram&utm_content=body-button-instagram-graph-API&utm_location=2
        @return item 1
        @scrapes title price
        @scrapes url project"""


    l = ItemLoader(item=PropertiesItem(), response=response)
    # Load fields using XPath expressions
    l.add_xpath('title', '/html/body/div[1]/div[5]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/p[1]/text()',
            MapCompose(unicode.strip, unicode.title))
    # l.add_xpath('price', './/*[@itemprop="price"][1]/text()',
    # MapCompose(lambda i: i.replace(',', ''),
    # float),
    # re='[,.0-9]+')
    # l.add_xpath('description', '//*[@itemprop="description"]'
    # '[1]/text()',
    # MapCompose(unicode.strip), Join())
    
    # Housekeeping fields
    l.add_value('url', response.url)
    l.add_value('project', self.settings.get('BOT_NAME'))
    l.add_value('spider', self.name)
    l.add_value('server', socket.gethostname())
    l.add_value('date', datetime.datetime.now())
    return l.load_item()