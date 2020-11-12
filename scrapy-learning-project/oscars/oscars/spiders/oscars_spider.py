import scrapy

class OscarsSpider(scrapy.Spider):
    name = "oscars"
    allowed_domains = "en.wikipedia.org"
    start_urls = ['https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture']


    def parse(self, response):
        data = {}
        data['title'] = response.css('title::text').extract()
        yield data
