
import scrapy


class FirstScrapyItem(scrapy.Item):
    # define the fields for your item here like:

    item=DmozItem()
    
    item ['title'] = scrapy.Field()
    item ['url'] = scrapy.Field() 
    item ['desc'] = scrapy.Field() 
    