import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging

# Create constant for urls
base_url = "https://www.flipkart.com/search?q="
query_url = "iphone11"

# Open url
url_client = urlopen(base_url+query_url)
print(url_client)
