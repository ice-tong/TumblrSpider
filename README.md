# TumblrSpider
使用scrapy编写的python爬虫，爬取汤不热上用户发布的图片与视频，下载到本地。

### 项目结构
	1. 爬虫：tbr.py
	2. 中间件: middlewares.py
	3. items: items.py
	4. 下载管道: pipelines.py
	
### 项目依赖
  * scrapy
  * requests
  * ssr(或其他科学上网工具)
### 使用方法 
  * 确保自己的电脑能够访问 https://www.tumblr.com/ 。
  * `./tumblrSpider/tumblrSpider/spiders/tbr.py` 文件中，在start_urls中填入一个种子用户的主页地址。max_depth 可设置最大爬取深度。
  * 在 `./tumblrSpider` 路径下， 使用命令 `scrapy crawl tbr` 
