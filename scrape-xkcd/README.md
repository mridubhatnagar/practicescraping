Scrape Comics present on XKCD website.

This project is built using Beautiful Soup.
The scraper scrapes the image and page urls from xkcd comic website.

Update:
At the moment scraped data is first stored in-memory in a dictionary and then dictionary is parsed to write data to csv. Instead, directly data can be written to csv and there is no need to store the data in-memory.

Learning
- BeautifulSoup
- Dealing with pagination while scraping
- writing the scraped data to CSV file
