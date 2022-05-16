import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://www.britannica.com/biography/Mortimer-J-Adler')
soup = BeautifulSoup(website.text, 'html.parser')
name = soup.select_one('h1').text
description = soup.select_one('.topic-identifier').text
summary = soup.select_one('.topic-paragraph').text.strip()
image = soup.select_one('.fact-box-picture img').attrs['src']
birth = soup.find(attrs={'data-label': 'born'}).find('dd').get_text(separator='|').split('|')[0]
death = soup.find(attrs={'data-label': 'died'}).find('dd').get_text(separator='|').split('|')[0]
subjects_of_study = soup.find(attrs={'data-label': 'subjects of study'}).select_one('ul')
subjects_items = subjects_of_study.select('li')
subjects = ''
for item in subjects_items:
	subjects += item.text.strip() + ','
print(subjects)