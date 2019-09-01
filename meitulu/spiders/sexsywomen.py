# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request
from ..items import MeituluItem
#from ..settings import beauty


class SexsywomenSpider(scrapy.Spider):
    name = 'sexsywomen'
    allowed_domains = ['meitulu.com']
    start_urls = ['https://www.meitulu.com/t/sevenbaby/']
    #start_urls = ['https://www.meitulu.com/t/' + beauty + '/']
    base_url = 'https://www.meitulu.com'
    nextpage = start_urls
    albtitle = ''
    alblink = ''

    def parse(self, response):
        for album_title in response.xpath('//div[@class="boxs"]/ul/li/a[@href]').extract():
            pat_alblist = 'https://[a-zA-Z0-9/\\.]*html'
            pat_albtitle = 'alt=(.+)]"'
            self.albtitle = re.search(pat_albtitle, album_title).group(0)[5:-1]
            self.alblink = re.search(pat_alblist, album_title).group(0)
            #alblink_use = alblink
            yield Request(self.alblink, callback=self.getsingleimg, meta={"albtitle":self.albtitle})
            if not response.xpath('//div[@id="pages"]/a/@href').extract():
                if self.nextpage != response.xpath('//div[@id="pages"]/a/@href').extract()[-1]:
                    self.nextpage = response.xpath('//div[@id="pages"]/a/@href').extract()[-1]
                    #nextpage_link = nextpage
                    yield Request(self.nextpage, callback=self.parse)

    def getsingleimg(self, response):
        for singlelink in response.xpath('//div[@class="content"]/center/img/@src').extract():
            item = MeituluItem()
            albtitle = response.meta["albtitle"]
            item['albname'] = albtitle
            item['downloadlink'] = singlelink
            yield item
        if self.alblink != self.base_url + response.xpath('//div[@id="pages"]/a[@class="a1"]/@href').extract()[-1]:
            self.alblink = self.base_url + response.xpath('//div[@id="pages"]/a[@class="a1"]/@href').extract()[-1]
            #alblink_use = alblink
            yield Request(self.alblink, callback=self.getsingleimg, meta={"albtitle":albtitle})
