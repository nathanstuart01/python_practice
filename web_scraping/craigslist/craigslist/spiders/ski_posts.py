# -*- coding: utf-8 -*-
import scrapy


class SkiGearSpider(scrapy.Spider):
    name = 'ski_posts'
    allowed_domains = ['craigslist.org/']
    start_urls = ['https://saltlakecity.craigslist.org/d/for-sale/search/sss']

    def parse(self, response):
        posts = response.xpath('//p[@class="result-info"]')
        for post in posts:
        	title = post.xpath('a/text()').extract_first()
        	price = post.xpath('span[@class="result-meta"]/span[@class="result-price"]/text()').extract_first()
        	relative_url = post.xpath('a/@href').extract_first()
        	absolute_url = response.urljoin(relative_url)

        	yield{'URL': absolute_url, 'Title':title, 'Price': price}