import request #connects to the webpage , which returns to the html 
import urllib.request
import bs4
from bs4 import BeautifulSoup as soup 

url_full = "https://www.yelp.com/search?find_desc=&find_loc=cal+state+fullerton&ns=1"

website = request.get(url_full);

ParsedObject = soup(website.text, "html.parsers")

distance_search = "<span class="domtags--span__373c0__1VGzF">0.7 Miles</span>"

x = soup.find ("span", "domtags--span__373c0__1VGzF")

print(x)