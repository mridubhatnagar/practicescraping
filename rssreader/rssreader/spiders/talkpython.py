import scrapy
import csv

class TalkpythonSpider(scrapy.Spider):
    name = 'talkpython'
    allowed_domains = ['https://talkpython.fm/episodes/rss_full_history']
    start_urls = ['https://talkpython.fm/episodes/rss_full_history']

    def parse(self, response):

        response.selector.remove_namespaces()

        title = response.xpath("//item/title/text()").extract()
        description = response.xpath("//item/description/text()").extract()
        published_date =  response.xpath("//item/pubDate/text()").extract()
        link =  response.xpath("//item/link/text()").extract()


        with open('tmp/talkpython.csv', 'w') as file:
            csvwriter = csv.writer(file, delimiter=',')
            fieldnames = ["title", "description", "published_date", "link"]
            csvwriter.writerow(fieldnames)
            for element in zip(title, description, published_date, link):
                csvwriter.writerow([element[0], element[1], element[2], element[3]])