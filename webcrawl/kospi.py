from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

all_divs = soup.find_all('span',attrs={'id':'KOSPI_now'})
#print(all_divs)
res = [span.string for span in all_divs]
for i in res:
    all_divs = soup.find_all('span', attrs={'id': 'time3'})
    print(i,all_divs)