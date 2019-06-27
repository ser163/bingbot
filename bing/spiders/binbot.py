# -*- coding: utf-8 -*-
import scrapy
from bing.items import BingItem


class BinBotSpider(scrapy.Spider):
    name = 'binbot'
    allowed_domains = ['cn.bing.com']
    start_urls = ['https://cn.bing.com']

    def parse(self, response):
        context = response.xpath('//*[@id="bgLink"]')
        item = BingItem()
        bg_image = self.start_urls[0] + context.xpath("//@href").extract_first()
        item['imgurl'] = bg_image
        yield item
