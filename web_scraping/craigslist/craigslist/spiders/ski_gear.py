# -*- coding: utf-8 -*-
import scrapy


class SkiGearSpider(scrapy.Spider):
    name = 'ski_gear'
    allowed_domains = ['craigslist.org/']
    start_urls = ['https://saltlakecity.craigslist.org/d/for-sale/search/sss']

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        print(titles)