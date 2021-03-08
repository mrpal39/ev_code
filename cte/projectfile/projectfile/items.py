# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy import Item, Field
# define the fields for your item here like: 
# 
class SainsburysItem(scrapy.Item):   
    name = scrapy.Field() 




class SainsburysItem(Item):
    url = Field()    
    product_name = Field()    
    product_image = Field()    
    price_per_unit = Field()    
    unit = Field()    
    rating = Field()   
    product_reviews = Field()    
    item_code = Field()    
    nutritions = Field()    
    product_origin = Field()


class FlatSainsburysItem(Item):
    url = Field()  
    product_name = Field()    
    product_image = Field()    
    price_per_unit = Field()    
    unit = Field()    
    rating = Field()    
    product_reviews = Field()    
    item_code = Field()    
    product_origin = Field()
    energy = Field()
    energy_kj = Field()
    kcal = Field()
    fibre_g = Field()
    carbohydrates_g = Field()
    of_which_sugars = Field()
