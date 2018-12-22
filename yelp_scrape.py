import requests #connects to the webpage , which returns to the html 
import urllib.request
import bs4
from bs4 import BeautifulSoup as soup 

url_full = "https://www.yelp.com/search?find_desc=&find_loc=cal+state+fullerton&ns=1"

website = requests.get(url_full);

ParsedObject = soup(website.text, "html.parser")

ParsedObject1 = soup(website.text, "html.parser")

#distance_search = <span class="domtags--span__373c0__1VGzF">0.7 Miles</span>

x = ParsedObject.find_all ("a", "lemon--a__373c0__1_OnJ link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5")

y = ParsedObject.find_all ("h3", "lemon--h3__373c0__5Q5tF heading--h3__373c0__1n4Of alternate__373c0__1uacp")

for i in y: 
	print(i.text)
