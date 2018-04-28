# -*- coding: utf-8 -*-


BOT_NAME = 'tumblrSpider'

SPIDER_MODULES = ['tumblrSpider.spiders']
NEWSPIDER_MODULE = 'tumblrSpider.spiders'

FILES_STORE = './data/'
FILES_EXPIRES = 90	
FEED_EXPORT_ENCODING = 'utf-8'

DOWNLOADER_MIDDLEWARES = {
    'tumblrSpider.middlewares.LocalProxySpiderMiddleware': 543,
}

ITEM_PIPELINES = {
    'tumblrSpider.pipelines.TumblrspiderPipeline': 2,
#    'tumblrSpider.pipelines.MyFilesPipeline': 1,
}

HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
