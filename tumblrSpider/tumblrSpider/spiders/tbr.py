# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from tumblrSpider.items import TumblrspiderItem
import re
import json


class TbrSpider(scrapy.Spider):
    name = 'tbr'
    allowed_domains = ['tumblr.com']
    start_urls = ['https://showgis.tumblr.com/']
    max_depth = 4
    
    meta = {
            'dont_redirect': True,
            'handle_httpstatus_list': [301, 302]
            }
    
    
    def start_requests(self):
        
        for url in self.start_urls:
            user_name = re.findall(r'://([^\.]*)\.tumblr\.com', url)[0]
            print(user_name)
            url = '''https://{}.tumblr.com/api/read/json?start=0&num=200'''.format(user_name)
            yield Request(url, headers=self.get_headers(), meta={'depth': 0})
            
    def parse(self, response):
        
        data = response.text[22:-2]
        data = json.loads(data)
        
        posts = data['posts']
        for post in posts:
            if post['type'] == 'regular':
                regular_body = post['regular-body']
                try:
                    video_id = re.findall(r'/(tumblr_[^_]*)_[^\.]*?\.jpg', regular_body)[0]
                    video_id = video_id.split('.')[0]
                    video_url = 'https://ve.media.tumblr.com/{}.mp4'.format(video_id)
                    video_name = video_url.split('/')[-1]
                    video_path = post['type'] + '/' + video_name


                    item = TumblrspiderItem()
                    item['file_url'] = video_url
                    item['file_path'] = video_path
                    item['file_type'] = post['type']
                    yield item

                except IndexError:
                    print(regular_body)

            if post['type'] == 'video':
                video_player = post['video-player']
                try:
                    video_id = re.findall(r'/(tumblr_[^_]*)_[^\.]*?\.jpg', video_player)[0]
                    video_url = 'https://vtt.tumblr.com/{}_480.mp4'.format(video_id)
                    video_name = video_url.split('/')[-1]
                    video_path = post['type'] + '/' + video_name
                    
                    item = TumblrspiderItem()
                    item['file_url'] = video_url
                    item['file_path'] = video_path
                    item['file_type'] = post['type']
                    yield item
                
                except IndexError:
                    print(video_player)
                    
            elif post['type'] == 'photo':
                photo_url = post['photo-url-1280']
                photo_name = photo_url.split('/')[-1]
                photo_path = post['type'] + '/' + photo_name
                
                item = TumblrspiderItem()
                item['file_url'] = photo_url
                item['file_path'] = photo_path
                item['file_type'] = post['type']
                yield item
                
            else:
                print(post['type'])
                
                
            try:
                reblogged_url = post['reblogged-from-url']
            except KeyError:
                continue
            try:
                user_name = re.findall(r'://([^\.]*)\.tumblr\.com', reblogged_url)[0]
            except IndexError:
                continue
            print(user_name)
            url = '''https://{}.tumblr.com/api/read/json?start=0&num=200'''.format(user_name)
            
            depth = response.meta['depth'] + 1
            
            if depth <= self.max_depth:
                
                yield Request(url, headers=self.get_headers(), 
                              callback=self.parse, meta={'depth': depth})
                    
    def get_headers(self):
        
        headers = {':authority': 'mypussynet.tumblr.com',
                   ':scheme': 'https', 
                   ':method': 'GET',
                   ':path': '/',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
                   'accept-encoding': 'gzip,deflate,br', 
                   'accept-language': 'zh-CN,zh;q=0.9', 
                   'cache-control': 'no-cache',  
                   'pragma': 'no-cache', 
                   'upgrade-insecure-requests': '1',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
                    }
        return headers
