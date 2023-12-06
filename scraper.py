import requests
from bs4 import BeautifulSoup

# specify the URL of the website you want to scrape
url = 'https://www.codewithharry.com/'

# send a GET request to the URL
response = requests.get(URL)

#parse the HTML content of the page 
soup = BeautifulSoup(response.text,'html.parser')

#extract information based on HTML structure
title = soup.title.text
paragraph = soup.find_all('p')

#print or process the extracted information 
print(f'title: {title}')
print('paragraph:')
for paragraph in paragraphs:
    print(paragraph.text)
else:
    print(f'error: unable to retrieve the webpage (status code:{response.status_code})')