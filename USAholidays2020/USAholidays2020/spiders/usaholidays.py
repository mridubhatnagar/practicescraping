import scrapy
import csv


class UsaholidaysSpider(scrapy.Spider):
    name = 'usaholidays'
    allowed_domains = ['https://www.officeholidays.com']
    start_urls = ['https://www.officeholidays.com/countries/usa/']
    row_values = []

    def parse(self, response):
        headers = response.xpath("//table[@class='country-table']/thead/tr/th/text()").extract()
        table_length = len(response.xpath("//table[@class='country-table']/tbody/tr").extract())
        
        with open("usa_holidays_2020.csv", 'w') as file:
            csvwriter = csv.writer(file, delimiter=',')
            csvwriter.writerow(headers)
            for row in range(1, table_length):
                for column in range(1, 6):
                    if column == 1:
                        day = response.xpath(f"//table[@class='country-table']/tbody/tr[{row}]/td[{column}]/text()").get()
                    elif column == 2:
                        date = response.xpath(f"//table[@class='country-table']/tbody/tr[{row}]/td[{column}]/time/text()").get()
                    elif column == 3:
                        holiday_name = response.xpath(f"//table[@class='country-table']/tbody/tr[{row}]/td[{column}]/a/text()").get()
                    elif column == 4:
                        type_ = response.xpath(f"//table[@class='country-table']/tbody/tr[{row}]/td[{column}]/text()").get()
                    elif column == 5:
                        comment = response.xpath(f"//table[@class='country-table']/tbody/tr[{row}]/td[{column}]/text()").get()
                csvwriter.writerow([day, date, holiday_name, type_, comment])
