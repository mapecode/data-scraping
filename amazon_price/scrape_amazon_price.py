# source: https://hackernoon.com/scraping-amazon-product-information-with-python-and-beautifulsoup-yn4s3tgr

from bs4 import BeautifulSoup
import requests

url = ''

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, features="lxml")

# get title
title = soup.select("#productTitle")[0].get_text().strip()

# get price
price = soup.select("#priceblock_ourprice")[0].get_text().strip()

print(title, price)