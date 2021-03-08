# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


class PropertiesItem():

    title=Field()
    price=Field()
    description=Field()
    address = Field()
    image_urls = Field()

    #imagescalculaitons
    images = Field()
    locations = Field()
    #housekeeping
    url=Field()
    project = Field()
    spider=Field()
    server = Field()
    date=Field()

