# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem

class QiushispiderPipeline(object):

    def __init__(self):
        self.filename = open(r'F:\潭州课程录播及源码\scpy框架\qiushi.txt','w',encoding='utf-8')
    
    def process_item(self, item, spider):
        self.filename.write(json.dumps(dict(item), ensure_ascii=False)+'\n\n')
        return item

    def close_spider(self,spider):
        self.filename.close()

