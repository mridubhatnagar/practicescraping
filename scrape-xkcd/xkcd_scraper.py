import csv
from bs4 import BeautifulSoup
import requests



def fetch_links(xkcd_url):
    '''
    scrapes image link and
    page link.
    '''

    xkcd_links = {}
    link = ''
    image_link = '' 

    while True:
        response = requests.get(xkcd_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")

            # find the previous page link
            previous_page_link = soup.find('a', rel='prev')
            if previous_page_link:
                link = "https://xkcd.com" + previous_page_link["href"]


            # finds the image link
            links = soup.select("#comic > img")
            if links:
                image_link = "https:" + links[0]["src"]

            else:
                image_link = "could not find image"

            xkcd_links[link] = image_link
            xkcd_url = link

            if xkcd_url.endswith("/1/"):
                break
        else:
            response.raise_for_status()

    return xkcd_links


def write_to_csv(image_and_page_links):
    '''
    writes scraped image and page link
    from xkcd to csv file.
    '''

    with open('xkcd_website_links.csv', 'w') as file:
        csvwriter = csv.writer(file, delimiter=',')
        csvwriter.writerow(['Page Link', 'Image Link'])
        for page_link, image_link in image_and_page_links.items():
            csvwriter.writerow([page_link, image_link])


if __name__ == "__main__":
    URL = "https://xkcd.com"
    image_and_page_links = fetch_links(URL)
    write_to_csv(image_and_page_links)
