# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PropertiesPipeline(object):
    def process_item(self, item, spider):
        return item


ITEM_PIPELINES = {

'scrapy.pipelines.images.ImagesPipeline': 1,
'properties.pipelines.geo.GeoPipeline': 400,
}
IMAGES_STORE = 'images'
IMAGES_THUMBS = { 'small': (30, 30) }