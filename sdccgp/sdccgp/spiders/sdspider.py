# -*- coding: utf-8 -*-
import scrapy
from sdccgp.items import SdccgpItem
from selenium import webdriver
from scrapy import spider,Request
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
import time
from lxml import etree


class SdspiderSpider(scrapy.Spider):
    name = 'sdspider'
    allowed_domains = ['ccgp-shandong.gov.cn']
    start_urls = ['']

    def __init__(self):
        self.brower = webdriver.Firefox()
        self.brower.set_page_load_timeout(30)


    def start_requests(self):
        """使用selenium翻页并生成详情页链接"""
        start_url = ['http://ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp?colcode=0301']
        for url in start_url:
            self.brower.get(url)
            while self.brower.find_element_by_link_text('下一页'):
                html = etree.HTML(self.brower.page_source)
                for note in html.xpath('//td[@class="Font9"]')[:-1]:
                    #构建url并将项目名称和时间作为参数传入
                    note_url = note.xpath('a/@href')[0]
                    note_name = note.xpath('a/text()')[0].replace(" ","")
                    note_time = note.xpath('text()')[3].replace(' ','')
                    url = 'http://ccgp-shandong.gov.cn' + note_url + '&note_name='
                    yield Request(url=url)
                self.brower.find_element_by_link_text('下一页').click()
            for note in self.brower.find_elements_by_xpath('//td[@class="Font9"]')[:-1]:
                url = 'http://ccgp-shandong.gov.cn' + note.xpath('a/@href')[0]
                yield Request(url=url)
            print('爬取一个分类')


    def closed(self,spider):
        print('spider close')
        self.brower.close()


    def parse(self,response):
        print('开始获取数据')
        item = SdccgpItem()
        item['uuid'] =
        item['name'] =
        item['href'] = response.url
        print('完成获取数据')

        yield item






