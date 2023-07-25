import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging

# Create constant for urls
base_url = "https://www.flipkart.com"
base_search_url = "https://www.flipkart.com/search?q="
query_url = "tv"

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

product_url = base_url + item_container[2].div.div.div.a['href']
print(product_url)

for i in item_container:
    pass
    #print(base_url + i.div.div.div.a['href'])

product_request = requests.get(product_url)
product_html = bs(product_request.text, 'html.parser')
comment_container = product_html.find_all("div",{"class": "_16PBlm"})
print(len(comment_container))
#print(comment_container[0].div.div.div.div.text)

# Get all ratings for a single product
""" for i in comment_container:
    pass
    #print(i.div.div.div.div.text) """

# Commenter's Name
print(comment_container[0].div.div.find_all("p",{"class": "_2sc7ZR _2V5EHH"}))

# Rating
print(comment_container[0].div.div.div.div.text)

# Rating in words
print(comment_container[0].div.div.div.p.text)

# Actual comment
print(comment_container[0].div.div.find_all("div",{"class": ""})[0].text)