from scrapy.item import Item, Field

import datetime 
import socket


class PropertiesItem(Item):
    # Primary fields
    title = PropertiesItem()
    price = Field()
    description = Field()
    address = Field()
    image_urls = Field()
    # Calculated fields
    images = Field()
    location = Field()
    # Housekeeping fields
    
    l.add_value('url', response.url)
    l.add_value('project', self.settings.get('BOT_NAME'))
    l.add_value('spider', self.name)
    l.add_value('server', socket.gethostname())
    l.add_value('date', datetime.datetime.now())



    return l.load_item()