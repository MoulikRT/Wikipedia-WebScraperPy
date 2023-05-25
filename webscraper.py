import requests
from bs4 import BeautifulSoup as bs

def some(i,dir,url):
    with open(dir+str(i)+'.html','w') as f:
        c = requests.get(url)
        f.write(c.content)
        
url = ""
dir= ""
f = requests.get(url)
bsobj = bs(f.content, 'html.parser')

unique_links = []

for link in bsobj.find_all('a'):
    href = link.get('href')
    if 'www' not in str(href): href = "https://en.wikipedia.org" + str(href)
    if 'https://en.wikipedia.org/wiki/' in href and '.svg' not in href and 'jpg' not in href: unique_links.append(href)
    if len(unique_links) >= 50:
        break
i= 0 
for link in unique_links:
    some(i,dir,link)