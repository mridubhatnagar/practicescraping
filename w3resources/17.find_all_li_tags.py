# Q17. Write a Python program to find and print all li tags of a given web page.

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.w3resource.com").text
soup = BeautifulSoup(page, "lxml")

for tag in soup.find_all('li'):
    print(tag.name + ": " + tag.text)


