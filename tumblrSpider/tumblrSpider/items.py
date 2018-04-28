# -*- coding: utf-8 -*-

import scrapy


class TumblrspiderItem(scrapy.Item):

    file_url = scrapy.Field()
    file_path = scrapy.Field()
    file_type = scrapy.Field()