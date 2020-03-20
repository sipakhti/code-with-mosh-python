from bs4 import BeautifulSoup as bs
import requests

search = input("Enter search term: ")
params = {"q":search}
r = requests.get("http://www.bing.com/search",params=params)

soup = bs(r.text,features="html.parser")
print(soup.prettify())
