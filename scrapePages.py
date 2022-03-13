from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text)
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
	if link.text.isdigit():
		x = link.get('href')
		urls.append(x)
print(urls)

def scraper(url, count):	
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')
	items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

	for i in items:
		itemName = i.find('h4', class_='card-title').text.strip('\n')
		itemPrice = i.find('h5').text
		print('%s) Item Name: %s, Price: %s' % (count, itemName, itemPrice))
		count+=1
	return count

count = 1
for i in urls:
	count = scraper(url + i, count)
	

