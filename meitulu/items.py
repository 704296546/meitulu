# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituluItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    albname = scrapy.Field()
    downloadlink = scrapy.Field()
