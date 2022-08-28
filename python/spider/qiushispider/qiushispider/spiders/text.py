# -*- coding: utf-8 -*-
import scrapy
from ..items import QiushispiderItem
import re


class TextSpider(scrapy.Spider):
    name = 'text'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        print(response.url)

        link_list = response.xpath('//div[@id="content-left"]/div/a[1]/@href').extract()
        for link in link_list:
            
            url = 'http://www.qiushibaike.com'+link
            print(url)
            request = scrapy.Request(url,callback=self.parse_content)
            yield request


        #翻页 爬取总共10页
        page = int(re.search('page/(\\d+)/$',response.url).group(1))
        if page<4:
            url_next=f'http://www.qiushibaike.com/text/page/{str(page+1)}/'
            req = scrapy.Request(url_next,callback=self.parse)
            yield req

    def parse_content(self,response):
        print(response.status)
        title = response.xpath('//div[@id="articleSideLeft"]/a/div[1]/span[1]/text()').extract()[0]
        content = ''.join(response.xpath('//div[@id="single-next-link"]/div/text()').extract())
        print(title,content)
        item = QiushispiderItem()
        item['title'] = title.strip()
        item['content'] = content.strip()
        yield item








'''
//div[@id="content-left"]/div/a[1]
//*[@id="qiushi_tag_122119644"]/a[1]
//*[@id="qiushi_tag_122157105"]/a[1]


//div[@id="articleSideLeft"]/a/div[1]/span[1]  标题
//div[@id="single-next-link"]/div              内容


#qiushi_tag_122119644 > a.contentHerf
document.querySelector("#qiushi_tag_122119644 > a.contentHerf")


https://www.qiushibaike.com/text/page/2/

'''