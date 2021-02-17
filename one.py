from datetime import datetime

import scrapy


class OneSpider(scrapy.Spider):
    name = 'one'

    allowed_domains = ['jin10.com']
    start_urls = ['https://www.jin10.com/']

    def parse(self, response):
        print(datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))
        div_list = response.xpath('//div[@class="jin-flash_list tw-change-box"]/div')
        for data in div_list:
            datatime = data.xpath('./div/div/text()').extract_first()
            content = data.xpath('./div/div/div/div/div/text()').extract_first()

            # 加粗的匹配
            if content == None:
                content = data.xpath('./div/div/div/div/div/b/text()').extract_first()
            if datatime != None and content != None:
                yield {
                    "datatime":datatime,
                    "content":content
                }
        yield scrapy.Request("https://www.jin10.com/", callback=self.parse, dont_filter=True)

