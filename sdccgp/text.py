import requests
from lxml import etree
from selenium import webdriver




#html = requests.get('http://ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp?colcode=0301')
# print(html)
#
# htmlx = etree.HTML(html.text)
#
# print(htmlx)
#
# names = htmlx.xpath('//td[@class='"'Font9'"']')[:-1]
# print(len(names))
# for note in names:
#     print(note.xpath('a/text()'))
#
#     print(note.xpath('a/@href'))
#
#     print(note.xpath('text()'))
# next_page = htmlx.xpath('//td[@class='"'Font9'"']')[-1]

browser = webdriver.Firefox()
browser.get('http://ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp?colcode=0301')
browser.find_element_by_link_text('下一页').click()

