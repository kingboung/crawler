# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class TopicItem(Item):
    url=Field()
    title=Field()
    #author=Field()

class ContentItem(Item):
    url=Field()
    content=Field()
    #author=Field()
