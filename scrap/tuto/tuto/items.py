# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item ,Field

from scrapy.loader import ItemLoader 
from scrapy.loader.processors import TakeFirst, MapCompose, Join  

class DemoLoader(ItemLoader):  
   default_output_processor = TakeFirst()  
   title_in = MapCompose(unicode.title) 
   title_out = Join()  
   size_in = MapCompose(unicode.strip)  
   # you can continue scraping here
class DemoItem(scrapy.Item):
    

    # define the fields for your item here like:
    product_title = scrapy.Field()
    product_link = scrapy.Field()

    product_description = scrapy.Field()

    pass
