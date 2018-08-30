# -*- coding: utf-8 -*-
import scrapy
from sdccgp.items import SdccgpItem
from selenium import webdriver
from scrapy import spider,Request
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
import time


class SdspiderSpider(scrapy.Spider):
    name = 'sdspider'
    allowed_domains = ['ccgp-shandong.gov.cn']
    start_urls = ['']

    def __init__(self):
        self.brower = webdriver.Firefox()
        self.brower.set_page_load_timeout(30)


    def start_requests(self):
        """使用selenium"""
        start_url = ['http://ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp?colcode=0301']
        for url in start_url:
            self.brower.get(url)
            self.get_next_page()


    def get_next_page(self):
        urls = [note.xpath('a/@href').extract() for note in self.brower.find_elements_by_xpath('//td[@class="Font9"]')[:-1]]
        for url in  urls:
            yield Request(url=url)
        time.sleep(3)
        try:
            self.brower.find_element_by_link_text('下一页').click()
            self.get_next_page()
        except:
            print("爬取结束")





    def closed(self,spider):
        print('spider close')
        self.brower.close()


    def parse_response(self,response):
        print('开始获取数据')
        item = SdccgpItem()
        item['name'] = '完成'
        print('完成获取数据')

        yield item
