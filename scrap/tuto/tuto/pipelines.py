import collections
from scrapy.exceptions import DropItem
from scrapy.exceptions import DropItem

import pymongo

class TutoPipeline(object):
    vat=2.55

    def process_item(self, item, spider):
        if item["price"]:
            if item['exclues_vat']:
                item['price']= item['price']*self.vat
                return item

            else:
                raise DropItem("missing price in %s"% item)
        
        return item



class MongoPipline(object):
    collections_name='scrapy_list'

    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri= mongo_uri
        self.mongo_db=mongo_db

    @classmethod
    def from_crewler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),

            mongo_db=crawler.settings.get('MONGO_DB','Lists')
        )    

    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongo_uri)
        self.db=self.client[self.mongo_db]


    def close_spider(self,spider):
        self.client.close()


    def process_item(self,item,spider):
        self.db[self.collection_name].insert(dict(item))
        return item

        # You can specify the MongoDB address and
        #  database name in Scrapy settings and MongoDB
        #  collection can be named after the item class.
        #  The following code describes 
        # how to use from_crawler() method to collect the resources properly −



class DuplicatePiline(object):
    def __init__(self):
        self.ids_seen=set()


    def process_item(self,item,spider):
        if item['id' ] in  self.ids_seen:
            raise DropItem("Repacted Item Found:%s"%item)

        else:
            self.ids_seen.add(item['id'])

            return item    

