# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#定义每条数据为一个Item,
#以下是每条数据有的属性，即是一个Item有的字段
class GirlItem(scrapy.Item):
    	images = scrapy.Field()
    	image_urls = scrapy.Field()
    	