import requests
from b4 import BeautifulSoup
page = 1

def web_spider(max_pages):
	while page <= max_page:
		url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
		source = requests.get(url)
		plain_text = source.tex
		soup = BeautifulSoup(plain_text)
		for link in soup.findAll('a', {'class': 'item-name'}):
			href = "https://buckysroom.org" + link.get('href')
			title = link.string
			print(href)
			print(title)
		page += 1
    
web_spider(1)