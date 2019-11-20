import requests
import time
from bs4 import BeautifulSoup
import os

GOUT='googleScrap.txt' 

url =  "https://www.google.com/search?q=site:bf&ie=UTF-8&num=10&start="
domains = set()
domains_number = 0
with open(GOUT, 'w') as fd:
    for index in range(20):
        start_number = index * 10
	 #print(start_number)
	fetched_raw_code = requests.get(url + str(start_number))
	soup = BeautifulSoup(fetched_raw_code.content, 'html.parser')
	div_urls_only = soup.findAll('div', {'class' : 'kCrYT'})
	print("[+] En cours de collecte : Page {0} de google...".format(index+1))
	for item in div_urls_only:
	     try:
                 fd.write('{0}\n'.format(item.a['href'].split('/')[3]))
                 domains.add(item.a['href'].split('/')[3])
		 domains_number = domains_number + 1
             except TypeError:
                 pass
	time.sleep(5)
print("\n-----------------------------------")
print("[-] {0} domaines collectes".format(domains_number))
print("\n[-] URLs collectees dans ce fichier {0}".format(GOUT))
print("\n------------------------------------")
	#print()







