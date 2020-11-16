import scrapy


class BookdetailsSpider(scrapy.Spider):
    name = 'bookdetails'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        """
        Parses the home page of
        books.toscrape.com and returns
        the travel page link.
        """
        travel_page_path = response.xpath("//ul[@class='nav nav-list']/li/ul/li[1]/a[@href]")\
            .xpath("@href").extract_first()
        travel_page_url = response.urljoin(travel_page_path)
        if travel_page_url:
            yield scrapy.Request(url=travel_page_url, callback=self.browse_book_details_link)


    def browse_book_details_link(self, response):
        """
        Identifies and returns the product description
        link for each book item.
        """
        all_book_items = response.xpath("//ol[@class='row']/ \
        li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']")\
        .extract()
        count_book_items = len(all_book_items)

        for item_count in range(1, count_book_items):
            details_page = response.xpath(f"//ol[@class='row']/li[{item_count}] \
            [@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']/ \
            article[@class='product_pod']/h3/a[@href]").xpath("@href").get()
            details_page_link = response.urljoin(details_page)
            if details_page_link:
                yield scrapy.Request(url=details_page_link, callback=self.parse_details)


    def parse_details(self, response):
        """
        Parses the book details
        """
        yield {
            "image_link": response.urljoin(response.xpath("//article[@class='product_page']/\
                div[@class='row']/div[@class='col-sm-6']/div[1]/div[1]/div[1]/div[1]/\
                    img[@src]").xpath("@src").get()),
            "book_title": response.xpath("//article[@class='product_page']/div[@class='row']/ \
                div[@class='col-sm-6 product_main']/h1/text()").get(),
            "price": response.xpath("//article[@class='product_page']/div[@class='row']/ \
                div[@class='col-sm-6 product_main']/p[@class='price_color']/text()").get(),
            "description": response.xpath("//article[@class='product_page']/p/text()").get(),
        }
            