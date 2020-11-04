# Select CSS elements
# Q18. Write a Python program to print the element(s) that has a specified id of a given web page.

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org").text
soup = BeautifulSoup(page, 'lxml')
print(soup.select_one("#python-network"))