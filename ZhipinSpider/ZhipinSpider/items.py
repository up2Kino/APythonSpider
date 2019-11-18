# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhipinspiderItem(scrapy.Item):
    # define the fields for your item here like:
    #工作名字
    title = scrapy.Field()

    #工资
    salary = scrapy.Field()

    #招聘公司
    company = scrapy.Field()

    #工作详细链接
    url = scrapy.Field()

    #工作地点
    work_spot = scrapy.Field()

    #行业
    industry = scrapy.Field()

    #招聘者
    recruiter = scrapy.Field()

    #工作经验
    experience = scrapy.Field()

    #学历
    edu = scrapy.Field()

