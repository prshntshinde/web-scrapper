import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging

# Create constant for urls
base_url = "https://www.flipkart.com"
base_search_url = "https://www.flipkart.com/search?q="
query_url = "iphone11"

# Open url
url_client = urlopen(base_search_url+query_url)
#print(url_client)
flipkart_page = url_client.read()
#print(flipkart_page)

flipkart_html = bs(flipkart_page,'html.parser')
#print(flipkart_html)
item_container = flipkart_html.find_all("div", {"class": "_1AtVbE col-12-12"})
#print(item_container)

del item_container[0:3]

#print(item_container[0].div.div.div.a['href'])

product_url = base_url + item_container[0].div.div.div.a['href']
#print(product_url)

for i in item_container:
    pass
    #print(base_url + i.div.div.div.a['href'])

product_request = requests.get(product_url)
product_html = bs(product_request.text, 'html.parser')
comment_container = product_html.find_all("div",{"class": "_16PBlm"})
#print(comment_container[0].div.div.div.div.text)

# Get all ratings for a single product
""" for i in comment_container:
    pass
    #print(i.div.div.div.div.text) """


comment_container[0].div.div