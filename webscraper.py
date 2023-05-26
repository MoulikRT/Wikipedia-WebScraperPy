import requests
from bs4 import BeautifulSoup as bs

    
        
url = "https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem"
f = requests.get(url)
bsobj = bs(f.content, 'html.parser')

unique_links = []

for link in bsobj.find_all('a'):
    href = link.get('href')
    if 'www' not in str(href): href = "en.wikipedia.org" + str(href)
    if 'en.wikipedia.org/wiki/' in href and '.svg' not in href and ':' not in href and 'jpg' not in href: unique_links.append(href)
    if len(unique_links) >= 500:
        break

with open('output.txt','w') as f:
        i= 0 
        for link in unique_links:
            print(i, "/", len(unique_links)-1)
            f.write(str(link)+"\n")
            i+=1