# -*- coding: utf-8 -*-
import scrapy 
from scrapy import Request
from scrapy.spiders import Spider
from girl.items import GirlItem

class MzituSpider(scrapy.Spider):
	print("............生成爬取请求.............")
	name = 'Mzitu'
	allowed_domains = ['mzitu.com']
	start_urls = []
	print(".................生成爬取的主页数....................")
	for i in range(1,2):
		start_urls.append("http://www.mzitu.com/page/"+str(i)+"/")
	print(".................生成爬取的主页数....................")
#等待从Engine返回的response，进行这页面解析
	def parse(self, response):
		print("正在爬取主页")
		whole_page=response.xpath('//ul[@id="pins"]/li')
	#解析每一项，找到套图网址，进行跳转
		for each_item in whole_page:
			Eachgirl_url=each_item.xpath('.//a/@href').extract()[0]
	#data_parse作为回调函数，其实就是调用了它，但是parse不用被修改。。。
		yield Request(Eachgirl_url,callback=self.data_parse)
#进入套图网页，进行相似解析操
	def data_parse(self,response):
		item=GirlItem()
		item["images"]=response.xpath('//div[@class="main-image"]/p/a/img/@src')[0].extract().split('/')[-1]
		item["image_urls"]=response.xpath('//div[@class="main-image"]/p/a/img/@src')[0].extract()
		print("套图分页添加一个item信息完成！")
		yield item
		print("找到套图的下一页.........")
		next_url = response.xpath('//div[@class="pagenavi"]/a/@href')[-1].extract()
		if next_url is not None:
			print("继续调用data_parse")
			yield scrapy.Request(next_url, callback=self.data_parse)