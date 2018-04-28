# TumblrSpider
使用scrapy编写的python爬虫，爬取汤不热上用户发布的图片与视频，下载到本地。

### 项目结构
  * 爬虫：`tbr.py`
  	1. 利用tumblr的一个接口：https://username.tumblr.com/api/read/json?start=0&num=200 获取用户post的内容。（具体见）
    	2. 获取用户post的视频或图片url。
    	3. 若是reblogged的内容则将被转发的该用户加入爬取，可设置爬取深度。
  * 中间件: `middlewares.py`
  * items: `items.py`
  * 下载管道: `pipelines.py`
	
### 项目依赖
  * scrapy
  * requests
  * ssr(或其他科学上网工具)
  
### 使用方法 
  * 确保自己的电脑能够访问 https://www.tumblr.com/ 。
  * `./tumblrSpider/tumblrSpider/spiders/tbr.py` 文件中，在start_urls中填入一个种子用户的主页地址。max_depth 可设置最大爬取深度。
  * 在 `./tumblrSpider` 路径下， 使用命令 `scrapy crawl tbr` 
