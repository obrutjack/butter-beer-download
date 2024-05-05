"""
參考此篇 https://github.com/VaasuDevanS/google-podcast-downloader
從 Google Podcast 下載奶油啤酒全部錄音檔為範例.

Author: obrutjack
Date: 20240505
"""

import requests
from bs4 import BeautifulSoup

import re

response = requests.get(
    "https://podcasts.google.com/feed/aHR0cHM6Ly9vcGVuLmZpcnN0b3J5Lm1lL3Jzcy91c2VyL2NrZndjdWNycWE1dmEwODAwYmhxbHcwajI?sa=X&ved=0CBEQlvsGahcKEwjInL6p6_WFAxUAAAAAHQAAAAAQCg")
soup = BeautifulSoup(response.text, "html.parser")
# 完整頁面
#print(soup.prettify()) 

# 參考應擷取位址
divs = soup.find_all("div", attrs={'class': 'oD3fme'})
dates = soup.find_all("div", attrs={'class': 'OTz6ee'})
names = soup.find_all("div", attrs={'class': 'e3ZUqe'})

# 檢查檔名
#for div in names:
#	name = div.text
#	name = re.sub('[/:*?"<>|]+', '', name)
#	file_name = f'{name}.mp3'
#	print(file_name)

for div in divs:

	name = div.find("div", attrs={'class': 'e3ZUqe'}).text
	name = re.sub('[/:*?"<>|]+', '', name)
	file_name = f'{name}.mp3'
	
	url = div.find("div", attrs={"jsname": "fvi9Ef"}).get("jsdata")
	url = url.split(";")[1]

	file_name_url = f'{file_name} - {url}'

	print(file_name_url)

	podcast = requests.get(url)
	with open(rf"{file_name}", "wb") as out:
		out.write(podcast.content)
