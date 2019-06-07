# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
 
class FilterDuplicate(object):
    
    def open_spider(self, spider):
        self.text = set()
 
    def process_item(self, item, spider):
        #check if item is already in your set:
        if item['text'] in self.text:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.text.add(item['text'])
            #means if the item doesn't exist in your set then add it to it
            return item