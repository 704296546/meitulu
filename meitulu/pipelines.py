# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import requests
from pathlib import *
import os
import pymongo
#from .settings import Mongo_db, Mongo_url, beauty

class MeituluPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.sexsywomen
        self.beautydb = self.db['sevenbaby']

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_url=crawler.settings.get('Mongo_url'),
    #         mongo_db=crawler.settings.get('Mongo_db')
    #     )

    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.mongo_url),
    #     self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        #print ('开始下载',item['albname'])
        pp = Path('G:\sweety\girl\image\夏美酱',item['albname'],item['downloadlink'].split('/')[-1])
        headers = {
            'Referer': 'https://www.meitulu.com/item/' + item['downloadlink'].split('/')[-2] + '.html'
        }
        pp = str(pp)
        pp_dir = Path('G:\sweety\girl\image\夏美酱',item['albname'])
        self.beautydb.update({"albname": item['albname']}, {'$set': {"albname": item['albname']}}, True)
        # if not os.access(pp_dir, os.F_OK):
        #     os.makedirs(pp_dir)
        # else:
        #     pass
        # if not os.path.exists(pp):
        #     try:
        #         imgs = requests.get(item['downloadlink'],headers=headers)
        #         with open(pp, 'ba+')as f:
        #             f.write(imgs.content)
        #     except Exception as e:
        #         print(e.args,pp)
        #         # print(headers)
        #         # print(item['downloadlink'])
        #         print('errorcomic')
        # else:
        #     pass
            #print('图片已存在')