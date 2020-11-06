from bs4 import BeautifulSoup
import requests
import csv


def fetch_links(xkcd_url):
    xkcd_links = {}

    while True:
        response = requests.get(xkcd_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")

            # find the previous page link
            previous_page_link = soup.find('a', rel='prev')
            link = "https://xkcd.com" + previous_page_link["href"]
        
            # finds the image link
            links = soup.find('div', id="comic")
            image_link = "https:" + links.img["src"]
    
            xkcd_links[link] = image_link
            xkcd_url = link

            if xkcd_url.endswith("/1/"):
               break
        else:
            response.raise_for_status()

    return xkcd_links


def write_to_csv(image_and_page_links):

    with open('xkcd_website_links.csv', 'w') as file:
        csvwriter = csv.writer(file, delimiter=',')
        csvwriter.writerow(['Page Link', 'Image Link'])
        for page_link, image_link in image_and_page_links.items():
            csvwriter.writerow([page_link, image_link])


if __name__ == "__main__":
    xkcd_url = "https://xkcd.com"
    image_and_page_links = fetch_links(xkcd_url)
    write_to_csv(image_and_page_links)