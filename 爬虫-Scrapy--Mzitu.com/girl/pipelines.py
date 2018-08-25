# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
class GirlPipeline(object):
    def process_item(self, item, spider):
        
        headers ={
        # DEFAULT_REQUEST_HEADERS = {
        # 'Host': 'i.meizitu.net',
        # 'Pragma': 'no-cache',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        # 'Cache-Control': 'no-cache',
        # 'Connection': 'keep-alive',
        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
        # 'Chrome/59.0.3071.115 Safari/537.36',
        # 'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer':  'http://www.mzitu.com/',
        }
        print("使用了header..........")
        #base_dir = os.getcwd()
        local_dir = 'Z:\\pic'
        local_file = local_dir + '\\' + item['images']
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        #文本文件
        with open(local_file,'wb') as f:
            print("对于需要下载的图片的headers定制设置")
            #content是二进制编码，这里是再一次请求访问图片的URL，下载到本地
            f.write(requests.get(item['image_urls'],headers=headers).content)
        print("当前item下载到本地完成..........")
        return item
    
