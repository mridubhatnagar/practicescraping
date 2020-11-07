The scraper scrapes the image and page urls from xkcd comic website.

Update:
At the moment scraped data is first stored in-memory in a dictionary and then dictionary is parsed to write data to csv. Instead, directly data can be written to csv and there is no need to store the data in-memory.