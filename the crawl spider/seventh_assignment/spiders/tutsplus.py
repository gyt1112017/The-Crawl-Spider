# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QuotesToScrapeCrawlSpider(CrawlSpider):
    name = 'quotestoscrapecrawl'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='tag']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
            yield {
                'text': response.xpath("//span[@class='text']/text()").extract_first()
            }
