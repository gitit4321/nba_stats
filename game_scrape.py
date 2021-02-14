from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import pprint

year = 2021

url = "https://www.basketball-reference.com/boxscores/202102090POR.html"

html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')

# match = soup.find('div', class_='section_wrapper box-POR box-POR-game').encode("utf-8")
# print(match)

match = soup.find('table', id='box-POR-game-basic')

starter_headers = [th.getText() for th in match.findAll('tr', limit=2)[1].findAll('th')]
print(starter_headers) 

reserves_headers = [th.getText() for th in match.find('tr', class_='thead').findAll('th')]
print(reserves_headers)

rows = match.findAll('tbody')

players = [[tr.getText() for tr in rows[i].findAll('tr')] for i in range(len(rows))]


player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]

stats = pd.DataFrame(player_stats, columns = starter_headers)
print(stats.head(5))