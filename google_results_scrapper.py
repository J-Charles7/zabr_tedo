import requests
import time
from bs4 import BeautifulSoup

url =  "https://www.google.com/search?q=site:bf&ie=UTF-8&num=10&start="
domains = set()
for index in range(13):
    start_number = index * 10
    print(start_number)
    fetched_raw_code = requests.get(url + str(start_number))
    soup = BeautifulSoup(fetched_raw_code.content, 'html.parser')
    div_urls_only = soup.findAll('div', {'class' : 'kCrYT'})
    for item in div_urls_only:
        try:
            print(item.a['href'].split('/')[3])
            domains.add(item.a['href'].split('/')[3])
        except TypeError:
            pass
    time.sleep(5)
    print()

print(len(domains))
print(domains)