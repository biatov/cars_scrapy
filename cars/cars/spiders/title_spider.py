import scrapy

from cars.items import CarsItem
from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class TitleSpider(CrawlSpider):
    name = "cars_title"

    allowed_domains = ['www.brightontoyota.com.au']

    start_urls = ['http://www.brightontoyota.com.au/used-car/list/?p=1']

    rules = (Rule(LinkExtractor(allow='/?p=\d+'), callback='parse_item'),)

    def parse_item(self, response):

        root = Selector(response)

        for each in root.xpath('//ul[@class="invList"]/li'):
            item = CarsItem()
            title = each.xpath('.//a[@class="invListTitle"]/h3/text()').extract()[0]
            price = each.xpath('.//div[@class="actualPrice"]/p/text()').extract()[0]
            item['title'] = '%s - %s' % (title, price)
            yield item
