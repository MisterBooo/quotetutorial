# -*- coding: utf-8 -*-
import scrapy
from urllib import parse

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('./span[@class="text"]/text()').extract()
            author = quote.xpath('.//small[@class="author"]/text()').extract()
            tags = response.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()

        next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_url is not  None:
            print(next_url)
            yield scrapy.Request(response.urljoin(next_url))

        pass
