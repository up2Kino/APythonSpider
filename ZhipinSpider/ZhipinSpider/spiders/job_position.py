# -*- coding: utf-8 -*-
import scrapy
import sys
# import sys,os
# # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(r"D:\Python\workspace\ZhipinSpider\ZhipinSpider")
# print(sys.path)
from ZhipinSpider.items import  ZhipinspiderItem


class JobPositionSpider(scrapy.Spider):
    #蜘蛛的名字
    name = 'job_position'

    #定义蜘蛛只爬取哪些域名
    allowed_domains = ['zhipin.com']

    #从哪个页面开始爬取
    start_urls = ['https://www.zhipin.com/?sid=sem_pz_bdpc_dasou_title']



    def parse(self, response):
        #response代表Scrapy下载器所获取的目标的响应
        #和shell调试中response对象完全一样
        
        #每个job_box包含一个工作信息
        for job_box in response.xpath('//div[@class="common-tab-box job-tab-box"]/ul/li'):
            #为每份工作创建一个item对象
            item = ZhipinspiderItem()

            #获取包含工作信息的div
            job_info = job_box.xpath('./div[@class="sub-li"]')
            item['title'] = job_info.xpath('./a/p/text()').extract()[0]
            item['work_spot'] = job_info.xpath('./a/p/text()').extract()[1]
            item['experience'] = job_info.xpath('./a/p/text()').extract()[2]
            item['edu'] = job_info.xpath('./a/p/text()').extract()[3]
            item['company'] = job_info.xpath('./a/p/text()').extract()[4]

            item['salary'] = job_info.xpath('./a/p/span/text()').extract()[0]
            item['recruiter'] = job_info.xpath('./a/p/span/text()').extract()[1]
            #item('title') = job_info.xpath('./a/p/span/text()').extract()[2]

            yield item
            
        # new_links = response.xpath('')
        # if new_links and len(new_links)>0 ：
        #     new_link = new_links[0]
        #     #制定之后的域名
        #     yield scrapy.Request('域名'+new_link,callback=self.parse())


