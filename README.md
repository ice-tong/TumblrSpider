# TumblrSpider
使用scrapy编写的python爬虫，爬取汤不热上用户发布的图片与视频，下载到本地。


### 项目结构
  * 爬虫：`tbr.py`
    1. 利用tumblr的一个接口：`https://username.tumblr.com/api/read/json?start=0&num=200` 获取用户post的内容。
    2. 获取用户post的视频或图片url。
    3. 若是reblogged的内容则将被转发的该用户加入爬取，可设置爬取深度。
    
  * 中间件: `middlewares.py`
    1. 设置代理，因为某种原因，不能直接上tumblr，所以需要科学上网后才行，ssr开全局模式后可以无需代理直接爬，若是PAC模式则需要添加本地代理。
    2. 也可以直接添加国外代理IP
  
  * items: `items.py`
    1. 三个字段，分别为`file_url`, `file_path`和`file_type`。
  
  * 下载管道: `pipelines.py`
    1. scrapy文件下载两种方式，用FilesPipeline或者requests。
    2. `TumblrspiderPipeline` 是用文件pipeline写的pipeline。
    3. `MyFilesPipeline` 是用requests方式写的pipeline。
    4. 相同网络环境下，前者比后者速度快，所以使用第一种pipeline就行。

### 项目依赖
  * scrapy
  * requests
  * ssr(或其他科学上网工具)
  
### 使用方法 
  * 确保自己的电脑能够访问 https://www.tumblr.com/ 。
  * `./tumblrSpider/tumblrSpider/spiders/tbr.py` 文件中，在start_urls中填入一个种子用户的主页地址。max_depth 可设置最大爬取深度。
  * 在 `./tumblrSpider` 路径下， 使用命令 `scrapy crawl tbr` 
