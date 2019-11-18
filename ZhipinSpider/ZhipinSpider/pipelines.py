# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class ZhipinspiderPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('job.db')
        self.c = self.conn.cursor()
        self.c.execute('create table if not exists job_tb('
            + 'id integer primary key autoincrement,'
            + 'title,'
            + 'salary,'
            + 'work_spot,'
            + 'experience,'
            + 'edu,'
            + 'company,'
            + 'recruiter)')


    #该方法中的item就是蜘蛛yield的item
    def process_item(self, item, spider):
        self.c.execute('insert into job_tb values(null,?,?,?,?,?,?,?)',
        (item['title'],item['salary'],item['work_spot'],item['experience'],item['edu'],item['company'],item['recruiter'])
        )

        #执行语句之后必须提交业务，不然不会更新
        self.conn.commit()


    #定义一个新的函数，使得蜘蛛关闭时，使程序关闭文件
    def close_spider (self,spider):
        print('----关闭数据库资源----')
        self.c.close()
        self.conn.close()




        # print('工作名称',item['title'])
        # print('工作地点',item['work_spot'])
        # print('要求的工作经历',item['experience'])
        # print('要求的学历',item['edu'])
        # print('来自公司',item['company'])
        # print('工资',item['salary'])
        # print('招聘者',item['recruiter'])
