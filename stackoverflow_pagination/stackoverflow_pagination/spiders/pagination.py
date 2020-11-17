import scrapy


class PaginationSpider(scrapy.Spider):
    name = 'pagination'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions/tagged/python?sort=frequent&pageSize=15']

    def parse(self, response):
        questions_count = len(response.xpath("//div[@id='mainbar']/div[@id='questions']/ \
        div[@class='question-summary']").extract())
        print(questions_count, "parse method")

        for count in range(1, questions_count+1):
            yield {
                "votes": response.xpath(f"//div[{count}][@class='question-summary']/div[1]/div[1]/div[1]/div[1]/span[@class='vote-count-post ' or @class='vote-count-post high-scored-post']/strong/text()").get(),
                "views": response.xpath(f"//div[{count}][@class='question-summary']/div[1]/div[2]").xpath("@title").get(),
                "question": response.xpath(f"//div[{count}][@class='question-summary']/div[2]/h3/a/text()").get(),
                "question_page_link": response.urljoin(response.xpath(f"//div[{count}][@class='question-summary']/div[2]/h3/a[@href]").xpath("@href").get()),
                "post_excerpt": response.xpath(f"//div[{count}][@class='question-summary']/div[2]/div[1]/text()").get(),
                "tags": response.xpath(f"//div[{count}][@class='question-summary']/div[2]/div[2]/a/text()").extract()
            }

        next_page_path = response.xpath("//div[@class='s-pagination pager fl']/a[last()][@href]").xpath("@href").get()
        next_page_url = response.urljoin(next_page_path)
        print(next_page_url, next_page_path)
        yield scrapy.Request(url=next_page_url, callback=self.parse)