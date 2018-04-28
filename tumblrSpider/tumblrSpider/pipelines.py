# -*- coding: utf-8 -*-

from scrapy.pipelines.files import FilesPipeline
from scrapy.http.request import Request
from scrapy.exceptions import DropItem
import requests
import os

class TumblrspiderPipeline(FilesPipeline):
    
    def file_path(self, request, response=None, info=None):
        
        path = request.meta['file_path']
        return path
    
    def get_media_requests(self, item, info):
        
        file_url = item['file_url']
        file_path = item['file_path']
        yield Request(file_url, meta={'file_path': file_path})
    
    def item_completed(self, results, item, info):
        
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            print(results)
            raise DropItem("Item contains no images")
        return item

class MyFilesPipeline(object):
    
    def __init__(self):
        
        self.file_store = './MyData/'
        self.proxies = {'http': '1270.0.1:1080', 'https': '127.0.0.1:1080'}
        
        if not os.path.exists(self.file_store):
            os.mkdir(self.file_store)
            
    def file_request(self, url, flag=1, timeout=5):
        
        try:
            r = requests.get(url, proxies=self.proxies, timeout=timeout)
            return r
        except TimeoutError:
            timeout += 2
            return self.file_request(url, flag, timeout)
        except:
            if flag <= 3:
                flag += 1
                return self.file_request(url, flag, timeout)
            else:
                return None
    
    def process_item(self, item, spider):
        
        url = item['file_url']
        file_dir = self.file_store + item['file_type']
        path = self.file_store + item['file_path']
        
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        if os.path.exists(path):
            return item
        
        r = self.file_request(url)
        if r:
            with open(path, 'wb') as f:
                f.write(r.content)
        
        return item