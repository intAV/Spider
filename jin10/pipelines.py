# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import hashlib
from redis import Redis


class MyonePipeline:
    def open_spider(self,spider):
        self.conn = Redis(host='127.0.0.1', port=6379)

    def process_item(self, item, spider):
        source = item['datatime'] + item['content']
        hashValue = hashlib.sha256(source.encode()).hexdigest()
        ex = self.conn.sadd('hashValue', hashValue)
        if ex == 1:
            print(item['datatime'],item['content'])
        else:
            pass

        return item

    def close_spider(self,spider):
        print("close redis...")
