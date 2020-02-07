
from bs4 import BeautifulSoup
import urllib.request
import os



url = "https://en.wikipedia.org/wiki/Deep_learning"
source_code = urllib.request.urlopen(url)
plain_text = source_code
soup = BeautifulSoup(plain_text, "html.parser")
heading = soup.find(id="firstHeading").text
print(heading)

web_links = soup.find_all('a')
for link in web_links:
    print(link.get('href'))
