# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from miao.items import TopicItem,ContentItem

## 爬虫的分析结果都会由scrapy交给此函数处理
class FilePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, TopicItem):
            ## 在此可进行文件写入、数据库写入等操作
            pass

        if isinstance(item,ContentItem):
            pass

        return item