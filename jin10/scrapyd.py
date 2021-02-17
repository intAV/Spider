import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ScrapydSpider(CrawlSpider):
    name = 'scrapyd'
    allowed_domains = ['scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn']

    rules = (
        Rule(LinkExtractor(allow=r'http://lab.scrapyd.cn/page/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://lab.scrapyd.cn/archives/\.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        name = response.xpath('//h1/a/text()').extract_first()
        content = response.xpath('//div[@class="post-content"]/p/text()').extract()
        tag = response.xpath('//p[@class="tags"]/a/text()').extract()

        if name != None and len(content) > 0 and len(tag) > 0:
            yield {
                "name":name,
                "content":content,
                "tag":tag
            }
